import shutil, smtplib, datetime, socket
from email.mime.text import MIMEText


path = ['/','/bkp','/home',]
gb = 1024 ** 3
limit = 10   #in Gigabyts
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
send=False

def main():
    txt1 = f'Serjik\'s Disk Usage Monitoring with Python.\nServer name: {socket.gethostname()}\n---------------------------------------\n\n'
    txt2 = ''
    txt3 = ''
    for p in path:  
        try:
            total = round(shutil.disk_usage(p).total/gb,1)
            used = round(shutil.disk_usage(p).used/gb,1)
            free = round(shutil.disk_usage(p).free/gb,1)
            # print(f'Disk usage statistics: {p}')
            usedPerc = round(100*used/total)
            # txt2 = txt2 + f' Total: {round(total/gb,1)}GB, Used: {round(used/gb,1)}GB, Free: {round(free/gb,1)}GB ---> {p} \n\n'
            txt2 = txt2 + f' [ {p} ]   {used} of {total} GB Used  -  Free: {free} GB  \n\n'
            # print(f'About {usedPerc}% is used\n')
            if usedPerc > limit:
                txt3 = txt3 + f' *** Warning {p} is used over {limit}%.  ({free} GB available)\n'
                send=True

        except:
            print(f'   *** {p} not found')
        finally:
            pass
    print(txt1 + txt2 +'\n---------------------------------------\n' + txt3)

def sendEmail(msg):
    sender_email = 'your@gmail.com'
    sender_password = 'app_password'
    receiver_email = 'email@domain.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 

    message = MIMEText(msg)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Server storage warning'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        server.quit()

if __name__ == '__main__':
    main()
