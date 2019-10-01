from NuovoLedControl import Nuovo7Segment
import dht
from machine import Pin

segment = Nuovo7Segment(Pin(5), Pin(18, Pin.OUT), Pin(19)) #Din Cs Clk
segment.setBrightness(8)
sensor = dht.DHT22(Pin(15))
def main():
    while True:
            try:
                sensor.measure()
                temp = float(sensor.temperature()) * 10
                humi = float(sensor.humidity()) * 10

                segment.setDigit(7, int(humi / 100), False)
                segment.setDigit(6, int((humi / 10) % 10), True)
                segment.setDigit(5, int(humi % 10), False)
                segment.setChar(4, 'h', False)

                segment.setDigit(3, int(temp/100), False)
                segment.setDigit(2, int((temp / 10)%10), True)
                segment.setDigit(1, int(temp%10) ,False)
                segment.setChar(0, 'c', False)
            except OSError as e:
                print('Failed to read sensor.')
main()
