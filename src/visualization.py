import cv2
def draw_players(frame,players):
    for p in players:
        x1,y1,x2,y2=p
        cv2.rectangle(frame, (x1,y1), (x2,y2),(0,255,0),2)
def draw_ball(frame,ball):
    if ball is None:
        return
    x1,y1,x2,y2=ball
    cv2.rectangle(frame, (x1,y1), (x2,y2),(0,0,255),2)

def draw_offside_line(frame,x):
    if x is None:
        return
    height=frame.shape[0]
    cv2.line(frame , (int(x),0),(int(x),height),(255,0,0),2)
