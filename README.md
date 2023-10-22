## Description

This Python script aims to enhance your online privacy and security by automatically rotating your DNS settings at a set interval (default is every 5 minutes). The script uses a pre-defined list of reputable DNS servers. The full article explaining the importance of DNS in ethical hacking can be found at [HackingPassion.com](https://hackingpassion.com/why-your-dns-settings-could-make-or-break-your-hacking-career/).

## Why is this Important?
Understanding and tweaking your DNS settings is crucial in the realm of ethical hacking. For a detailed guide on why DNS settings are so important, check out this comprehensive article on [HackingPassion.com](https://hackingpassion.com/why-your-dns-settings-could-make-or-break-your-hacking-career/).

![DNS Changer Eye](logo-dns-changer-eye.png)

## Features

- Automatically rotates DNS settings
- Utilizes a list of 64 reputable DNS servers
- Enhances online privacy and security

## Requirements

- Python 3.x
- Linux OS (specifically designed for Parrot OS)

## Usage

Clone the Repository: Clone this repository to your local machine.
Run the Script: Navigate to the directory and execute python3 DNS_Rotator.py.
Manual Verification: Open a new terminal and run cat `/etc/resolv.conf` to check the current DNS settings.
Monitoring: Use network monitoring tools like Wireshark to confirm DNS queries are being sent to the correct servers.

1. Clone the repository
2. Navigate to the script's directory
3. Run `python3 dns_rotator.py`

## List of DNS Servers

The script includes the following DNS servers:

- Cloudflare: 1.1.1.1, 1.0.0.1
- Quad9: 9.9.9.9, 149.112.112.112
- OpenDNS: 208.67.222.222, 208.67.220.220
- Verisign: 64.6.64.6, 64.6.65.6
- UncensoredDNS: 91.239.100.100, 89.233.43.71
- CleanBrowsing: 185.228.168.9, 185.228.169.9
- Yandex: 77.88.8.8, 77.88.8.1
- AdGuard: 176.103.130.130, 176.103.130.131
- DNS Advantage: 156.154.70.1, 156.154.71.1
- Norton: 199.85.126.10, 199.85.127.10
- GreenTeam: 81.218.119.11, 209.88.198.133
- SafeDNS: 195.46.39.39, 195.46.39.40
- SmartViper: 208.76.50.50, 208.76.51.51
- Dyn: 216.146.35.35, 216.146.36.36
- FreeDNS: 37.235.1.174, 37.235.1.177
- Alternate DNS: 198.101.242.72, 23.253.163.53
- puntCAT: 109.69.8.51
- Quad101: 101.101.101.101, 101.102.103.104
- FDN: "80.67.169.12", "80.67.169.40"
- OpenNIC: "185.121.177.177", "185.121.177.53"
- AS250.net: "195.10.46.179", "212.82.225.7"
- Orange: "194.168.4.100", "194.168.8.100"
- SingNet: "203.122.222.6", "203.122.223.6"
- Level3: "209.244.0.3", "209.244.0.4"
- Belgian ISP Telenet: "109.88.203.3", "62.197.111.140"
- Sprintlink: "194.38.104.56", "194.38.105.56"
- Vodafone NZ: "203.118.141.194", "203.118.141.195"
- Vodafone NZ 2: "203.79.252.114", "203.79.252.115"

## Disclaimer

This script is for educational purposes only. Use it responsibly and ensure you have permission to change DNS settings on the network you're operating on.
