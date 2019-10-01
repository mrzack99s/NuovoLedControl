## NuovoLedControl for Micropython
NuovoLedControl 7 segment 8 digits (MAX7219) Micropython for ESP32 & ESP8266

>	© Copyright 2019 Nuovo, TD. <br>
>	Author Chatdanai Phakaket <br>
>	email zchatdanai@gmail.com or nuovo.td@gmail.com <br>
	
 ___
 
 
 **=== How to use setter?  ===**
 - Set string 8 digits <br>(Can use this case. If length of string equal 8 only!)
    ```
    setString
   ```
  - Set digit (digit,integer,dot) ;; dot is boolean. 
  <br>It's mean True , False => Have dot , Don't have dot
    ```
    segment.setDigit(7, 9, False)
    ```
  - Set Character (digit,char,dot) ;; dot is boolean. 
  <br>It's mean True , False => Have dot , Don't have dot
    ```
    segment.setChar(7, 'h', False)
    ```    
 - Set Row (digit,binary)
    ```
    segment.setRow(7,0b11111111)
   ```
  - Clear display
    ```
    segment.clearDisplay()
    ```

 
 **=== How to initial setup?  ===**
 
 1. import library
 
    ```
    from NuovoLedControl import Nuovo7Segment
    ```
 2. Call constructor with DIN , CS , CLK pin. For initial setup pin
 
    ```
    segment = Nuovo7Segment(Pin(5), Pin(18, Pin.OUT), Pin(19))
    ```
 3. Set brightness from 0 - 15 only!
 
    ```
    segment.setBrightness(8)
    ```
    Then, You're finish initial setup