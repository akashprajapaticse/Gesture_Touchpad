# ✋🖱️ Gesture-Based Touchpad

This project is a **gesture-based touchpad** implemented using **Python**, **OpenCV**, **MediaPipe**, and **PyAutoGUI**. It allows users to control the mouse pointer and perform left-click, right-click, and scrolling using hand gestures captured through a webcam.

---

## 📌 **Features**
✅ Move mouse cursor using finger gestures  
✅ Left-click using thumb and index finger pinch  
✅ Right-click using thumb and middle finger pinch  
✅ Vertical scrolling using index and middle finger distance  
✅ Real-time hand tracking and smooth cursor control  

---

## 🛠️ **Tech Stack**
- **Python** – Programming language  
- **OpenCV** – Computer vision library  
- **Mediapipe** – Hand tracking framework  
- **PyAutoGUI** – Mouse and keyboard automation  

---

## 📂 **Folder Structure**
```
├── gesture_touchpad.py      # Main Python script
├── requirements.txt         # Dependencies list
├── README.md                # Project documentation
```

---

## 🚀 **Setup and Usage**
### ✅ **1. Clone the repository**:
```bash
git clone https://github.com/akashprajapaticse/Gesture-Touchpad.git
```

### ✅ **2. Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### ✅ **3. Install dependencies**:
```bash
pip install -r requirements.txt
```

### ✅ **4. Run the application**:
```bash
python gesture_touchpad.py
```

---

## 🎯 **How It Works**
1. **Hand Tracking**  
   - Uses MediaPipe to track hand landmarks in real time.  

2. **Mouse Movement**  
   - Index finger position is mapped to screen coordinates to move the cursor.  

3. **Left Click**  
   - If the distance between the thumb and index finger is small, triggers a left click.  

4. **Right Click**  
   - If the distance between the thumb and middle finger is small, triggers a right click.  

5. **Scrolling**  
   - Vertical distance between index and middle fingers controls scrolling.  

---

## 🖥️ **Gesture Mapping**
| Gesture | Action |
|---------|--------|
| Pinch thumb and index finger | Left click |
| Pinch thumb and middle finger | Right click |
| Move index finger vertically | Scroll |

---

## 🚦 **Troubleshooting**
❗ **No Output**  
- Ensure that the webcam is properly connected.  
- Ensure that `cv2` and `mediapipe` libraries are correctly installed.  

❗ **Mouse Movement Not Working**  
- Adjust the camera position to capture hands clearly.  
- Ensure that the hand is well-lit and visible to the camera.  

---

## 🌟 **Contributing**
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-name`).  
3. Make your changes and commit (`git commit -m 'Add new feature'`).  
4. Push to the branch (`git push origin feature-name`).  
5. Create a pull request.  

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 👤 **Author**
👤 **Akash Prajapati** - [GitHub](https://github.com/akashprajapaticse)

---

## ⭐ **Show Your Support**
If you like this project, give it a ⭐ on GitHub!
