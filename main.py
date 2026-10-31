from datetime import datetime, timezone
import re
import urllib.error
import urllib.request

from utils import write_text


def main():
    fetch = input('\nFetch source? (y/n)\n>>> ').lower()
    dt_now = datetime.now(timezone.utc)
    dt = dt_now.isoformat(timespec='milliseconds')

    # Source list
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
            return

    with (
        open('domain.txt', 'w', encoding='utf-8') as f_domain,
        open('github.txt', 'w', encoding='utf-8') as f_github,
        open('non-github.txt', 'w', encoding='utf-8') as f_nongit
    ):
        with open('source.txt', 'r', encoding='utf-8') as f_source:
            # Combine multiple repo links to one
            repos = set()

            for line in f_source:
                raw_filter = line.strip().rstrip('^$all')

                if line.startswith('!'):
                    # Comment lines
                    continue
                elif '/' not in line:
                    # Plain domains
                    f_domain.write(f'||{raw_filter}^\n')
                elif '||github.com/' in line or '||raw.githubusercontent.com/' in line:
                    # Github-related filters
                    line_search = re.search(r'^\|\|(?:github\.com|raw\.githubusercontent\.com)\/([^\/]+\/[^\/]+)', raw_filter)
                    if not line_search:
                        continue
                    repo = line_search.group(1)
                    if repo in repos:
                        continue
                    repos.add(repo)
                    f_github.write(f'||com/{repo}/*.$document,xmlhttprequest,to=github.com|raw.githubusercontent.com\n')
                else:
                    # Other path-based domain
                    f_nongit.write(f'{raw_filter}^$document,xmlhttprequest\n')

    # Modify date time
    templates = """! Expires: 1 days
! Description: Fork of "Online Malicious URL Blocklist" by URLHaus
! Homepage: https://github.com/stephenhawk8054/MaliciousURLBlocklist
! License: https://github.com/stephenhawk8054/MaliciousURLBlocklist/blob/main/LICENSE
!
! GitHub issues: https://github.com/stephenhawk8054/MaliciousURLBlocklist/issues
! GitHub pull requests: https://github.com/stephenhawk8054/MaliciousURLBlocklist/pulls

! Domains
!#include domain.txt
! Non-github path-based
!#include non-github.txt
! Github path-based
!#if !env_mobile
!#include github.txt
!#endif

"""
    with open('filters.txt', 'w', encoding='utf-8') as fw:
        fw.write('! Title: Malicious URL Blocklist\n')
        fw.write(f'! Last modified: {dt}\n')
        fw.write(templates)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()