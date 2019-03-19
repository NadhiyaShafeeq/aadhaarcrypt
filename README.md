# AadhaarCrypt

AadhaarCrypt is an API which let users store Aadhaar information online and offline in a more safe way.

![banner](https://i.imgur.com/zjeu2EM.png)


## Usage

1. Generate a private key by making the following request

```
POST /generate-token HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Length: 41

{"name":"Dante", "email":"foo@bar.com"}
```

You will get the following reponse along with your private key

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 75
Access-Control-Allow-Origin: *
Server: Werkzeug/0.14.1 Python/3.6.3
Date: Tue, 19 Mar 2019 06:29:35 GMT

{"key": "40f7971420f16ecaf9926b181f475d6f1d903cd4e3eca8e35dab21d4160cdb12"}
```
