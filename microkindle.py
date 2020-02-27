from microbit import *
pages = 0 #variavel para páginas
cover = Image(
        "00900:"
        "09590:"
        "95559:"
        "95559:"
        "09990")
display.show(cover)

page1_1 = Image(
        "09090:"
        "99999:"
        "09990:"
        "99999:"
        "09090")
page1_2 = Image(
        "00000:"
        "09990:"
        "09990:"
        "09990:"
        "00000:")
page2_1 = Image(
        "00009:"
        "90000:"
        "00900:"
        "00090:"
        "99999")
page2_2 = Image(
        "90000:"
        "00900:"
        "00090:"
        "09000:"
        "99999")
page2_3 = Image(
        "00900:"
        "00090:"
        "09000:"
        "00009:"
        "99999")
page2_4 = Image(
        "00090:"
        "09000:"
        "00009:"
        "90000:"
        "99999")
page2_5 = Image(
        "09000:"
        "00009:"
        "90000:"
        "00900:"
        "99999")
page3_1 = Image(
        "00000:"
        "00990:"
        "09990:"
        "99999:"
        "00000")
page3_2 = Image(
        "00000:"
        "09900:"
        "99900:"
        "99990:"
        "00000")
page3_3 = Image(
        "00000:"
        "90000:"
        "99000:"
        "99900:"
        "00000")
page3_4 = Image(
        "00000:"
        "00000:"
        "90000:"
        "99000:"
        "00000")
page3_5 = Image(
        "00000:"
        "00000:"
        "00000:"
        "90000:"
        "00000")
page3_6 = Image
        "00000:"
        "00000:"
        "00000:"
        "00009:"
        "00000")
page3_7 = Image(
        "00000:"
        "00000:"
        "00009:"
        "00099:"
        "00000")
page3_8 = Image(
        "00000:"
        "00009:"
        "00099:"
        "00999:"
        "00000")
page3_9 = Image(
        "00000:"
        "00099:"
        "00999:"
        "09999:"
        "00000")

page4_1 = Image(
        "90009:"
        "00000:"
        "00900:"
        "00009:"
        "09000")
page4_2 = Image(
        "90009:"
        "00000:"
        "00900:"
        "00900:"
        "00009")
page4_3 = Image(
        "00090:"
        "09000:"
        "90009:"
        "00000:"
        "00900")
page4_4 = Image(
        "90000:"
        "00090:"
        "09000:"
        "90009:"
        "00000")
page4_5 = Image(
        "00000:"
        "90000:"
        "00090:"
        "09000:"
        "90009")
page4_6 = Image(
        "09000:"
        "00000:"
        "90000:"
        "00090:"
        "09000")
page4_7 = Image(
        "00009:"
        "09000:"
        "00000:"
        "90000:"
        "00090")
page4_8 = Image(
        "00900:"
        "00009:"
        "09000:"
        "00000:"
        "90000")
page4_9 = Image(
        "00000:"
        "00900:"
        "00009:"
        "09000:"
        "00000")
page5_1 = Image(
        "00090:"
        "09000:"
        "99999:"
        "00000:"
        "99999")
page5_2 = Image(
        "00000:"
        "00090:"
        "99999:"
        "99999:"
        "99999")
page5_3 = Image(
        "09000:"
        "00000:"
        "99999:"
        "99999:"
        "99999")
page5_4 = Image(
        "00000:"
        "00000:"
        "99999:"
        "00000:"
        "00000")
page6_1 = Image(
        "00000:"
        "00000:"
        "00000:"
        "99999:"
        "99999")
page6_2 = Image(
        "00000:"
        "00000:"
        "00009:"
        "99999:"
        "99999")
page6_3 = Image(
        "00000:"
        "00009:"
        "00009:"
        "99999:"
        "99999")
page6_4 = Image(
        "00099:"
        "00099:"
        "00009:"
        "99909:"
        "99999")
page6_5 = Image(
        "00999:"
        "00099:"
        "00009:"
        "99009:"
        "99999")
page6_6 = Image(
        "00990:"
        "09999:"
        "00099:"
        "90009:"
        "99999")
page6_7 = Image(
        "00000:"
        "09990:"
        "99999:"
        "90099:"
        "99999")
page6_8 = Image(
        "00000:"
        "00000:"
        "99999:"
        "99999:"
        "99999")

def coverpage():
    display.show(cover)

def page1():
    display.show([page1_1,page1_2,page1_1,page1_2])

def page2():
    display.show([page2_1,page2_2,page2_3,page2_4,page2_5])

def page3():
    display.show([page3_1,page3_2,page3_3,page3_4,
                    page3_5,page3_6,page3_7,page3_8,page3_9])

def page4()
    display.show([page4_1,page4_2,page4_3,page4_4,page4_5,
                page4_6,page4_7,page4_8,page4_9])