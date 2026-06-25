<img width="583" height="629" alt="logo" src="https://github.com/user-attachments/assets/adb133f1-b7a2-4bb0-8fd8-10a76deb409c" />

# transitsong
Sonification of TESS lightcurves between 200-900 Hz. 

## How to install:
```pip install transitsong```

### Dependencies:
- numpy
- sounddevice
- lightkurve
- matplotlib
- scipy
- moviepy

## How to use:
```import transitsong```<br>
```from transitsong.main import Transit```<br>
```transit = Transit(tic_id, sector, window)```<br>
- tic_id: str
- sector: int
- window (optional): list of length 2, start and end of desired section (Barycentric TESS Julian Date)
