# KEYLOGGER_PROJECT
## WHAT IS KEYLOGGER? 
A keylogger is a type of software or hardware device that records every keystroke made on a keyboard. It can be used for legitimate purposes like monitoring employee productivity or tracking user activity on a computer. Still, it is also commonly used for malicious purposes such as stealing passwords, credit card numbers, and other sensitive information.
## Explain this project
here I got two files keylogger.py and server.py 
* file keylogger.py will be placed in the target machine
* file server.py will be placed on the server or the machine will receive information sent from the machine containing the keylogger
##### how it works
After running the keylogger.py file on the target computer, it will receive input from the keyboard and send it to the server (the server has run the py file first). After receiving the information, the terminal will receive and display it again. After shutting down the program, everything recorded will be written to the file.txt on the server
###### Step 1
* run file server.py on the server
* ![image](https://github.com/DOMBNC/DOM/assets/101182846/aa955fd8-fb78-4be8-b454-f9273d0eda80)
###### Step 2
* run file keylogger.py on the target computer
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/e1b3969b-2269-4feb-bd41-e6623da2cec5)
* the server will display "Accepted connection from ('192.168.1.2', 51839)"
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/d91bc9d7-3d56-4f2a-88f0-d407644346c4)
###### Step 3 
* Try entering the content using the keyboard into cmd. In this case, I try with test 01, test 02, test03
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/de0ff100-cc67-4ebd-a8ea-f51bfde3bca6)
* This is what we receive on the server
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/ca31bc60-9a2d-4cf5-84fa-e0ac0f711003)
###### Step 4
* Stop by typing exit
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/471b6af4-d246-4ca7-a62e-6fe823c2f809)
* On the server, it will automatically create a file named file.txt, it will contain the content of what the target computer has entered and be displayed on the terminal.
* ![image](https://github.com/DOMBNC/KEYLOGGER/assets/101182846/b63ff42e-0903-4d74-b9f7-a20a49c838f0)
# !!!Only used for learning ethical hacking!!!
