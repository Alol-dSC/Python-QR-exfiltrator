# Python-QR-exfiltrator
I saw this video on Hak5's YT channel (https://www.youtube.com/watch?v=WBkNgb-iPGE) that showed data exfiltration using QR codes so I tried recreating it with python

## Prerequisites 
This script is meant to run on python 2.x a linux machine, I'll probably make it windows compatible in the future.
As a prerequisite you need qrcode and zbarimg installed, for that you just need to
```bash
pip install qrcode
sudo apt-get install zbar-tools
````
In a later version you'll be able to just dump all your files into Data2QR and it'll convert everything into one gif, for now you can only convert a single textfile (testfile.txt)

## Usage
To convert to a gif put your file in Data2Txt and run ```bash python qr_exfil.py``` from inside it's directory
A gif should apear in the upper directory

To convert back to text leave the gif as is and run ```bash python back2text.py``` from inside it's directory
A textfile should appear
