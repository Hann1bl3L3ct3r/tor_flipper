import argparse
import time
import requests
from stem.control import Controller
from stem import Signal

def get_current_ip(proxy_address="socks5h://127.0.0.1:9050"):
    try:
        response = requests.get("http://icanhazip.com", proxies={"http": proxy_address, "https": proxy_address}, timeout=10)
        return response.text.strip()
    except requests.RequestException as e:
        return f"[!] Failed to fetch IP: {e}"

def main():
    parser = argparse.ArgumentParser(description="Tor exit node rotator with IP verification")
    parser.add_argument("-s", "--seconds", type=int, required=True,
                        help="Interval in seconds to rotate Tor exit node")
    parser.add_argument("-p", "--port", type=int, default=9051,
                        help="Tor control port (default: 9051)")
    parser.add_argument("--password", type=str, required=True,
                        help="Password for Tor control port authentication")
    parser.add_argument("--proxy", type=str, default="socks5h://127.0.0.1:9050",
                        help="SOCKS5 proxy address for Tor (default: socks5h://127.0.0.1:9050)")

    args = parser.parse_args()

    with Controller.from_port(port=args.port) as control:
        control.authenticate(password=args.password)
        print(f"[+] Authenticated to Tor control port on port {args.port}")

        while True:
            control.signal(Signal.NEWNYM)
            print("[+] Sent NEWNYM signal to rotate Tor circuit.")
            time.sleep(5)  # brief delay to allow circuit rebuild before checking IP

            new_ip = get_current_ip(proxy_address=args.proxy)
            print(f"[+] Current Tor exit IP: {new_ip}")
            print(f"[i] Waiting {args.seconds} seconds before next rotation...\n")
            time.sleep(args.seconds)

if __name__ == "__main__":
    main()
