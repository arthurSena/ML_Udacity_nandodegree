# Instagram crawler

The _crawler.py_ script can be used to download a certain amount of photos from a instagram profile. 

## Getting Started

### Prerequisites

It requires the following packages:

requests 2.18.4
requests-oauthlib 0.8.0
selenium 3.7.0
urllib3 1.22

The command below will install these packages using the requirements.txt file
```console
xpto@bar:~$ pip install -r requirements.txt
```
### Running

In order to run the script, you just need to pass the profile name (-p) and the amount of photos (-a)
to be downloaded. The script will create a folder named by the instagram profile name passed and save all photos in it. See the example below:

```console
xpto@bar:~$ python crawler.py -p beaches_n_resorts -a 4
Opening browser...
Loading web page...
Scrolling to the bottom
Amount of photos' links captured so far:  25
Getting  https://instagram.frec8-1.fna.fbcdn.net/vp/ca53d5502a146d79bf82274e138c314a/5BF21FED/t51.2885-15/sh0.08/e35/c0.134.1080.1080/s640x640/37814895_452099295270163_5940012359610269696_n.jpg
Saving in  /home/arthur/Desktop/beaches_n_resorts/37814895_452099295270163_5940012359610269696_n.jpg

Getting  https://instagram.frec8-1.fna.fbcdn.net/vp/28f2f66a8d8c0e35be8092662d80243c/5C143FD1/t51.2885-19/s150x150/24175430_308389219678483_5596502820896374784_n.jpg
Saving in  /home/arthur/Desktop/beaches_n_resorts/24175430_308389219678483_5596502820896374784_n.jpg

Getting  https://instagram.frec8-1.fna.fbcdn.net/vp/7516e8820fa0f15b8729b6786ca5cb34/5BF2555D/t51.2885-15/sh0.08/e35/c0.134.1080.1080/s640x640/37758263_937718166430611_5531934614735552512_n.jpg
Saving in  /home/arthur/Desktop/beaches_n_resorts/37758263_937718166430611_5531934614735552512_n.jpg

Getting  https://instagram.frec8-1.fna.fbcdn.net/vp/a0e7d8993ff8fe568e4458facbe5e43f/5B769E41/t51.2885-15/e15/c0.80.640.640/38514049_198241864378191_6653922626710274048_n.jpg
Saving in  /home/arthur/Desktop/beaches_n_resorts/38514049_198241864378191_6653922626710274048_n.jpg
```


