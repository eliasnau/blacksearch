<img alt="blackbird-logo" align="left" width="300" height="300" src="assets/img/BlackSearch.png">
<h1>Blacksearch</h1>

### An OSINT tool to search fast for Google in the Terminal, Get data from IP Adresses like Geolocation and Service Privider.
> BlackSearch is a powerful OSINT tool that provides IP address information, Google searches, website vulnerability analysis, data breach checks, and domain exploration. Use it responsibly and always seek permission before using it against others.

</br>

<img alt="blackbird-cli" align="center" src="assets/img/BlackSearchCLI.png">

## Disclaimer

This program is for educational purposes ONLY. Do not use it against individuals or systems without proper authorization and explicit permission. The author (eliasnau25) does not endorse any illegal or unethical activities with this software. Use it responsibly, respecting the privacy and rights of others. Any misuse or unauthorized use is strictly prohibited and may have legal consequences.

## Setup

#### Clone the repository
```shell
git clone https://github.com/eliasnau25/blacksearch
cd blackbird
```

#### Install requirements
```shell
pip install -r requirements.txt
```
## Usage

### Perform a normal google search in your terminal
```python
python blackbird.py --google -q <query>
```
Optional Arguments:
```python
-r <max-results>    #The maximum amount of results to display
-s <site>   #Only search on a specific website
-t <filetype>    #Only search for a specific file type
```
#### Example:

Input:
```python
python blacksearch.py --google -q "Python documentation" -r 10 -t "pdf"
```
Output:

```python
Searching for 'site:"python.org" Python documentation'...
========== Result #1 ==========
Title: Python Docs
Description: Python 3.11.4 documentation. Welcome! This is the official documentation for Python 3.11.4. Parts of the documentation: ...
URL: https://docs.python.org/ 

========== Result #2 ==========
Title: Our Documentation | Python.org
Description: Browse the docs online or download a copy of your own. Python's documentation, tutorials, and guides are constantly evolving. Get started here, or scroll ...
URL: https://www.python.org/doc/ 

========== Result #3 ==========
Title: The Python Tutorial — Python 3.11.4 documentation
Description: Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to ...
URL: https://docs.python.org/3/tutorial/index.html 

Search completed in 3.53 seconds. Found 3 results.
```

### Perform an IP-Search
```python
python blacksearch.py --ip -q <ip-adress> # You can provid an Ip-4 Ip-6 or a domain
```
Optional Arguments:
```python
none
```

#### Example:

Input:
```python

python blacksearch.py --ip -q "google.com"
```

Output:
```python
========== google.com ==========
Country: United Kingdom
Region: England
City: London
Lat: 51.5072, Lon: -0.127586
zip: W1B
Service Provider: Google LLC

Search completed in 0.33 seconds
```
### Perform an Domain Info Search
```python
python blacksearch.py --ip -q <domain> # You can provid an Ip-4 Ip-6 or a domain
```
Optional Arguments:
```python
none
```

