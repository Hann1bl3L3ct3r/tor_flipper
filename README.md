# tor_flipper
Python based command line utility to automatically change TOR exit nodes on a set time. 

Can be used for password sprays, DoS/DDoS attacks, and general anonymity. 
Must ensure control port is enabled. Can be used with and without password authentication. 

```
python tor_flipper.py -h
usage: tor_flipper.py [-h] -s SECONDS [-p PORT] --password PASSWORD [--proxy PROXY]

Tor exit node rotator with IP verification

options:
  -h, --help            show this help message and exit
  -s, --seconds SECONDS
                        Interval in seconds to rotate Tor exit node
  -p, --port PORT       Tor control port (default: 9051)
  --password PASSWORD   Password for Tor control port authentication
  --proxy PROXY         SOCKS5 proxy address for Tor (default: socks5h://127.0.0.1:9050)
```

```
python tor_flipper.py -s 30 -p 9051 --password '' 
[+] Authenticated to Tor control port on port 9051
[+] Sent NEWNYM signal to rotate Tor circuit.
[+] Current Tor exit IP: 185.220.101.20
[i] Waiting 30 seconds before next rotation...

[+] Sent NEWNYM signal to rotate Tor circuit.
[+] Current Tor exit IP: 109.70.100.5
[i] Waiting 30 seconds before next rotation...

[+] Sent NEWNYM signal to rotate Tor circuit.
[+] Current Tor exit IP: 2.58.56.93
[i] Waiting 30 seconds before next rotation...

[+] Sent NEWNYM signal to rotate Tor circuit.
[+] Current Tor exit IP: 192.42.116.192
[i] Waiting 30 seconds before next rotation...

```
