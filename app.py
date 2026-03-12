import streamlit as st
import cv2
from src.detection import detect_objects
from src.pass_detector import detect_pass
from src.offside_detector import detect_offside
from src.visualization import draw_players, draw_ball, draw_offside_line
import numpy as np

st.title("⚽ OffsideVision AI - VAR Prototype")

video_path = "data/match.mp4"

cap = cv2.VideoCapture(video_path)

frame_placeholder = st.empty()

previous_ball = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    players, ball = detect_objects(frame)

    pass_event = False

    if ball is not None and previous_ball is not None:
        speed = np.linalg.norm(np.array(ball[:2]) - np.array(previous_ball[:2]))

        if speed > 25:
            pass_event = True

    previous_ball = ball

    offside, defender_x = detect_offside(players)

    draw_players(frame, players)
    draw_ball(frame, ball)
    draw_offside_line(frame, defender_x)

    if pass_event and offside:
        cv2.putText(frame, "OFFSIDE DETECTED",
                    (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame, channels="RGB")