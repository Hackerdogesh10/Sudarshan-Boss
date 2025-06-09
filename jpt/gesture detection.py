import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Detect hands
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract landmark coordinates (e.g., tip of index finger)
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])

            # Draw a circle at the fingertip
            cv2.circle(image, (x, y), 10, (0, 255, 0), -1)

    cv2.imshow('Hand Gesture', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Example: Detect a swipe gesture
prev_x = 0
threshold = 50  # Minimum horizontal movement to trigger

if results.multi_hand_landmarks:
    hand_landmarks = results.multi_hand_landmarks[0]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    current_x = int(index_tip.x * image.shape[1])

    # Check for rightward swipe
    if (current_x - prev_x) > threshold:
        print("Swipe detected! Send image.")
        # Add code to transfer image here

    prev_x = current_x
    import socket
import cv2

# Capture image from webcam
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('image_to_send.jpg', frame)

# Send via socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('RECEIVER_IP_ADDRESS', 12345))  # Replace with receiver's IP

with open('image_to_send.jpg', 'rb') as f:
    s.sendfile(f)

s.close()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)

conn, addr = s.accept()
with open('received_image.jpg', 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

conn.close()

