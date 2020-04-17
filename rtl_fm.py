import subprocess
import time

def rtl_fm_call(fm_type, frequency, sample_rate, output_rate, gain="0", squelch="0",
		approx=None, E=None ):
    args_list = ["rtl_fm", "-f "+frequency,"-M "+fm_type,
		"-s "+sample_rate, "-r "+output_rate, "-g "+gain,
		"-l "+squelch]
    if E != None:
        args_list.append("-E "+E)
    if approx != None:
        args_list.append("-A "+approx)
    ps = subprocess.Popen(args_list)
    try:
        while True:
            time.sleep(1)
    finally:
        ps.kill()

rtl_fm_call(fm_type="wbfm",frequency="89.1M", sample_rate="170k",output_rate="32k", E="s")
