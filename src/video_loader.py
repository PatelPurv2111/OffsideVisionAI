import cv2
def load_video(video_path):
    cap=cv2.VideoCapture(video_path)
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        yield frame
    cap.release()