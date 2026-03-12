import cv2
from src.video_loader import load_video
from src.detection import detect_objects
from src.pass_detector import detect_pass
from src.offside_detector import detect_offside
from src.visualization import draw_players, draw_ball, draw_offside_line
VIDEO_PATH = "data/match.mp4"

for frame in load_video(VIDEO_PATH):
    players, ball = detect_objects(frame)
    pass_event = detect_pass(ball)
    offside, defender_x = detect_offside(players)
    draw_players(frame, players)
    draw_ball(frame, ball)
    draw_offside_line(frame, defender_x)
    if pass_event and offside:
        cv2.putText(frame, "OFFSIDE DETECTED", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    cv2.imshow("OffsideVision VAR", frame)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()