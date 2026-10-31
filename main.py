import urllib.error
import urllib.request

from utils import write_text


def main():
    fetch = input('\nFetch source? (y/n)\n>>> ').lower()

    if fetch in ('y', 'yes'):
        req = urllib.request.Request('https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-online.txt', method='GET')
        try:
            with urllib.request.urlopen(req) as resp:
                data: bytes = resp.read()
                if not resp.status == 200:
                    print(resp.status)
                    return
                write_text(data.decode().strip(), 'source.txt')
        except urllib.error.URLError as e:
            print(e)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()