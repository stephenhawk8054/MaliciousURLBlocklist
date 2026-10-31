# MaliciousURLBlocklist
Fork of "Online Malicious URL Blocklist" by URLHaus

## Links for adding to uBlock Origin

```yml
https://cdn.jsdelivr.net/gh/stephenhawk8054/MaliciousURLBlocklist@latest/filters.txt
```

## Some modifications comparing to original sources:

- Plain domain filters are in the form of 

```adb
||example.com^
```

- Path-based filters are in the form of 

```adb
||example.com/path^$document,xmlhttprequest
```

- Since there are too many github-related filters, these will be combined to block different paths inside the repo in the form of 

```adb
||com/username/repo/*.$document,xmlhttprequest,to=github.com|raw.githubusercontent.com
```
and will not be available on mobile platforms.

## How to use

- To fetch the source and update the filters, run

```
python main.py
```

## About
[GPLv3 License](https://github.com/stephenhawk8054/MaliciousURLBlocklist/blob/main/LICENSE)
