# JEE Main Marks Calculator (Python)
A program made in python to calculate marks obtained in NTA JEE Main (April 2019)

The NTA Website does not show the marks obtained in the exam. Only the percentiles and candidate responses are provided, from which interested candidates have to calculate their marks by referring to the answer key. It is complicated because the answer key only shows the question ID and correct option ID (WTF is wrong with them FFS). With this program, you can avoid manually calculating the marks. :P

Download built ZIP package containing EXE and answer key from [releases](https://github.com/blacklightpy/jee-main-results/releases)

# Usage

Run the EXE and input the URL of your JEE Main Responses (Can be found by logging in at the [JEE Main Website](https://jeemain.nic.in/JeeMainApp/Online/CandidateHome.aspx))

# Building from Source

## Install dependencies
`pip install bs4 requests pyinstaller`

## Run without compiling
`python main.py`

## Build command
`pyinstaller --onefile --icon=nta_logo.ico main.py`

Remember to keep key.txt in the working directory.
