import tkinter as tk
import sqlite3
from datetime import datetime

# إنشاء قاعدة بيانات SQLite3
conn = sqlite3.connect('assistant.db')
c = conn.cursor()

# إنشاء جدول لتخزين سجلات المحادثات
c.execute('''CREATE TABLE IF NOT EXISTS conversations
             (id INTEGER PRIMARY KEY, timestamp TEXT, user_message TEXT, assistant_reply TEXT)''')

# إضافة دالة لإضافة سجل محادثة جديد إلى قاعدة البيانات
def add_conversation(user_message, assistant_reply):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO conversations (timestamp, user_message, assistant_reply) VALUES (?, ?, ?)", (timestamp, user_message, assistant_reply))
    conn.commit()

# دالة للرد على الاستفسارات
def respond():
    user_input = entry.get()
    reply = "مرحبًا! لقد قلت: " + user_input
    add_conversation(user_input, reply)
    text.insert(tk.END, "أنت: " + user_input + "\nالمساعد: " + reply + "\n\n")
    entry.delete(0, tk.END)

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("مساعد اصطناعي")

# إنشاء منطقة لعرض الردود
text = tk.Text(root)
text.pack()

# إنشاء مربع نص لإدخال الاستفسارات
entry = tk.Entry(root, width=50)
entry.pack()

# زر لإرسال الاستفسار
button = tk.Button(root, text="إرسال", command=respond)
button.pack()

# تشغيل النافذة
root.mainloop()

# إغلاق قاعدة البيانات عند إغلاق التطبيق
conn.close()