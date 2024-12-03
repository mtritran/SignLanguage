import pickle
import cv2
import mediapipe as mp
import numpy as np
import time
import pyttsx3
import tkinter as tk
from tkinter import messagebox, font
import threading
from PIL import Image, ImageTk


class SignLanguageTranslator:
    def __init__(self, model_path='D:\SignLanguageMediapipe\SignLanguageMediapipe\data.p'):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Load ML model
        self.model_dict = pickle.load(open(model_path, 'rb'))
        self.model = self.model_dict['model']

        # Define labels
        self.labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']


        # MediaPipe setup
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

        # Translation parameters
        self.predicted_character = ""
        self.displayed_text = "Text: "
        self.start_time = None
        self.hold_duration = 2

        # Create main window
        self.root = tk.Tk()
        self.root.title("Sign Language Translator")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')

        # Setup UI
        self.setup_ui()

        # Start camera thread
        self.camera_thread = threading.Thread(target=self.process_camera, daemon=True)
        self.camera_active = True
        self.camera_thread.start()

    def setup_ui(self):
        # Main Frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Camera Preview
        self.camera_label = tk.Label(main_frame, bg='black')
        self.camera_label.pack(pady=10, expand=True)

        # Translated Text Display
        text_frame = tk.Frame(main_frame, bg='#f0f0f0')
        text_frame.pack(pady=10, fill=tk.X)

        self.text_display = tk.Text(text_frame, height=3, width=50,
                                    font=('Helvetica', 14), wrap=tk.WORD)
        self.text_display.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        # Buttons Frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(pady=10)

        # Speak Button
        speak_btn = tk.Button(button_frame, text="Speak", command=self.speak_text,
                              bg='#4CAF50', fg='white', font=('Arial', 12))
        speak_btn.pack(side=tk.LEFT, padx=10)

        # Clear Button
        clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_text,
                              bg='#F44336', fg='white', font=('Arial', 12))
        clear_btn.pack(side=tk.LEFT, padx=10)

        # Close Button
        close_btn = tk.Button(button_frame, text="Close", command=self.on_closing,
                              bg='#2196F3', fg='white', font=('Arial', 12))
        close_btn.pack(side=tk.LEFT, padx=10)

        # Bind closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def process_camera(self):
        cap = cv2.VideoCapture(0)

        while self.camera_active:
            data_aux = []
            x_, y_ = [], []

            ret, frame = cap.read()
            if not ret:
                break

            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Drawing hand landmarks
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style()
                    )

                    # Prepare data for prediction
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10
                    x2 = int(max(x_) * W) + 10
                    y2 = int(max(y_) * H) + 10

                    # Prediction with error handling
                    try:
                        prediction = self.model.predict([np.asarray(data_aux)])

                            # Handle different possible prediction formats
                        if isinstance(prediction[0], (np.str_, str)):
                            current_character = prediction[0]
                            if current_character == '_':
                                current_character = ' '
                        elif isinstance(prediction[0], (np.integer, int)):
                            current_character = self.labels[int(prediction[0])]
                        else:
                            current_character = self.labels[int(prediction[0][0])]
                    except Exception as e:
                        print(f"Prediction error: {e}")
                        continue

                    # Character holding logic
                    if current_character == self.predicted_character:
                        if self.start_time is None:
                            self.start_time = time.time()
                        elif time.time() - self.start_time >= self.hold_duration:
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), -1)
                            cv2.putText(frame, current_character, (x1, y1 - 10),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

                            # Update text
                            if current_character == ' ':
                                self.displayed_text += ' '
                            else:
                                self.displayed_text += current_character

                            # Reset start time
                            self.start_time = None
                    else:
                        self.predicted_character = current_character
                        self.start_time = time.time()

                    # Draw rectangle and character
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, current_character, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

            # Update text display
            self.root.after(0, self.update_text_display)

            # Convert frame for Tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            photo = ImageTk.PhotoImage(image=image)

            # Update camera label
            self.root.after(0, self.update_camera_display, photo)

        cap.release()

    def update_camera_display(self, photo):
        self.camera_label.configure(image=photo)
        self.camera_label.image = photo

    def update_text_display(self):
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, self.displayed_text)

    def speak_text(self):
        text_to_speak = self.displayed_text.replace("Text: ", "")
        if text_to_speak.strip():
            self.engine.say(text_to_speak)
            self.engine.runAndWait()

    def clear_text(self):
        self.displayed_text = "Text: "
        self.text_display.delete(1.0, tk.END)

    def on_closing(self):
        self.camera_active = False
        self.root.destroy()

    def run(self):
        self.root.mainloop()


def main():
    translator = SignLanguageTranslator()
    translator.run()


if __name__ == "__main__":
    main()