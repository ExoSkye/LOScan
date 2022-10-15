# LOScan
The tools/commands I used to scan for LiveOverflow's Server

# Steps

## Step 1

Install `masscan`.

This step is distro specific but:

On debian derived systems you can run:
```
sudo apt install masscan
```
and on Arch derived distros you can run:
```
sudo pacman -Sy masscan
```

## Step 2

Run this command to find all minecraft servers running on Hetzner's Servers (sorry Hetzner for spamming your IP blocks)

```
sudo masscan -p25565 157.90.0.0/16 116.202.0.0/16 116.203.0.0/16 128.140.0.0/17 142.132.128.0/17 159.69.0.0/16 162.55.0.0/16 167.233.0.0/16 167.235.0.0/16  168.119.0.0/16  176.9.0.0/16 178.63.0.0/16 168.119.0.0/16  185.12.65.0/24 188.34.128.0/17 188.40.0.0/16 195.201.0.0/16 213.133.96.0/19 213.239.192.0/18 23.88.0.0/17 46.4.0.0/16 49.12.0.0/16 49.13.0.0/16 5.75.128.0/17 5.9.0.0/16 78.46.0.0/15 85.10.192.0/18 88.198.0.0/16 88.99.0.0/16 91.107.128.0/17 94.130.0.0/16 --excludefile exclude.conf | tee masscan.out
```

It is not neccesary to run this command to completion.

## Step 3

Install the python dependencies using this command (may require sudo):

```
pip3 install joblib mcstatus
```

## Step 4

Run `json_conv.py` in the same directory as where you run the masscan command.

## Step 5

Run `motd.py | grep -C 3 LiveOverflow` to find all IPs that have LiveOverflow in their MOTDs.

Sample output:
```
kai@muellerssoftwaredomain ~> python3 motd.py | grep -C 3 LiveOverflow
MOTD of IP: xxx.xxx.xxx.xxx
	"LiveOverflow Let's Play"
Timeout on xxx.xxx.xxx.xxx
MOTD of IP: xxx.xxx.xxx.xxx
	A Minecraft Server
 ```
 
 IPs censored for obvious reasons.
