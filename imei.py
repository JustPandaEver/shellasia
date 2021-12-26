import subprocess
imei = (subprocess.check_output(['getprop','persist.radio.imei'])[:-1])
print(imei.decode("utf-8"))
