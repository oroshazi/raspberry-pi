import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.HIGH)  # Set pin to high(+3.3V) to off the led

try:
    while True:
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...taa')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.7)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...taa')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.7)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...taa')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.7)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.2)
        print('...ti')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.3)
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.8)
# When 'Ctrl+C' is pressed, the flowing code will be  executed.
except KeyboardInterrupt:
    GPIO.output(LedPin, GPIO.HIGH)   # led off
    GPIO.cleanup()
