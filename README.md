# Blocule
Develop blockchain applications for embedded devices.

## Video link
* https://www.youtube.com/watch?v=6e8vpMPB5Ks

## Hardware Requirements
* Raspberry Pi Zero W - https://www.raspberrypi.org/products/raspberry-pi-zero-w/ 
* Adafruit 128x64 OLED Bonnet - https://www.adafruit.com/product/3531
* 5V power supply or microUSB
* microSD card - 8,16 or 32 GB works

## OS
* Download raspbian - https://www.raspberrypi.org/downloads/raspbian/
* Install Guide for raspbian - https://www.raspberrypi.org/documentation/installation/installing-images/README.md
* Configure WiFi - https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md


## Install packages
* ``` sudo apt-get  update ```
* ``` sudo apt-get install -y git curl build-essential gcc g++ zlib1g-dev libconfig-dev bison wget net-tools openssh-server x11-apps autoconf automake libtool make unzip```
* ``` sudo apt-get install -y python3 python3-pip ```

## Install Java
* ``` echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | sudo tee /etc/apt/sources.list.d/webupd8team-java.list ```
* ``` echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | sudo tee -a /etc/apt/sources.list.d/webupd8team-java.list ```
* ``` sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 ```
* ``` sudo apt-get update; sudo apt-get install oracle-java8-installer ```

## Install Python packages for OLED Bonnet
* https://learn.adafruit.com/adafruit-128x64-oled-bonnet-for-raspberry-pi/usage


## Clone Blocule and Compile
* ``` cd ~/ ```
* ``` git clone https://github.com/sirishmk/blocule.git ```
* ``` cd blocule ```
* ``` make all ``` # This will take a while

## Quick way to generate a Wallet file
* Open the build.gradle in the trx-wallet folder and make the following changes
* Find ``` main = 'org.tron.emb.EmbClientApplication' ``` and Replace with ``` main = 'org.tron.walletcli.TestClient' ```
* Now import your wallet or create a new one. This will generate a ** Wallet ** file, save a copy of this. 


## Running the local wallet server
You may have to update the ~/blocule/trx-wallet/src/main/resources/config.conf with a valid node IP (https://github.com/tronprotocol/wallet-cli/blob/221a1673894e1fbc22c4f6f9ad78bae66a7d136d/src/test/resources/City.txt)
* Copy the ** Wallet ** file to ``` ~/blocule/trx-wallet/build/libs/ ```
* ``` cd ~/blocule/trx-wallet/build/libs/; java -jar  wallet-1.0-SNAPSHOT.jar ```

## Run the LCD wallet interface
* Open ``` ~/blocule/LCD/tron_trnx.py ``` and add the wallet address, wallet password and the toaddress (This will be replaced in the future)
* ``` cd ~/blocule/LCD; make run_disp ```

You can add the wallet server and the LCD interface script to your initialization.
Download more bitmap fonts from here - https://www.dafont.com/bitmap.php

## Known issues
* The send coin does not seem to work recently due to high bandwidth error.
* The wallet server is slow and a direct grpc python client is needed to speed up the server bootup.

DISCLAIMER: This project has nothing to do with my day job. This project was developed during my free time with my resources and is entirely free for use.
