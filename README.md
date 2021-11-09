## Vat Scraper UpWORK

Dependencies:
- Python 3.7
- PIP
- virtualenv

### Install dependencies:

```cmd
pip install virtualenv
virtualenv venv
.\env\Scripts\activate
pip install -r .\requirements.txt
playwright install
```

### Run Script:

```cmd
.\env\Scripts\activate
python .\main.py
```

### Description:

- The script open a navigator on headless mode and start the scraping for every line of the file `vat.txt`
- All responses of the web are stored on the file `output_%Y_%m_%d_%H_%M.csv`, every run of the script 
generate a new file with the same pattern name.




