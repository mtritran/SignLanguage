# Hệ thống nhận diện ngôn ngữ ký hiệu bằng Random Forest

Hệ thống này sử dụng **Random Forest Classifier** để nhận diện ngôn ngữ ký hiệu (Sign Language) thông qua hình ảnh bàn tay, với các ký hiệu tương ứng với 26 chữ cái tiếng Anh (A-Z). Hệ thống bao gồm các bước: thu thập dữ liệu, huấn luyện mô hình, và đánh giá kết quả.

## Mục lục

- [Tính năng](#tính-năng)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cấu trúc dữ liệu](#cấu-trúc-dữ-liệu)
- [Hướng dẫn cài đặt](#hướng-dẫn-cài-đặt)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
- [Kết quả](#kết-quả)
- [Cảm ơn](#cảm-ơn)

## Tính năng

- Thu thập dữ liệu hình ảnh trực tiếp từ camera.
- Huấn luyện mô hình nhận diện ngôn ngữ ký hiệu dựa trên **Random Forest**.
- Chuyển đổi ký hiệu ngôn ngữ ký hiệu thành văn bản hiển thị và đọc bằng giọng nói.
- Hỗ trợ giao diện đồ họa thân thiện (GUI) sử dụng **Tkinter**.

## Yêu cầu hệ thống

### Phần cứng
- Camera (để thu thập dữ liệu từ người dùng).

### Phần mềm
- IDE Pycharm
- Python 3.9+
- Thư viện cần thiết:
  - OpenCV
  - MediaPipe
  - Tkinter 
  - Scikit-learn
  - NumPy
  - Pyttsx3
  - Pillow

## Cấu trúc dữ liệu

- Dữ liệu hình ảnh được tổ chức trong thư mục `Data`, với mỗi lớp ký tự (A-Z) lưu trữ trong một thư mục riêng.
- Dữ liệu hình ảnh được gắn nhãn bằng cách lưu các tên thư mục tương ứng với ký tự.

Ví dụ cấu trúc thư mục:
```
Data/
├── A/
│   ├── 0.jpg
│   ├── 1.jpg
│   └── ...
├── B/
│   ├── 0.jpg
│   ├── 1.jpg
│   └── ...
...
├── Z/
│   ├── 0.jpg
│   ├── 1.jpg
│   └── ...
```

## Hướng dẫn cài đặt

1. **Clone dự án**:
   ```bash
   git clone https://github.com/mtritran/SignLanguage
   cd sign-language
   ```

2. **Cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

## Hướng dẫn sử dụng

### 1. Thu thập dữ liệu
- Chạy chương trình thu thập dữ liệu:
  ```bash
  python collect_imgs.py
  ```
- Chọn kí tự muốn thu thập dữ liệu (A-Z) và nhấn nút `Start Collection`. Mỗi lớp sẽ thu thập 150 ảnh.
![Screenshot 2024-11-29 092237](https://github.com/user-attachments/assets/51dce76c-b1bf-495a-9bc6-5de2fb7e5433)
- Kết quả thu thập sẽ lưu tất cả các ảnh của của từng kí tự trong folder `Data`.
![image](https://github.com/user-attachments/assets/600daa37-ba51-44a2-a87f-351b0b4730a4)

### 2. Xử lý ảnh và lưu tọa độ ảnh vào file pickle:
- Chạy chương trình xử lý ảnh với thư : 
  ```bash
  python create_dataset.py
  ```
- Kết quả xử lý sẽ lưu lại file `data.pickle`.
![image](https://github.com/user-attachments/assets/3a87fbfb-47b9-4c44-acfb-045654347632)
  
### 3. Huấn luyện mô hình
- Chạy chương trình huấn luyện:
  ```bash
  python train_classifier.py
  ```
- Kết quả huấn luyện sẽ lưu mô hình đã huấn luyện trong file `data.p`.
![image](https://github.com/user-attachments/assets/940d61ed-9b45-41a6-bbad-003fe01c667a)

### 4. Sử dụng hệ thống nhận diện
- Chạy chương trình nhận diện:
  ```bash
  python inference_classifier.py
  ```
- Hệ thống sẽ sử dụng camera để nhận diện ký hiệu và hiển thị kết quả trong giao diện người dùng.
![Screenshot 2024-11-29 195204](https://github.com/user-attachments/assets/03f3c220-40d6-45bc-9216-be182e46cc8c)
- Nhấn vào nút speak để đọc các từ đã nhận diện hoặc nhấn clear để xóa hết các từ vừa nhận diện.

## Kết quả

- Độ chính xác: **<Hiển thị độ chính xác mô hình ở đây, ví dụ: 95%>**.
- Báo cáo chi tiết:
  - Sử dụng confusion matrix và classification report để đánh giá mô hình.

## Cảm ơn

Dự án này được hoàn thành với sự hỗ trợ của:
- [Mediapipe](https://mediapipe.dev) cho xử lý hình ảnh bàn tay.
- [Scikit-learn](https://scikit-learn.org/) cho mô hình Random Forest.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) cho giao diện đồ họa.

--- 
