import os
import cv2
import tkinter as tk
from tkinter import messagebox
import threading
import time


class DatasetCollector:
    def __init__(self, classes, dataset_size=150, output_dir='Data'):
        self.classes = classes
        self.dataset_size = dataset_size
        self.output_dir = output_dir

        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Setup camera
        self.cap = cv2.VideoCapture(0)

        # Create main window
        self.root = tk.Tk()
        self.root.title("Dataset Image Collector")

        # Create UI elements
        self.setup_ui()

    def setup_ui(self):
        # Class selection
        self.class_var = tk.StringVar(self.root)
        self.class_var.set(self.classes[0])  # default value

        tk.Label(self.root, text="Select Class:", font=('Arial', 12)).pack(pady=10)
        class_dropdown = tk.OptionMenu(self.root, self.class_var, *self.classes)
        class_dropdown.pack(pady=10)

        # Progress indicators
        self.progress_label = tk.Label(self.root, text="Ready to collect", font=('Arial', 12))
        self.progress_label.pack(pady=10)

        self.collection_button = tk.Button(self.root, text="Start Collection", command=self.start_collection,
                                           font=('Arial', 12), bg='green', fg='white')
        self.collection_button.pack(pady=20)

        # Camera preview
        self.canvas = tk.Label(self.root)
        self.canvas.pack(padx=20, pady=20)

        # Start camera preview
        self.update_camera_preview()

    def update_camera_preview(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert frame to RGB for Tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize for better display
            frame_resized = cv2.resize(frame_rgb, (640, 480))

            # Convert to Tkinter-compatible image
            from PIL import Image, ImageTk
            img = Image.fromarray(frame_resized)
            imgtk = ImageTk.PhotoImage(image=img)

            self.canvas.imgtk = imgtk
            self.canvas.configure(image=imgtk)

        self.canvas.after(10, self.update_camera_preview)

    def start_collection(self):
        current_class = self.class_var.get()
        class_dir = os.path.join(self.output_dir, current_class)

        # Create class directory if it doesn't exist
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

        # Disable button during collection
        self.collection_button.config(state=tk.DISABLED)

        # Start collection in a separate thread
        threading.Thread(target=self.collect_images, args=(current_class, class_dir), daemon=True).start()

    def collect_images(self, current_class, class_dir):
        # Countdown
        for i in range(3, 0, -1):
            self.progress_label.config(text=f"Collecting images for class {current_class} in {i}...")
            time.sleep(1)

        counter = 0
        while counter < self.dataset_size:
            ret, frame = self.cap.read()

            # Update progress
            self.progress_label.config(text=f"Collecting {current_class}: {counter + 1}/{self.dataset_size}")

            # Save image
            cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)

            counter += 1
            time.sleep(0.1)  # Small delay between captures

        # Reset UI
        self.progress_label.config(text="Collection Complete!")
        self.collection_button.config(state=tk.NORMAL)

        # Show completion message
        tk.messagebox.showinfo("Dataset Collection",
                               f"Completed collecting {self.dataset_size} images for class {current_class}")

    def run(self):
        self.root.mainloop()

    def __del__(self):
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()


def main():
    classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']

    collector = DatasetCollector(classes, dataset_size=150)
    collector.run()


if __name__ == "__main__":
    main()