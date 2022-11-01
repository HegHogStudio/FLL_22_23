#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Zentimeter pro Umdrehung: 17.9070781255

# Create your objects here.
ev3 = EV3Brick()
MotorLinks = Motor(Port.D)
MotorRechts = Motor(Port.C)
FarbMitte = ColorSensor(Port.S3)
FarbAussen = ColorSensor(Port.S1)
Gyro = GyroSensor(Port.S2)
MittelMotorLinks = Motor(Port.A)
MittelMotorRechts = Motor(Port.B)
Beruehrungssensor = TouchSensor(Port.S4)

# Funktionen
def FahreStrecke(pStrecke, pMaxgeschwindigkeit = 500, pBeschleunigungsfaktor = 1, pBremsfaktor = 1, pMingeschwindigkeit = 50, pPropFaktor = 1, pBenutzteHauptrichtung = 0, pRelativ = 0):
    Durchschnitt = 0
    MotorLinks.reset_angle(0)
    MotorRechts.reset_angle(0)

    while(Durchschnitt < pStrecke):
        Abweichung = AbweichungZurHauptrichtung(pBenutzteHauptrichtung) - pRelativ
        Durchschnitt = (MotorLinks.angle() + MotorRechts.angle()) / 2

        MotorLinks.run(max(pMingeschwindigkeit, min(pMaxgeschwindigkeit, min(Durchschnitt*pBeschleunigungsfaktor, (pStrecke-Durchschnitt)*pBremsfaktor))) + Abweichung*pPropFaktor)
        MotorRechts.run(max(pMingeschwindigkeit, min(pMaxgeschwindigkeit, min(Durchschnitt*pBeschleunigungsfaktor, (pStrecke-Durchschnitt)*pBremsfaktor))) + Abweichung*pPropFaktor)
        MotorLinks.brake()
        MotorRechts.brake()


# Write your program here.

# Fernsehen
FahreStrecke(677)