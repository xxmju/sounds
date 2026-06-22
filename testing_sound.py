import numpy as np
import sounddevice as sd 
import lightkurve as lk
import matplotlib.pyplot as plt 

tic = 124029677 
sector = 33

search_result = lk.search_lightcurve(
        f"TIC {tic}",
        mission="TESS",
        author="SPOC",
        sector =[sector]
    )

lc = search_result.download()

lc_fluxes = lc.flux.value
lc_times = lc.time.value

med_value = np.median(lc_fluxes)
all_flux_ratio = lc_fluxes/med_value

freq_maps = ()

samplerate = 44100
duration = 2.0

for flux in lc_fluxes:
    ratio_to_median = flux/med_value

    frequency = 440.0

    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    audio_signal = 0.5 * np.sin(2*np.pi*frequency*t)

    sd.play(audio_signal, samplerate)
    sd.wait()


