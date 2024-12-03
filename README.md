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
   git clone https://github.com/your-repo/sign-language-recognition.git
   cd sign-language-recognition
   ```

2. **Cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Tạo thư mục dữ liệu**:
   - Đảm bảo thư mục `Data` tồn tại trong dự án để lưu trữ hình ảnh.

## Hướng dẫn sử dụng

### 1. Thu thập dữ liệu
- Chạy chương trình thu thập dữ liệu:
  ```bash
  python dataset_collector.py
  ```
- Chọn kí tự muốn thu thập dữ liệu (A-Z) và nhấn nút `Start Collection`. Mỗi lớp sẽ thu thập 150 ảnh.
![Uploading image.png…]()


### 2. Huấn luyện mô hình
- Chạy chương trình huấn luyện:
  ```bash
  python train_model.py
  ```
- Kết quả huấn luyện sẽ lưu mô hình đã huấn luyện trong file `data.p`.

### 3. Sử dụng hệ thống nhận diện
- Chạy chương trình nhận diện:
  ```bash
  python sign_language_translator.py
  ```
- Hệ thống sẽ sử dụng camera để nhận diện ký hiệu và hiển thị kết quả trong giao diện người dùng.

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
