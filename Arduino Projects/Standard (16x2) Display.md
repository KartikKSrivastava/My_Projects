# Standard 16x2 Display

A register select (RS) pin that controls where in the LCD's memory you're writing data to.
A Read/Write (R/W) pin that selects reading mode or writing mode
An Enable pin that enables writing to the registers
8 data pins (D0 -D7). The states of these pins (high or low) are the bits that you're writing to a register when
you write, or the values you're reading when you read.
There's also a display constrast pin (Vo), power supply pins (+5V and Gnd) and LED Backlight (Bklt+ and
BKlt-) pins that you can use to power the LCD, control the display contrast, and turn on and off the LED
backlight, respectively.
The process of controlling the display involves putting the data that form the image of what you want to
display into the data registers, then putting instructions in the instruction register. The LiquidCrystal Library
simplifies this for you so you don't need to know the low-level instructions.

-----------------------------------------------------------------------------------------------------------------

# Functions Used from Arduino Library:

1. lcd.begin(cols, rows)
Action: Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display.
begin() needs to be called before any other LCD library commands.
lcd: a variable of type LiquidCrystal, cols: the number of columns that the display has, rows: the number of rows
that the display has
2. lcd.print(data)
Action: Used to print data on the display
3. lcd.setCursor(col,row)
Description: method to reposition the cursor
lcd.setCursor(0, 0); // top left
lcd.setCursor(15, 0); // top right
lcd.setCursor(0, 1); // bottom left
lcd.setCursor(15, 1); // bottom right
4. lcd.blink()
Description: Turn on the blinking cursor
5. lcd.noBlink()
Description: Turn off the blinking cursor
6. lcd.noCursor()
Description: Turn off cursor
7. lcd.cursor()
Description: Turn on cursor
8. lcd.scrollDisplayLeft()
Description: scroll one position left
9. lcd.scrollDisplayRight()
Description: scroll one position right
10. lcd.autoscroll()
Description: autoscroll() moves all the text one space to the left each time a letter is added
11. noAutoscroll()
Description: turns scrolling off
12. lcd.clear()
Description: Clears the LCD screen and positions the cursor in the upper-left corner.

--------------------------------------------------------------------------------------------------------

# Arduino Program

#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
void setup() {
 lcd.begin(16, 2);
 lcd.print("hello, world!");
}
void loop() {
 lcd.setCursor(0, 1);
 lcd.print(millis() / 1000);
}
