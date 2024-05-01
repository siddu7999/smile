import cv2
from deepface import DeepFace

def main():

    cap = cv2.VideoCapture(0)
    
    # Checking if the camera opened successfully
    if not cap.isOpened():
        print("Error: Cannot open camera.")
        return
    
    # Loading Haar cascade for face detection
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Converting frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detecting faces in the image
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        
        
        for (x, y, w, h) in faces:
            # Extract the face from the frame
            face_frame = frame[y:y+h, x:x+w]
            
            try:
                # Analyzing the face for emotion
                results = DeepFace.analyze(face_frame, actions=['emotion'], enforce_detection=False)
                
                # Processing each result
                for result in results:
                    if result['dominant_emotion'] == 'happy':
                        emotion_text = "Smiling"
                    else:
                        emotion_text = "Not Smiling"

                   
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            except Exception as e:
                print(f"Error during emotion detection: {e}")
                emotion_text = "Detection Error"
                cv2.putText(frame, emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Video', frame)
        
        # Break the loop with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
