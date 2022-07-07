# Bitly url shorterer.

This project interacts with the site bit.ly for trimming links. Your link is sent to the input, and a shortened link like bit.ly/****** is output.

You can also submit an already shortened link to the input, then the output will have the number of clicks on this link.

## Launch.

Get a token to work with the API [bitly.com](https://app.bitly.com/settings/api/).

Added `'BITLY_TOKEN'` to `.env` file.

Run `main.py` with the optional parameter "url" as a link and get a bitlink.
If an optional parameter is Bitlink, the program will count the number of clicks on it.

Run 'main.py' without the optional parameter to enter links through ```input()```.

## How to install?

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```pip install -r requirements.txt```

Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for isolate the project

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org).
 
