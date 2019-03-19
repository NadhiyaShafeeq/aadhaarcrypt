[![author](https://img.shields.io/badge/Author-PsychoCoder-red.svg)](https://twitter.com/PsychoCodes)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-green.svg)](https://www.python.org/)

# AadhaarCrypt

>**:purple_heart: Open Source**

AadhaarCrypt is an API which let users store [Aadhaar Card](https://uidai.gov.in/) information online and offline in a more secure way. Aadhaar Crypt encrypts the aadhaar card data using a private key and returns the encrypted text back to the user which can be stored in place of the actual data in your online databases.

![banner](https://i.imgur.com/zjeu2EM.png)

## Why use AadhaarCrypt

Aadhaar card data is one of the most sensitive piece of information for every citizen of India and there are multiple websites and organisations which takes Aadhaar card number for identification purposes and store them in their online databases, there were incidents in past where aadhaar data was leaked because of vulnerable web applications.

* [Indian state government leaks thousands of Aadhaar numbers](https://techcrunch.com/2019/01/31/aadhaar-data-leak/)
* [Indane leaked millions of Aadhaar numbers: French security researcher](https://economictimes.indiatimes.com/news/politics-and-nation/indane-leaked-millions-of-aadhaar-numbers-french-security-researcher/articleshow/68058639.cms)


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
