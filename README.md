# Blacksearch

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

#### Perform a normal google search in your terminal
```python
python blackbird.py --google -q <query>
```
Optional Arguments:
```python
-r <max-results>    #The maximum amount of results to display
-s <site>   #Only search on a specific website
-t <filetype>    #Only search for a specific file type
```

#### Perform an IP-Search
```python
python blackbird.py --ip -q <ip-adress>
```
Optional Arguments:
```python
none
```