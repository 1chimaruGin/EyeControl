# Eye Control

> Control the mouse with your eyes.

EyeControl is a Python app that tracks your gaze through a webcam (or video file) and moves the mouse cursor to follow your pupils. It uses dlib for face detection and 68-point facial landmarks, OpenCV for frame processing, and PyUserInput to drive the mouse.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-008000)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- Real-time gaze tracking from a webcam or a video file
- Maps pupil position to screen coordinates to move the mouse cursor
- Detects gaze direction: looking left, right, center, or blinking
- Per-eye pupil localization with automatic threshold calibration
- On-screen annotation of gaze state and pupil coordinates
- Ships with the dlib 68-point landmark model, no extra download needed

## Installation

Clone this repository.

```bash
git clone git@github.com:1chimaruGin/EyeControl.git
cd EyeControl
```

Create a conda environment with OpenCV and dlib.

```bash
conda env create --file env.yml
conda activate eyecontrol
```

Install the remaining requirements via pip.

```bash
pip install -r requirements.txt
```

The dlib landmark model (`gaze_tracking/trained_models/shape_predictor_68_face_landmarks.dat`) is included in the repository.

## Usage

Run the app:

```bash
python main.py
```

By default `main.py` reads from a video file (`videoplayback.mp4`). To use the webcam instead, set the source to `"0"` in `main.py`:

```python
ec = EyeControl("0")  # webcam
ec.start()
```

Press `Esc` to close the demo window.

## Project Structure

```
EyeControl/
├── main.py                 # Entry point: ties gaze tracking to mouse control
├── utils.py                # Mouse actions and webcam/video readers
├── gaze_tracking/
│   ├── gaze_tracking.py    # Face detection + gaze analysis
│   ├── eye.py              # Eye region isolation
│   ├── pupil.py            # Pupil detection
│   ├── calibration.py      # Pupil threshold calibration
│   └── trained_models/
│       └── shape_predictor_68_face_landmarks.dat
├── requirements.txt
└── env.yml
```

## References

- [GazeTracking](https://github.com/antoinelame/GazeTracking)
- [few_shot_gaze](https://github.com/NVlabs/few_shot_gaze)

## Citations

```
@inproceedings{Park2019ICCV,
  author    = {Seonwook Park and Shalini De Mello and Pavlo Molchanov and Umar Iqbal and Otmar Hilliges and Jan Kautz},
  title     = {Few-Shot Adaptive Gaze Estimation},
  year      = {2019},
  booktitle = {International Conference on Computer Vision (ICCV)},
  location  = {Seoul, Korea}
}
```

## License

Released under the [MIT License](LICENSE).
