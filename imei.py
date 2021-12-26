import subprocess
imei = (subprocess.check_output(['getprop','ro.ril.oem.imei'])[:-1])
print(imei.decode("utf-8"))
