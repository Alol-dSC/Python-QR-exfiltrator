import os
import base64

os.system("echo > tmp")
os.system("convert -verbose ../output.gif out.png")
for i in range (0,18):
	cmd = "zbarimg out-"+ str(i) +".png >> tmp"
	os.system(cmd)

tmp = open("tmp","r")
file = open("output","w")
j = (tmp.read()).replace("QR-Code:","").split("\n")
for i in j:
	file.write(base64.b64decode(i))
os.system('rm tmp out-*.png')
