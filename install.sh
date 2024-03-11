#!/bin/bash

apt update && apt upgrade -y

apt install python3 python3-pip -y

apt install python python-pip -y

apt install python-numpy python-pillow -y

source env/Scripts/activate

python -m venv env && source env/Scripts/activate

pip install -r windows.txt
    	
pip install numpy pillow
pip install --upgrade -r windows.txt
pip install --upgrade  numpy pillow
         


python manage.py runserver

set -e
UNAME=$(uname)


if command -v python3 or python &>/dev/null or "$OSTYPE" == "linux-gnu"*; then
    PYTHON=python3
    pip install numpy pillow
    pip install --upgrade -r linux.txt
    pip install --upgrade  numpy pillow
		
    python3 manage.py runserver


    PYTHON=python
    python manage.py runserver
fi

