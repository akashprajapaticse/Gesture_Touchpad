import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Get screen resolution
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)

# Gesture states
left_click_flag = False
right_click_flag = False
scroll_start_y = None

def distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get fingertip positions
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            
            index_x, index_y = int(index_finger.x * w), int(index_finger.y * h)
            screen_x, screen_y = int(index_finger.x * screen_w), int(index_finger.y * screen_h)
            
            # Move mouse
            pyautogui.moveTo(screen_x, screen_y, duration=0.1)
            
            # Left click gesture (Thumb & Index close)
            if distance((thumb.x, thumb.y), (index_finger.x, index_finger.y)) < 0.05:
                if not left_click_flag:
                    pyautogui.click()
                    left_click_flag = True
            else:
                left_click_flag = False
                
            # Right click gesture (Thumb & Middle close)
            if distance((thumb.x, thumb.y), (middle_finger.x, middle_finger.y)) < 0.05:
                if not right_click_flag:
                    pyautogui.rightClick()
                    right_click_flag = True
            else:
                right_click_flag = False
                
            # Scroll gesture (Two-finger vertical movement)
            middle_y = int(middle_finger.y * h)
            if abs(index_y - middle_y) > 20:
                if scroll_start_y is None:
                    scroll_start_y = index_y
                scroll_amount = (scroll_start_y - index_y) // 5
                pyautogui.scroll(scroll_amount)
            else:
                scroll_start_y = None
    
    cv2.imshow("Gesture Touchpad", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
