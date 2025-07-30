from machine import Pin
from utime import sleep

print("Hello world!")

vermelho = Pin(15, Pin.OUT)
amarelo = Pin(16, Pin.OUT)
verde = Pin(17, Pin.OUT)

while True:
    verde.on()
    print("LED VERDE LIGADO!")
    sleep(20)
    verde.off()
    print("LED VERDE DESLIGADO!")

    sleep(0.5)

    amarelo.on()
    print("LED AMARELO LIGADO!")
    sleep(10)
    amarelo.off()
    print("LED AMARELO DESLIGADO!")

    sleep(0.5)

    vermelho.on()
    print("LED VERMELHO LIGADO!")
    sleep(7)
    vermelho.off()
    print("LED VERMELHO DESLIGADO!")

    sleep(0.5)