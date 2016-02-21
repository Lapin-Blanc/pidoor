#!/usr/bin/env python3
import signal
import sys
from pprint import pprint
from time import sleep
import sqlite3

import Adafruit_CharLCD
from pythonbeid.beid import scan_readers, read_infos, triggered_decorator
from RPi import GPIO as gpio

RED_LED = 26
GREEN_LED = 27

# retrieve a list of available readers
r = scan_readers()[0]

@triggered_decorator
def card_insterted(action, card, reader=r.name):
    if action=="inserted":
        i = read_infos(card)
        pprint(i)
        cur = sqlite3.connect('cardsite/db.sqlite3').cursor()
        num_carte = i['num_carte']
        cur.execute("select prenoms, nom, acces_autorise, num_carte from djangobeid_personne where num_carte='%s';" % num_carte)
        res = cur.fetchall()
        cur.fetchall()
        cur.close()
        if not len(res)==1:
            print("Personne inconnue")
            gpio.output(RED_LED, True)
            gpio.output(GREEN_LED, False)
            lcd.clear()
            lcd.message("Unknown ID\nAccess denied...")
        else:
            prenom = res[0][0].split()[0]
            nom = res[0][1]
            acces = res[0][2]
            print(prenom, nom, acces, end=" : ")
            if acces == 1:
                print("Accès autorisé")
                gpio.output(RED_LED, False)
                gpio.output(GREEN_LED, True)
                lcd.clear()
                lcd.message(prenom + " " + nom + "\nAccess granted...")
            else:
                print("Accès interdit")
                gpio.output(RED_LED, True)
                gpio.output(GREEN_LED, False)
                lcd.clear()
                lcd.message(prenom + " " + nom + "\nAccess denied...")

@triggered_decorator
def card_removed(action, card, reader=r.name):
    if action=="removed":
        gpio.output(RED_LED, False)
        gpio.output(GREEN_LED, False)
        lcd.clear()
        lcd.message("System ready...\nInsert card")

if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    gpio.setup(RED_LED, gpio.OUT)
    gpio.setup(GREEN_LED, gpio.OUT)
    gpio.output(RED_LED, False)
    gpio.output(GREEN_LED, False)
    print("\nInsérez ou retirez une carte d'identité")
    print("---------------------------------------")
    print("")

    lcd = Adafruit_CharLCD.Adafruit_CharLCD()
    lcd.clear()
    lcd.message("System ready...\nInsert card")
    try:
        while True:
            pass 

    except KeyboardInterrupt:
        print("Fin du programme")
        lcd.clear()
        lcd.message("Shutting down...")
        gpio.cleanup()

