import qrcode
import base64
import os

n = 500
txt = open("testfile.txt","r")
enc = base64.b64encode(txt.read())

lpoe =  [enc[i:i+n] for i in range(0, len(enc), n)]

for i in  range(len(lpoe)):
	cmd = 'qr "' +  lpoe[i] + '" > poe' + str(i) +'.jpg'
	os.system(cmd)

os.system("convert -delay 20 -loop 0 poe*.jpg ../output.gif")
os.system("rm poe*.jpg")
