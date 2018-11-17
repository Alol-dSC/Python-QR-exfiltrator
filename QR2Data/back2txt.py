import os
import base64

os.system("echo > tmp")
os.system("convert ../output.gif out.png")
for i in range (0,18): #the range is dependant on the size of data in each qrcode
	cmd = "zbarimg out-"+ str(i) +".png >> tmp"
	os.system(cmd)

tmp = open("tmp","r")
file = open("output","w")
j = (tmp.read()).replace("QR-Code:","").split("\n")
for i in j:
	file.write(base64.b64decode(i))
os.system('rm tmp out-*.png')
