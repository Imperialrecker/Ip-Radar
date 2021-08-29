# Ip-Radar

<h1 align="center">
  <br>
  <a href="https://github.com/Imperialrecker/Ip-Radar"><img src="https://github.com/Imperialrecker/Ip-Radar/blob/main/Ip-Radar/icon.png" alt="Ip-Radar icon"></a>

</h1>

<h4 align="center">A tool with attractive capabilities</h4>

<p align="center">
  <a href="http://python.org">
    <img src="https://img.shields.io/badge/License-CC0 1.0-blueviolet">
  </a>
  
  <a href="http://python.org">
    <img src="https://img.shields.io/badge/Python-v3-blue">
  </a>
  
  <a href="https://www.linux.org/">
    <img src="https://img.shields.io/badge/Platform-Linux-orange">
  </a>
  
<a href="https://www.microsoft.com/en-us/windows/">
    <img src="https://img.shields.io/badge/Platrform-Windows-brightgreen">
  </a>
  
<a href="https://www.apple.com/">
    <img src="https://img.shields.io/badge/Platrform-MacOs-critical">
  </a>
</p>

![demo](https://github.com/Imperialrecker/Ip-Radar/blob/main/Ip-Radar/images/Working%20screen.png)

Python based IPv4 information collector with location in Google Maps.

### Features:

- Get City Info of IPv4
- Get Region Info of IPv4
- Get Country Info of IPv4
- Get Latitude Info of IPv4
- Get Longitude Info of IPv4
- Get Direct Google Maps Link

### Operating Systems Tested

- Twister OS (Armbian based)
- MacOS (Big Sur V11.4)
- Windows (7)

### Installation On Linux

Please install neofetch module using appropriate installation method from <a href="https://github.com/dylanaraps/neofetch/wiki/Installation#">here</a>. Then follow the command line instructions (prior to this please have python3 and pip installed):

```bash
$ git clone https://github.com/Imperialrecker/Ip-Radar.git
$ sudo pip3 install ip2geotools
$ cd Ip-Radar
$ sudo python3 IP-Radar.py
```

### Installation On MacOs

1. We need to install Homebrew first prior to install neofetch module as follows (If you have Homebrew installed you can skip this step):

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Now we install the neofetch module:

```bash
$ brew install neofetch
```
3. Now we install ip2geotools library used in the python script:

```bash
$ sudo pip3 install ip2geotools
```

```bash
$ git clone https://github.com/Imperialrecker/Ip-Radar.git
$ sudo pip3 install ip2geotools
$ cd Ip-Radar
$ sudo python3 IP-Radar.py
```
