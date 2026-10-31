# MaliciousURLBlocklist
Fork of "Online Malicious URL Blocklist" by URLHaus

## Links for adding to uBlock Origin

```yml
Later
```

## Some modifications comparing to original sources:

- Plain domain filters are in form of 

```adb
||example.com^
```

- Path-based filters are in form of 

```adb
||example.com/path^$document,xmlhttprequest
```

- Since there are too many github-related filters, these are combined to block different paths inside the repo in the form of 

```adb
/username/repo/*.$document,xmlhttprequest
```
and will not be available on mobile platforms.

## How to use

- To fetch the source and update the filters, run

```
python main.py
```

## About
[GPLv3 License](https://github.com/stephenhawk8054/MaliciousURLBlocklist/blob/main/LICENSE)
