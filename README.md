## pidoor
Simple door access management via Belgian Indentity card on RaspberryPi


### Pyscard installation

    sudo apt-get -y update && sudo apt-get -y upgrade
    sudo apt-get -y install swig libpcsclite-dev libacr38u python3-setuptools build-essential python3-pip git
    git clone https://github.com/LudovicRousseau/pyscard.git
    cd pyscard
    sudo python3 setup.py build_ext install
    cd ..
    sudo rm -fr pyscard

### Django installation

    sudo pip3 install django

### Django configuration

    cd
    git clone https://github.com/Lapin-Blanc/pidoor.git
    cd pidoor
    python3 cardsite/manage.py makemigrations
    python3 cardsite/manage.py migrate
    python3 cardsite/manage.py createsuperuser

### Testing

    python3 cardsite/manage.py runserver 0.0.0.0:8000 &
    ./pidoor.py

Access management site at http://raspberry_ip:8000/admin/ via Firefox or IE (java needed, so, no Chrome...)
from a computer with a Beid reader.

Encode some users and grant them access or not, then try the cards into the RPi's reader
