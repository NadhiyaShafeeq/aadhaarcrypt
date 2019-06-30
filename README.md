[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)<br />
**:purple_heart: Open Source**

<h1 align="center">AadhaarCrypt<sub style="color:red">BETA</sub></h1>
<p align="center"><img src="https://i.imgur.com/8MdzlBl.png" /></p>

> **AadhaarCrypt** because most of the developers do not even bother encrypting our sensitive information online. :rage:

AadhaarCrypt is an API which let users store [Aadhaar Card](https://uidai.gov.in/) information online in secure way. Aadhaar Crypt encrypts the aadhaar card data using a private key and returns the encrypted text back to the user which can be stored in place of the actual data in your online databases.

## Dependencies

* `Flask` `Flask cors` `pycrypto`

## Why use AadhaarCrypt?

Aadhaar card data is one of the most sensitive piece of information for every citizen of India and there are multiple websites and organisations which takes Aadhaar card number for identification purposes and store them in their online databases, there were incidents in past where aadhaar data was leaked because of vulnerable web applications.

* [Indian state government leaks thousands of Aadhaar numbers](https://techcrunch.com/2019/01/31/aadhaar-data-leak/)
* [Indane leaked millions of Aadhaar numbers: French security researcher](https://economictimes.indiatimes.com/news/politics-and-nation/indane-leaked-millions-of-aadhaar-numbers-french-security-researcher/articleshow/68058639.cms)

## Installation

1. Clone the repository

```
git clone https://github.com/shibli2700/aadhaarcrypt.git
```

2. run the follwing commands on your command line to install the dependencies.

```
cd aadhaarcrypt
python setup.py install
```

3. Run the server
```
python app.py
```

## Usage

**Ajax code to generate private key**
```javascript
function gettoken(){

  var url =  "http://127.0.0.1:5000/generate-token" //you can add ur own host here
  params = "{'name' : 'dante', 'email' : 'foo@bar.com'}"; //data to send

  try{
    var xhttp = new XMLHttpRequest();
  }catch(e){
    console.log(e)
  }

  xhttp.open("POST", url);
  xhttp.send(params);
  xhttp.onreadystatechange = function(){
    if(this.status == 200 && this.readyState == 4){
      console.log(this.responseText);
    }
  }
}

gettoken();
```


1. **Generate a private key by making the following request**

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

```json
{"key": "749ffeed93790ce4720ac5d04d4bcb8d"}
```
2. **Encrypt the data by making the following request**

```
POST /encrypt-data HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Length: 131

{"key":"749ffeed93790ce4720ac5d04d4bcb8d", "aadhaarno":"23-456-123", "name":"Lucifer", "dob":"21-09-1997", "address":"Park Avenue"}
```
You will get the encrypted data in reponse

```json
{"encrypted_text": "d29a3eb24a553ebd399daae63bad9703432edc5abc1822efd0e2e1ff74ad15784c45f1e5474593c9b34672b7ddf6a11d86d7d55a951ff24a3bd7628c6e654bed27ab407fcd6120bdab55c82e2b93cc6eff980869c48833b9a599d8262795c29787846567c3d09ea220fb5492d5"}
```

3. **Decrypt the data using the following reponse**

```
POST /decrypt-data HTTP/1.1
Host: 127.0.0.1:5000
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Length: 271

{"key":"749ffeed93790ce4720ac5d04d4bcb8d", "data":"d29a3eb24a553ebd399daae63bad9703432edc5abc1822efd0e2e1ff74ad15784c45f1e5474593c9b34672b7ddf6a11d86d7d55a951ff24a3bd7628c6e654bed27ab407fcd6120bdab55c82e2b93cc6eff980869c48833b9a599d8262795c29787846567c3d09ea220fb5492d5"}
```

You will get the decrypted json reponse

```json
{"decrypted_text": "\"aadhaarno\": \"23-456-123\", \"name\": \"Lucifer\", \"dob\": \"21-09-1997\", \"address\": \"Park Avenue\"}"}
```
## References
