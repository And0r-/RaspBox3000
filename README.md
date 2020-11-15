# RaspBox3000


WoW do not allow key broadcasting for multiboxer.
So any key pressed from the keyboard has to go directli to WoW.

My solution is to use a Raspberry pi3 with a keyboard and multiple raspberry zero as a HID.
So i can send the pressed key to all different computers or use a more save 1-1-1 mode.(comming soon)
(1-1-1 = 1 input causes only 1 action in only 1 client)

1-1-1 will be a round robin mode, so first time you press e.g. "2" it will be only send to the first computer. 
next time it will send it to the second, e.t.c

so when you have 5 chars you can not only press 1 time "2" to cast e.g. frostbold on all chars. you have to spam "2" minimum 5 times.
This will be a lot faster then alt-tab between all chars.

Known Issus:
A lot :D
This is only a first prototype to check is it possible.
I do not think I have enought time to make this usable for all
At the moment there the possible keys are very limitted.
modifire keys will be ignored. (upper "A" will only be a "a")
space, tab, etc. do not work
Keys will be released imidiatly on the HID keyboard. so it can be detected easy as a fake input.

I do not use it on WoW I only test it with multiple text editors on multiple Computers (mac and windows)

Setup:
On the Raspberry pi zeros I use Raspbian and it will boot as a HID device.
like this: https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/
but you have do it a littlebit different so:
/dev/hidg0 is mouse (not suported at the moment)
/dev/hidg1 is keyboard

you can check is it working when you can run  the RPi_Keyboard_Example.py script and write some example keys.


Then you need any Raspbery 3/4 as server with a keyboard.
This will use Server/SendKeys.py
On this scrippt you have to replaice the ip's from the raspbery zeros, at the moment.
Then you can run it.

The setup is not so easy. but wen the interest is big, I will create a image. to make it a lot more easy to use it.
