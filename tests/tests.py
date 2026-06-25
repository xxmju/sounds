import sys
from pathlib import Path

parallel_dir = Path(__file__).resolve().parent.parent / "transitsong/"
sys.path.append(str(parallel_dir))

from main import Transit
#from transitsong.main import Transit
import pytest

# test that lightcurve downloads ok! 

def test_lc_download():
    tic = 124029677 
    sector = 33

    transit = Transit(tic, sector)

    assert len(transit.norm_flux) == len(transit.time), "Time and flux arrays are not the same length"
    assert len(transit.norm_flux) > 0, "norm flux array, time array is of length 0"


# def test_value_error_in_window(): 
#     tic = 124029677 
#     sector = 33
#     transit = Transit(tic, sector, window=[0, 1])
#     print(transit.success)
    
#     assert transit.success is False, "window had issues"

# end to end test

def test_check_folder_products():
    tic = 124029677 
    sector = 33
    window = [2217, 2220]

    planet = Transit(tic, sector, window=window)
    planet.make_sound_arr()
    planet.make_video()
    planet.combine()

    song_file_loc = planet.song_path + f"TIC{planet.tic}_S{planet.sector}_SONG.wav"
    dance_file_loc = planet.dance_path + f"TIC{planet.tic}_S{planet.sector}_DANCE.mp4"
    song_and_dance_file_loc = planet.song_and_dance_path + f"TIC{planet.tic}_S{planet.sector}_FINAL.mp4" 

    assert Path(song_file_loc).is_file()
    assert Path(dance_file_loc).is_file()
    assert Path(song_and_dance_file_loc).is_file()

test_lc_download()
test_check_folder_products()

#test_value_error_in_window()
