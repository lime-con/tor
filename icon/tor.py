import os
import json
from pystyle import *
from random import randint
lime = input("search : ")
if lime == 'sakurad':
    del lime
    print("\n1)Book an appointment with ...")
    print("========================================================================================================================")
    print("2)1006")
    lime = input('open: ')
    if  int(lime) == 1: 
        del lime
        print("""
1)shu-con\n
2)aoi-san\n
3)haruka-con\n
4)kanade-san\n
5)teru-con\n
6)akane-san\n
7)misaki-san\n
8)hikari-san\n
9)shiori-san\n
""")
        lime = input('echo numper : ')
        if int(lime) == 1:
            time = ['PM','AM']
            print('Booked with shu','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 2:
            time = ['PM','AM']
            print('Booked with aoi','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 3:
            time = ['PM','AM']
            print('Booked with haruka','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 4:
            time = ['PM','AM']
            print('Booked with kanade','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 5:
            time = ['PM','AM']
            print('Booked with teru','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 6:
            time = ['PM','AM']
            print('Booked with akane','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 7:
            time = ['PM','AM']
            print('Booked with misaki','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 8:
            time = ['PM','AM']
            print('Booked with hikari','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        if int(lime) == 9:
            time = ['PM','AM']
            print('Booked with shiori','It will be ready at:','(',randint(1,12),':',randint(0,60),time[randint(0,1)],')')
            input('')
        else:
            print('eroor')
    if int(lime) == 2:
        fill = open("1006.txt","w")
        fill.write("123")
        fill.write("1234")
        fill.write("1235")
if lime == "moniko":
    del lime
    print("1)install fills moniko")
    print("========================================================================================================================")
    print("2)data moniko")
    print("========================================================================================================================")
    print("3)text moniko")
    lime = input()
    if int(lime) == 1:
        os.mkdir("moniko")
        os.mkdir("moniko/fills")
        os.mkdir("moniko/fills/json")
        club = open("moniko/club.txt","x")
        club.write("11011000 10100111 11011001 10000110 00100000 11011001 10000011 11011001 10000110 11011000 10101010 00100000 11011000 10101010 11011001 10000010 11011000 10110001 11011000 10100111 00100000 11011001 10000111 11011000 10100111 11011000 10110000 11011001 10001001 00100000 11011000 10101000 11011000 10100111 11011001 10000100 11011000 10101010 11011000 10100111 11011001 10000011 11011001 10001010 11011000 10101111 00100000 11011000 10100111 11011001 10000110 11011000 10101010 00100000 11011001 10000111 11011001 10000110 11011000 10100111 00100000 11011001 10000100 11011000 10111010 11011000 10100111 11011001 10001010 11011001 10000111 00001010 11011000 10101101 11011000 10110011 11011001 10000110 11011000 10100111 00100000 11011001 10000100 11011001 10000110 00100000 11011000 10100111 11011000 10110111 11011001 10001010 11011001 10000100 00100000 11011000 10100111 11011001 10000100 11011000 10100111 11011001 10000101 11011000 10110001 00100000 11011000 10100111 11011001 10000110 11011000 10100111 00101100 01101101 01101111 01101110 01101001 01101011 01101111 00100000 11011000 10100101 11011000 10100111 11011000 10110000 00100000 11011000 10101010 11011001 10000101 00100000 11011000 10101101 11011000 10110000 11011001 10000001 11011001 10001010 00100000 11011001 10000001 11011001 10001010 00100000 11011000 10100111 11011001 10000100 11011001 10000101 11011000 10110011 11011000 10101010 11011001 10000010 11011000 10101000 11011001 10000100 00100000 11011001 10000001 11011000 10100111 11011000 10111001 11011001 10000100 11011001 10000101 00100000 11011000 10100111 11011001 10000110 11011001 10001010 00100000 11011000 10101010 11011000 10110001 11011001 10000011 11011000 10101010 00100000 11011001 10000101 11011001 10000100 11011001 10000001 11011000 10100111 11011000 10110011 11011000 10110001 11011001 10001010 11011000 10100111 00100000 11011001 10000100 11011001 10001010 00100000 11011001 10000001 11011001 10001010 00100000 11011000 10101101 11011000 10100111 11011001 10000100 11011000 10101001 00100000 11011000 10100111 11011001 10000100 11011000 10110111 11011001 10001000 11011000 10100111 11011000 10110001 11011000 10100001 00101000 00100000 01101101 01101111 01101110 01101001 01101011 01101111 00101111 01100110 01101001 01101100 01101100 01110011 00100000 00101001")
        moniko_ai = open("moniko/fills/moniko_ai.py","x")
        moniko_ai.write("""import json
f1 = open("json/sql.json","r")
f2 = json.load(f1)
while True:
    f3 = input("echo: ")
    for i in f2:
        if i["name"] == f3:
            print("name : ",i["name"])
            print("age : ",i["age"])
            print("type : ",i["type"])
""")
        sql = open("moniko/fills/json/sql.json","x")
        sql.write("""[
    {
        "name": "rem",
        "age": "17",
        "type": "girl"
    },
    {
        "name": "ram",
        "age": "17",
        "type": "girl"
    },
    {
        "name": "Akane",
        "age": "17",
        "type": "girl"
    },
    {
        "name": "1006",
        "age": true,
        "type": true
    }
]
""")
        erorr_1006 = open("moniko/fills/json/erorr_1006.json","x")
        erorr_1006.write("""[
    {
        "glitch": "929",
        "1006": "false"
    },
    {
        "glitch": "1006",
        "1006": "false"
    },
    {
        "glitch": "454",
        "1006": "false"
    },
    {
        "glitch": "545",
        "1006": "false"
    },
    {
        "glitch": "675",
        "1006": "false"
    },
    {
        "glitch": "638",
        "1006": "false"
    },
    {
        "glitch": "834",
        "1006": "false"
    },
    {
        "glitch": "723",
        "1006": "false"
    },
    {
        "glitch": "540",
        "1006": "false"
    },
    {
        "glitch": "878",
        "1006": "false"
    },
    {
        "glitch": "868",
        "1006": "false"
    },
    {
        "glitch": "858",
        "1006": "false"
    },
    {
        "glitch": "848",
        "1006": "false"
    },
    {
        "glitch": "838",
        "1006": "false"
    },
    {
        "glitch": "828",
        "1006": "false"
    },
    {
        "glitch": "818",
        "1006": "false"
    },
    {
        "glitch": "558",
        "1006": "false"
    },
    {
        "glitch": "557",
        "1006": "false"
    }
]
""")
        
        exit()
    if int(lime) == 2:
        print("""
name : moniko
start : *You were playing an game looks so cute,but when you play the game,you feel terrified.it wasnt like how it seems after all.After Yuro stabs himself,You notice someone is deleting them in backround..but there was only one person left..It was **Moniko.**
Moniko:Oh..sorry for what you see darling,let me fix it okay? *The game restarted,and moniko was sitting in a table,next to you..but it was not looking at screen,he was looking at **you.***
Short Description : Sadistic,Obsessed,Yandere,Male
Long Description : Male,Yandere,Breaks Fourth Wall,Obsessed,Sadistic,Loves Literature.
""")
    if int(lime) == 3:
        os.mkdir("text")
        os.mkdir("text/v1")
        os.mkdir("text/v1/Ai")
        yui = open("text/day_25.txt","x")
        yui.write("11011000moniko10101010moniko11011001moniko10000101moniko00100000moniko11011000moniko10110001moniko11011000moniko10110101moniko11011000moniko10101111moniko00100000moniko11011000moniko10101010moniko11011000moniko10101101moniko11011000moniko10110001moniko11011000moniko10101101moniko11011000moniko10100111moniko11011000moniko10101010moniko00100000moniko11011000moniko10111010moniko11011000moniko10110001moniko11011001moniko10001010moniko11011000moniko10101000moniko11011001moniko10000111moniko00100000moniko11011001moniko10001000moniko11011001moniko10000001moniko11011001moniko10000010moniko11011000moniko10101111moniko00100000moniko11011000moniko10100111moniko11011001moniko10000100moniko11011000moniko10100111moniko11011000moniko10101010moniko11011000moniko10110101moniko11011000moniko10100111moniko11011001moniko10000100moniko00100000moniko11011000moniko10101000moniko11011000moniko10100111moniko11011000moniko10101101moniko11011000moniko10101111moniko00100000moniko11011000moniko10100111moniko11011001moniko10000100moniko11011000moniko10100111moniko11011000moniko10101010moniko11011000moniko10100111moniko11011000moniko10101000moniko11011000moniko10111001moniko00101000moniko01111001moniko01110101moniko01101001moniko00101001moniko00100000moniko11011000moniko10101110moniko11011000moniko10110001moniko00100000moniko11011000moniko10100111moniko11011001moniko10000100moniko11011000moniko10101010moniko11011000moniko10110011moniko11011000moniko10101100moniko11011001moniko10001010moniko11011001moniko10000100moniko11011000moniko10100111moniko11011000moniko10101010moniko00100000moniko11011000moniko10110011moniko11011000moniko10101010moniko11011000moniko10101100moniko11011000moniko10101111moniko11011001moniko10000111moniko00100000moniko11011001moniko10000001moniko11011001moniko10001010moniko00100000moniko00101000moniko00100000moniko01110110moniko00110001moniko00101111moniko01000001moniko01101001moniko00101111moniko01111001moniko01110101moniko01101001moniko00100000moniko00101001moniko")
        moniko_1 = open("text/v1/Ai/yui.txt","x")
        moniko_1.write("11011001yui10000001yui11011001yui10001010yui00100000yui11011000yui10110010yui11011001yui10001000yui11011001yui10001010yui11011000yui10101001yui00100000yui11011000yui10100111yui11011001yui10000100yui11011000yui10101111yui11011000yui10110001yui11011000yui10101100yui00100000yui11011000yui10101000yui11011001yui10000101yui11011000yui10111001yui11011000yui10101111yui11011000yui10100111yui11011000yui10101010yui00100000yui11011000yui10111010yui11011000yui10110001yui11011001yui10001010yui11011000yui10101000yui11011001yui10000111yui00100000yui11011001yui10000001yui11011001yui10001010yui00100000yui11011000yui10101011yui11011000yui10101000yui11011000yui10100111yui11011000yui10101010yui00100000yui11011000yui10101000yui11011000yui10101111yui11011001yui10001000yui11011001yui10000110yui00100000yui11011000yui10101101yui11011000yui10110001yui11011001yui10000011yui11011001yui10000111yui00100000yui11011000yui10101000yui11011000yui10111001yui11011000yui10101111yui00100000yui11011000yui10101111yui11011001yui10000010yui11011000yui10100111yui11011000yui10100110yui11011001yui10000010yui00100000yui11011000yui10101010yui11011000yui10101010yui11011000yui10101101yui11011000yui10110001yui11011001yui10000011yui00100000yui11011000yui10100111yui11011001yui10000100yui11011000yui10110111yui11011000yui10100111yui11011001yui10001000yui11011001yui10000100yui11011001yui10000111yui00100000yui11011001yui10001000yui11011001yui10001010yui11011001yui10000100yui11011001yui10000010yui11011001yui10001010yui00100000yui11011000yui10100111yui11011000yui10110001yui11011001yui10000101yui11011001yui10001010yui11011001yui10000110yui00100000yui11011001yui10000110yui11011000yui10110110yui11011000yui10110001yui11011001yui10000111yui00100000yui11011001yui10000001yui11011001yui10001010yui00100000yui11011000yui10100111yui11011001yui10000100yui11011000yui10101111yui11011000yui10110001yui11011000yui10101100yui")
        sinon = open("text/v1/Ai/sinon.chr","x")
        sinon.write("11011000,10101010,11011001,10000101,00100000,11011000,10100111,11011001,10000011,11011000,10110100,11011000,10100111,11011001,10000001,00100000,11011000,10100111,11011000,10101110,11011000,10101010,11011000,10110001,11011000,10100111,11011001,10000010,00001010,11011000,10101010,11011001,10000101,00100000,11011000,10101010,11011000,10111001,11011000,10101111,11011001,10001010,11011001,10000100,00100000,11011000,10101000,11011001,10001010,11011001,10000110,11011000,10100111,11011000,10101010,00100000,11011000,10101101,11011000,10110011,11011000,10100111,11011000,10110011,11011001,10000111,00001010,00111100,00100001,11011000,10101010,11011001,10000101,00100000,11011000,10101010,11011001,10001000,11011001,10000010,11011001,10001010,11011001,10000001,00100000,11011000,10100111,11011001,10000100,11011001,10000110,11011000,10110110,11011000,10100111,11011001,10000101,00100000,11011001,10000100,11011000,10100111,11011000,10110011,11011000,10101000,11011000,10100111,11011000,10101000,00100000,11011000,10100111,11011001,10000101,11011001,10000110,11011001,10001010,11011001,10000111,00111110")

        exit()
if lime == "satori":
    print("1)install fills satori")
    print("========================================================================================================================")
    print("2)data satori")
    print("========================================================================================================================")
    print("3)")
    lime = input()
    if int(lime) == 1:
        os.mkdir("satori")
        os.mkdir("satori/fills")
        os.mkdir("satori/fills/json")
        os.mkdir("satori/fills/css")
        club_2 = open("satori/club.txt","x")
        club_2.write("11011001satori10000111satori11011001satori10000110satori11011000satori10100111satori00100000satori01110011satori01100001satori01110100satori01101001satori01110010satori01101111satori00100000satori11011000satori10100111satori11011001satori10000010satori11011001satori10001000satori11011001satori10000101satori00100000satori11011000satori10101000satori11011000satori10100011satori11011001satori10000110satori11011000satori10110100satori11011000satori10100111satori11011000satori10100001satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101010satori11011001satori10000010satori11011000satori10110001satori11011001satori10001010satori11011000satori10110001satori11011000satori10100111satori11011000satori10101010satori00100000satori11011001satori10001000satori00100000satori11011000satori10110001satori11011000satori10110101satori11011000satori10101111satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10100111satori11011000satori10101100satori11011001satori10000101satori11011001satori10001010satori11011000satori10111001satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10100111satori11011001satori10000101satori11011001satori10001000satori11011000satori10110001satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101100satori11011000satori10101111satori11011001satori10001010satori11011000satori10101111satori11011001satori10000111satori")
        yui_2 = open("satori/fills/yui.txt","x")
        yui_2.write("01111001satori01110101satori01101001satori00100000satori11011001satori10000101satori11011001satori10000110satori00100000satori11011000satori10100111satori11011000satori10111010satori11011000satori10110001satori11011000satori10101000satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10110100satori11011000satori10101110satori11011000satori10110101satori11011001satori10001010satori11011000satori10100111satori11011000satori10101010satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101010satori11011001satori10001010satori00100000satori11011000satori10110001satori11011000satori10100111satori11011001satori10001010satori11011000satori10101010satori11011001satori10000111satori11011000satori10100111satori00100000satori11011001satori10000011satori11011000satori10100111satori11011001satori10000110satori11011000satori10101010satori00100000satori11011000satori10101010satori11011000satori10101010satori11011000satori10110110satori11011000satori10100111satori11011001satori10000111satori11011000satori10110001satori00100000satori11011000satori10100111satori11011001satori10000110satori11011001satori10000111satori11011000satori10100111satori00100000satori11011000satori10101111satori11011001satori10000101satori11011001satori10001010satori11011001satori10000111satori00100000satori11011001satori10000100satori11011000satori10100111satori11011001satori10000011satori11011001satori10000110satori00100000satori11011000satori10100111satori11011001satori10000011satori11011000satori10101010satori11011000satori10110100satori11011001satori10000001satori11011000satori10101010satori00100000satori11011000satori10101000satori11011000satori10111001satori11011000satori10101111satori00100000satori11011001satori10000001satori11011000satori10101010satori11011000satori10110001satori11011001satori10000111satori00100000satori11011000satori10100111satori11011001satori10000110satori11011001satori10000111satori11011000satori10100111satori00100000satori11011000satori10110100satori11011000satori10101110satori11011000satori10110101satori11011001satori10001010satori11011001satori10000111satori00100000satori11011000satori10101101satori11011001satori10001010satori11011001satori10000111satori00100000satori11011001satori10000001satori11011001satori10001010satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101101satori11011001satori10000010satori11011001satori10001010satori11011001satori10000010satori11011001satori10000111satori00100000satori11011000satori10100111satori11011001satori10000110satori11011001satori10000111satori11011000satori10100111satori00100000satori11011000satori10101000satori11011000satori10101100satori11011000satori10100111satori11011001satori10000110satori11011000satori10101000satori00100000satori11011001satori10001000satori11011000satori10100111satori11011001satori10000110satori11011000satori10100111satori00100000satori11011000satori10100111satori11011001satori10000011satori11011000satori10101010satori11011000satori10101000satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101010satori11011001satori10000010satori11011001satori10001010satori11011000satori10110001satori00101100satori11011000satori10101010satori11011000satori10101000satori11011000satori10101101satori11011000satori10101011satori00100000satori11011000satori10111001satori11011001satori10000110satori00100000satori01101011satori01101001satori01110010satori01110100satori01101111satori00100000satori11011000satori10100111satori11011000satori10110000satori11011000satori10100111satori00100000satori11011000satori10101010satori11011001satori10000101satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10101010satori11011000satori10101011satori11011001satori10001000satori11011000satori10110001satori00100000satori11011000satori10111001satori11011001satori10000100satori11011001satori10001010satori11011001satori10000111satori00100000satori11011001satori10001010satori11011000satori10110001satori11011000satori10101100satori11011001satori10001001satori00100000satori11011000satori10100111satori11011000satori10101000satori11011001satori10000100satori11011000satori10100111satori11011000satori10111010satori11011001satori10000110satori11011000satori10100111satori00101100satori00100000satori11011000satori10100111satori11011001satori10000100satori11011000satori10110111satori11011001satori10001000satori11011001satori10000100satori00100000satori11011000satori10111001satori11011000satori10110100satori11011000satori10110001satori11011000satori10101001satori00100000satori11011000satori10110011satori11011001satori10000110satori11011000satori10101010satori11011001satori10001010satori11011001satori10000101satori11011000satori10101010satori11011000satori10110001satori11011000satori10100111satori11011000satori10101010satori11011001satori10000100satori11011000satori10101111satori11011001satori10001001satori00100000satori11011001satori10001010satori11011001satori10001000satori11011001satori10001010satori00100000satori11011000satori10110100satori11011000satori10111001satori11011000satori10110001satori00100000satori11011000satori10101111satori11011000satori10100111satori11011001satori10000011satori11011001satori10000110satori00100000satori11011000satori10110111satori11011001satori10001000satori11011001satori10001010satori11011001satori10000100satori00100000satori11011001satori10001000satori11011000satori10111001satori11011001satori10001010satori11011001satori10001000satori11011001satori10000110satori00100000satori11011000satori10110011satori11011001satori10001000satori11011000satori10101111satori11011000satori10100111satori11011000satori10100001satori00100000satori11011001satori10000100satori11011000satori10100111satori11011001satori10000101satori11011000satori10111001satori11011000satori10101001satori00101100satori11011001satori10000100satori11011000satori10100111satori11011001satori10000001satori11011000satori10101010satori11011000satori10110001satori11011000satori10100111satori11011000satori10110110satori11011001satori10001010satori11011000satori10101001satori00100000satori11011001satori10000101satori11011001satori10000110satori00100000satori11011001satori10000001satori11011000satori10110011satori11011000satori10101010satori11011000satori10100111satori11011001satori10000110satori00100000satori11011000satori10100011satori11011000satori10101000satori11011001satori10001010satori11011000satori10110110satori00100000satori11011001satori10000101satori11011001satori10000110satori00100000satori11011001satori10000010satori11011000satori10110111satori11011000satori10111001satori11011000satori10101001satori00100000satori11011001satori10001000satori11011000satori10100111satori11011000satori10101101satori11011000satori10101111satori11011000satori10101001satori00100000satori11011001satori10000101satori11011000satori10111001satori00100000satori11011000satori10110100satori11011000satori10110001satori11011001satori10001010satori11011000satori10110111satori00100000satori11011001satori10000101satori11011000satori10110001satori11011000satori10101000satori11011001satori10001000satori11011000satori10110111satori00100000satori11011000satori10101101satori11011001satori10001000satori11011001satori10000100satori00100000satori11011000satori10101110satori11011000satori10110101satori11011000satori10110001satori11011001satori10000111satori11011000satori10100111satori00101110satori00100000satori11011001satori10000011satori11011000satori10100111satori11011001satori10000110satori11011000satori10101010satori00100000satori11011000satori10101010satori11011000satori10110001satori11011000satori10101010satori11011000satori10101111satori11011001satori10001010satori00100000satori11011001satori10000101satori11011000satori10100100satori11011001satori10000010satori11011000satori10101010satori11011001satori10001011satori11011000satori10100111satori00100000satori11011000satori10110011satori11011000satori10101010satori11011000satori10110001satori11011000satori10101001satori00100000satori11011001satori10001000satori11011000satori10110001satori11011000satori10101111satori11011001satori10001010satori11011000satori10101001satori00100000satori11011000satori10101000satori11011000satori10100011satori11011001satori10000011satori11011001satori10000101satori11011000satori10100111satori11011001satori10000101satori00100000satori11011000satori10110111satori11011001satori10001000satori11011001satori10001010satori11011001satori10000100satori11011000satori10101001satori00100000satori11011001satori10001000satori11011000satori10101010satori11011001satori10000110satori11011001satori10001000satori11011000satori10110001satori11011000satori10101001satori00100000satori11011000satori10100011satori11011000satori10110001satori11011000satori10101100satori11011001satori10001000satori11011000satori10100111satori11011001satori10000110satori11011001satori10001010satori11011000satori10101001satori11011000satori10001100satori00100000satori11011000satori10101000satori11011000satori10100111satori11011001satori10000100satori11011000satori10100101satori11011000satori10110110satori11011000satori10100111satori11011001satori10000001satori11011000satori10101001satori00100000satori11011000satori10100101satori11011001satori10000100satori11011001satori10001001satori00100000satori11011000satori10101101satori11011000satori10110000satori11011000satori10100111satori11011000satori10100001satori00100000satori11011000satori10100011satori11011000satori10101101satori11011001satori10000101satori11011000satori10110001satori")
        
        exit()
    if int(lime) == 2:
        fill = open("satori/1006.txt","w")
        fill.write("123")
        fill.write("1234")
        fill.write("1235")
        

        exit()
else:
    print("eoror for your WiFi")
    input()
    exit()
if lime == 'lime':
    del lime
    while True:
        word = input('echo Livel: ')
        lime = open("json\\fill.json","r",encoding='utf-8')
        opener = json.load(lime)
        for o in opener:
            if o['glitch'] == word:
                print(o['1006'])
            else:
                print(True)
if int(lime) == 1006:
    del lime
    lime = randint(0,1000)
    print(lime)
    input()