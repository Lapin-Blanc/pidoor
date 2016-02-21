## pidoor
Simple door access management via Belgian Indentity card on RaspberryPi

### Installation

    sudo apt-get -y update && sudo apt-get -y upgrade

### installation pyscard...

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
    python3 cardsite/manage.py runserver 0.0.0.0:8000 &

