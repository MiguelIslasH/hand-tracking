import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                    max_num_hands=2,
                    min_detection_confidence=0.7,
                    min_tracking_confidence=0.7)
cap = cv2.VideoCapture(2)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            h, w, _ = image.shape

            # Pulgar (4)
            thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))

            # índice (8), medio (12), anular (16), meñique (20)
            fingertips = [8, 12, 16, 20]
            for tip in fingertips:
                finger_tip = (int(landmarks[tip].x * w), int(landmarks[tip].y * h))
                cv2.line(image, thumb_tip, finger_tip, (0, 0, 255), 2)

    cv2.imshow("Laser desde el pulgar", image)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
