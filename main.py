import cv2
import numpy as np
from gaze_tracking import GazeTracking
from utils import MouseAction, ReadWebcam, ReadVideo, annotate


class EyeControl:
    """
    Control the mouse with eyes
    """
    def __init__(self, source: str = "") -> None:
        self.gaze = GazeTracking()
        self.mouse = MouseAction()
        self.streams = ReadVideo(source) if source != "0" else ReadWebcam()

    def start(self):
        for frame, fshape in self.streams:
            frame, LP, RP, text = self.gaze_meta(frame)
            x, y = self.mouse.eye_position(LP, RP)
            self.mouse.mouse_action(fshape[:2], [x, y])

            frame = annotate(frame, text, LP, RP)
            cv2.imshow("Demo", frame)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break

    def gaze_meta(self, frame: np.array):
        gaze = self.gaze
        gaze.refresh(frame)
        frame = gaze.annotated_frame()
        LP = gaze.pupil_left_coords()
        RP = gaze.pupil_right_coords()
        text = ""
        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
        return frame, LP, RP, text


if __name__ == "__main__":
    source = "videoplayback.mp4"
    ec = EyeControl(source)
    ec.start()
