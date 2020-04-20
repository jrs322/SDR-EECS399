import subprocess
def rtl_fm_call(fm_type, frequency, sample_rate, gain="0", squelch="0",
		approx=None, E=None ):
    args_list = ["rtl_fm", "-f "+frequency,"-M "+fm_type,
		"-s "+sample_rate, "-g "+gain,
		"-l "+squelch]
    if E != None:
        args_list.append("-E "+E)
    if approx != None:
        args_list.append("-A "+approx)
    ps = subprocess.Popen(args_list, stdout=subprocess.PIPE, stdin= subprocess.PIPE)

rtl_fm_call(fm_type="wbfm",frequency="89.1M", sample_rate="12k")
