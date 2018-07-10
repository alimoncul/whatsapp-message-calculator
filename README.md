# whatsapp-message-calculator
## What is this script for?
This script designed to calculate message counts from whatsapp backup text file.

## What do i need for this script?
**1.** You need python and you can download from here: https://www.python.org/downloads/

**2.** You need to export your Whatsapp Chat.  
## How can i export my Whatsapp Chat on Android?
**1.** Enter your chat that you want to export, this can be group or person.

**2.** Click the 3 dot on the right top corner and select other.

**3.** Select "Export this conversation".

**4.** Select without media and send it to your email.

## How can i export my Whatsapp Chat on iOS?
**1.** Enter your chat that you want to export, this can be group or person.

**2.** Click the group name on the top.

**3.** Go to bottom and select "Export this conversation".

**4.** Select without media and send it to your email.
## How can i run this script?
```python
f = open('CHANGE HERE.txt', 'r+', encoding='utf-8')
```
Find this line on script(line 42) and change the "CHANGE HERE" to your whatsapp export file name. After that you can run this script with python and results.txt will be created. Bugs can be occured, please report if so.
