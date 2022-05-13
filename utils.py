import cv2
import numpy as np
from pathlib import Path
from pymouse import PyMouse
from typing import List, Optional, Tuple


class MouseAction:
    def __init__(self) -> None:
        self._m = PyMouse()
        self.screen = self._m.screen_size()

    def mouse_action(
        self, fshape: List[int], position: List[int], action: Optional[str] = None
    ):
        factorx, factory = self.asratio(self.screen, fshape)
        pos_x, pos_y = position
        self._m.move(pos_x * factorx, pos_y * factory)
        if action is not None:
            self._m.click()

    @staticmethod
    def asratio(screen, fshape):
        xs, ys = screen
        xf, yf = fshape
        return xs // xf, ys // yf

    @staticmethod
    def eye_position(left: Optional[Tuple], right: Optional[Tuple]):
        if left == right:
            return 100, 100
        xl, yl = left
        xr, yr = right
        x, y = (xl + xr) // 2, (yl + yr) // 2
        return x, y


class ReadWebcam:  # for inference
    # YOLOv5 local webcam dataloader, i.e. `python detect.py --source 0`
    def __init__(self, pipe="0"):
        self.pipe = eval(pipe) if pipe.isnumeric() else pipe
        self.cap = cv2.VideoCapture(self.pipe)  # video capture object
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # set buffer size

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if cv2.waitKey(1) == ord("q"):  # q to quit
            self.cap.release()
            cv2.destroyAllWindows()
            raise StopIteration

        # Read frame
        ret_val, img0 = self.cap.read()
        img0 = cv2.flip(img0, 1)  # flip left-right

        # Print
        assert ret_val, f"Camera Error {self.pipe}"

        # Convert
        img = img0.copy()
        return img, img.shape

    def __len__(self):
        return 0


class ReadVideo:
    def __init__(self, path, img_size=640, stride=32, auto=True):
        self.img_size = img_size
        self.stride = stride
        self.auto = auto
        path = str(Path(path).resolve())  # os-agnostic absolute path
        self.cap = cv2.VideoCapture(path)
        self.frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count + 1 == self.frames:  # last video
            raise StopIteration
        else:
            _, img = self.cap.read()
        self.count += 1
        return img, img.shape

    def __len__(self):
        return self.frames  # number of files


def annotate(frame: np.array, text: str, LP: Tuple[int], RP: Tuple[int]):
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, "Left pupil:  " + str(LP), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(RP), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    return frame