#### Example:
Input
```python
python blacksearch.py --domain -q "google.com"
```
Output:
```python
WHOIS Data:
domain_name: ['GOOGLE.COM', 'google.com']
registrar: MarkMonitor, Inc.
whois_server: whois.markmonitor.com
referral_url: None
updated_date: [datetime.datetime(2019, 9, 9, 15, 39, 4), datetime.datetime(2019, 9, 9, 15, 39, 4, tzinfo=datetime.timezone.utc)]
creation_date: [datetime.datetime(1997, 9, 15, 4, 0), datetime.datetime(1997, 9, 15, 7, 0, tzinfo=datetime.timezone.utc)]
expiration_date: [datetime.datetime(2028, 9, 14, 4, 0), datetime.datetime(2028, 9, 13, 7, 0, tzinfo=datetime.timezone.utc)]
name_servers: ['NS1.GOOGLE.COM', 'NS2.GOOGLE.COM', 'NS3.GOOGLE.COM', 'NS4.GOOGLE.COM', 'ns3.google.com', 'ns4.google.com', 'ns1.google.com', 'ns2.google.com']
status: ['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited https://icann.org/epp#serverTransferProhibited', 'serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)']
emails: ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com']
dnssec: unsigned
name: None
org: Google LLC
address: None
city: None
state: CA
registrant_postal_code: None
country: US
DNS Records:
A: ['142.251.208.110']
AAAA: ['2a00:1450:400d:80e::200e']
MX: ['smtp.google.com.']
SSL Certificate Information:
subject: ((('commonName', '*.google.com'),),)
issuer: ((('countryName', 'US'),), (('organizationName', 'Google Trust Services LLC'),), (('commonName', 'GTS CA 1C3'),))
version: 3
serialNumber: 27D289988C526B9009B854630582BC06
notBefore: Jul 10 08:16:18 2023 GMT
notAfter: Oct  2 08:16:17 2023 GMT
subjectAltName: (('DNS', '*.google.com'), ('DNS', '*.appengine.google.com'), ('DNS', '*.bdn.dev'), ('DNS', '*.origin-test.bdn.dev'), ('DNS', '*.cloud.google.com'), ('DNS', '*.crowdsource.google.com'), ('DNS', '*.datacompute.google.com'), ('DNS', '*.google.ca'), ('DNS', '*.google.cl'), ('DNS', '*.google.co.in'), ('DNS', '*.google.co.jp'), ('DNS', '*.google.co.uk'), ('DNS', '*.google.com.ar'), ('DNS', '*.google.com.au'), ('DNS', '*.google.com.br'), ('DNS', '*.google.com.co'), ('DNS', '*.google.com.mx'), ('DNS', '*.google.com.tr'), ('DNS', '*.google.com.vn'), ('DNS', '*.google.de'), ('DNS', '*.google.es'), ('DNS', '*.google.fr'), ('DNS', '*.google.hu'), ('DNS', '*.google.it'), ('DNS', '*.google.nl'), ('DNS', '*.google.pl'), ('DNS', '*.google.pt'), ('DNS', '*.googleadapis.com'), ('DNS', '*.googleapis.cn'), ('DNS', '*.googlevideo.com'), ('DNS', '*.gstatic.cn'), ('DNS', '*.gstatic-cn.com'), ('DNS', 'googlecnapps.cn'), ('DNS', '*.googlecnapps.cn'), ('DNS', 'googleapps-cn.com'), ('DNS', '*.googleapps-cn.com'), ('DNS', 'gkecnapps.cn'), ('DNS', '*.gkecnapps.cn'), ('DNS', 'googledownloads.cn'), ('DNS', '*.googledownloads.cn'), ('DNS', 'recaptcha.net.cn'), ('DNS', '*.recaptcha.net.cn'), ('DNS', 'recaptcha-cn.net'), ('DNS', '*.recaptcha-cn.net'), ('DNS', 'widevine.cn'), ('DNS', '*.widevine.cn'), ('DNS', 'ampproject.org.cn'), ('DNS', '*.ampproject.org.cn'), ('DNS', 'ampproject.net.cn'), ('DNS', '*.ampproject.net.cn'), ('DNS', 'google-analytics-cn.com'), ('DNS', '*.google-analytics-cn.com'), ('DNS', 'googleadservices-cn.com'), ('DNS', '*.googleadservices-cn.com'), ('DNS', 'googlevads-cn.com'), ('DNS', '*.googlevads-cn.com'), ('DNS', 'googleapis-cn.com'), ('DNS', '*.googleapis-cn.com'), ('DNS', 'googleoptimize-cn.com'), ('DNS', '*.googleoptimize-cn.com'), ('DNS', 'doubleclick-cn.net'), ('DNS', '*.doubleclick-cn.net'), ('DNS', '*.fls.doubleclick-cn.net'), ('DNS', '*.g.doubleclick-cn.net'), ('DNS', 'doubleclick.cn'), ('DNS', '*.doubleclick.cn'), ('DNS', '*.fls.doubleclick.cn'), ('DNS', '*.g.doubleclick.cn'), ('DNS', 'dartsearch-cn.net'), ('DNS', '*.dartsearch-cn.net'), ('DNS', 'googletraveladservices-cn.com'), ('DNS', '*.googletraveladservices-cn.com'), ('DNS', 'googletagservices-cn.com'), ('DNS', '*.googletagservices-cn.com'), ('DNS', 'googletagmanager-cn.com'), ('DNS', '*.googletagmanager-cn.com'), ('DNS', 'googlesyndication-cn.com'), ('DNS', '*.googlesyndication-cn.com'), ('DNS', '*.safeframe.googlesyndication-cn.com'), ('DNS', 'app-measurement-cn.com'), ('DNS', '*.app-measurement-cn.com'), ('DNS', 'gvt1-cn.com'), ('DNS', '*.gvt1-cn.com'), ('DNS', 'gvt2-cn.com'), ('DNS', '*.gvt2-cn.com'), ('DNS', '2mdn-cn.net'), ('DNS', '*.2mdn-cn.net'), ('DNS', 'googleflights-cn.net'), ('DNS', '*.googleflights-cn.net'), ('DNS', 'admob-cn.com'), ('DNS', '*.admob-cn.com'), ('DNS', 'googlesandbox-cn.com'), ('DNS', '*.googlesandbox-cn.com'), ('DNS', '*.safenup.googlesandbox-cn.com'), ('DNS', '*.gstatic.com'), ('DNS', '*.metric.gstatic.com'), ('DNS', '*.gvt1.com'), ('DNS', '*.gcpcdn.gvt1.com'), ('DNS', '*.gvt2.com'), ('DNS', '*.gcp.gvt2.com'), ('DNS', '*.url.google.com'), ('DNS', '*.youtube-nocookie.com'), ('DNS', '*.ytimg.com'), ('DNS', 'android.com'), ('DNS', '*.android.com'), ('DNS', '*.flash.android.com'), ('DNS', 'g.cn'), ('DNS', '*.g.cn'), ('DNS', 'g.co'), ('DNS', '*.g.co'), ('DNS', 'goo.gl'), ('DNS', 'www.goo.gl'), ('DNS', 'google-analytics.com'), ('DNS', '*.google-analytics.com'), ('DNS', 'google.com'), ('DNS', 'googlecommerce.com'), ('DNS', '*.googlecommerce.com'), ('DNS', 'ggpht.cn'), ('DNS', '*.ggpht.cn'), ('DNS', 'urchin.com'), ('DNS', '*.urchin.com'), ('DNS', 'youtu.be'), ('DNS', 'youtube.com'), ('DNS', '*.youtube.com'), ('DNS', 'youtubeeducation.com'), ('DNS', '*.youtubeeducation.com'), ('DNS', 'youtubekids.com'), ('DNS', '*.youtubekids.com'), ('DNS', 'yt.be'), ('DNS', '*.yt.be'), ('DNS', 'android.clients.google.com'), ('DNS', 'developer.android.google.cn'), ('DNS', 'developers.android.google.cn'), ('DNS', 'source.android.google.cn'))
OCSP: ('http://ocsp.pki.goog/gts1c3',)
caIssuers: ('http://pki.goog/repo/certs/gts1c3.der',)
crlDistributionPoints: ('http://crls.pki.goog/gts1c3/zdATt0Ex_Fk.crl',)
Mentions on Websites:
https://accounts.google.com/ServiceLogin?hl=hr&continue=https://www.google.com/search?q%3Dgoogle.com&gae=cb-eomsrt
https://policies.google.com/technologies/cookies?hl=hr&utm_source=ucb
https://consent.google.com/dl?continue=https://www.google.com/search?q%3Dgoogle.com&gl=HR&hl=hr&cm=2&pc=srp&uxe=eomsrt&src=1
https://policies.google.com/privacy?hl=hr&utm_source=ucb
https://policies.google.com/terms?hl=hr&utm_source=ucb
```

#### More Features comming soon
