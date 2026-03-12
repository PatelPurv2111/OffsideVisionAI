import numpy as np

previous_ball = None

def detect_pass(ball):
    global previous_ball
    if ball is None:
        return False
    if previous_ball is None:
        previous_ball = ball
        return False
    speed = np.linalg.norm(np.array(ball[:2]) - np.array(previous_ball[:2]))
    previous_ball = ball
    return speed > 25