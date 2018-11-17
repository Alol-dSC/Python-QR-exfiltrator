import qrcode
import base64
import os

qrSize = 500 #the length in chars of each strings that gets converted to base64, zbarimg doesn't recognize over a certain threshold
txt = open("testfile.txt","r")
encText = base64.b64encode(txt.read())

data =  [encText[i:i+qrSize] for i in range(0, len(encText), qrSize)]

for i in  range(len(data)):
	cmd = 'qr "' +  data[i] + '" > data' + str(i) +'.jpg'
	os.system(cmd)

os.system("convert -delay 20 -loop 0 data*.jpg ../output.gif")
os.system("rm data*.jpg")
