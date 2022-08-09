# <div align="center">Eye Control</div>

<!-- <div align="center">
<p>Multi-Object Tracking with YOLOv5 and Norfair tracker</p>
<p>
[![Total alerts](https://img.shields.io/lgtm/alerts/g/1chimaruGin/EyeControl.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/1chimaruGin/EyeControl/alerts/)
</p>
<p>
<img src="images/car.gif" width="270"/> <img src="images/race.gif" width="270"/> 
</p>
</div> -->

## Installation

Clone this repository.

```bash
git clone git@github.com:1chimaruGin/EyeControl.git
```

Create conda env and install opencv, dlib, etc..
```bash
conda env create --file env.yml
```

Install other requirements via pip.
```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## References

* https://github.com/antoinelame/GazeTracking
* https://github.com/NVlabs/few_shot_gaze
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
