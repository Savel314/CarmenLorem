import sys
from storageBD import sort_nameDB, sort_authorDB, addBD, delBD, renameBD
from PyQt6 import uic
from PyQt6.QtWidgets import *
from discord_bot import *
import asyncio


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('BaseUI.ui', self)
        self.setWindowTitle('Музоставиль')
        self.setFixedSize(800, 600)

        self.page = 10
        self.page_ui = 1
        self.sel_link = ''
        self.press_key = 0
        self.useful = None
        self.tablet()
        self.left_right()
        self.nameDB()
        self.click_link()
        self.pl_but()
        self.pause_but()
        self.unpause_but()
        self.channel_txt = open('discord_channel.txt', 'r').read()
        self.Other_Button.clicked.connect(self.other_widget)

    def left_right(self):
        self.left_but.clicked.connect(self.left_button)
        self.right_but.clicked.connect(self.right_button)
        self.page_label.setText(str(self.page_ui))

    def right_button(self):
        self.page += 10
        self.page_ui += 1
        self.page_label.setText(str(self.page_ui))
        self.demon()

    def left_button(self):
        if self.page != 10:
            self.page -= 10
            self.page_ui -= 1
            self.page_label.setText(str(self.page_ui))
            self.demon()

    def tablet(self):
        self.Name_Button.clicked.connect(self.nameDB)
        self.Author_Button.clicked.connect(self.authorDB)

    def nameDB(self):
        self.useful = sort_nameDB()
        self.demon()

    def authorDB(self):
        self.useful = sort_authorDB()
        self.demon()

    def demon(self):  # demon -> demonstration
        self.name1.setText(''), self.link1.setText(''), self.author1.setText('')
        self.name2.setText(''), self.link2.setText(''), self.author2.setText('')
        self.name3.setText(''), self.link3.setText(''), self.author3.setText('')
        self.name4.setText(''), self.link4.setText(''), self.author4.setText('')
        self.name5.setText(''), self.link5.setText(''), self.author5.setText('')
        self.name6.setText(''), self.link6.setText(''), self.author6.setText('')
        self.name7.setText(''), self.link7.setText(''), self.author7.setText('')
        self.name8.setText(''), self.link8.setText(''), self.author8.setText('')
        self.name9.setText(''), self.link9.setText(''), self.author9.setText('')
        self.name10.setText(''), self.link10.setText(''), self.author10.setText('')
        lenght = len(self.useful)
        for i in range(self.page - 10, self.page):
            if i >= lenght:
                continue
            else:
                if i < 10:
                    one, two, three = self.useful[i]
                    if i == 0:
                        self.name1.setText(one), self.link1.setText(two), self.author1.setText(three)
                    if i == 1:
                        self.name2.setText(one), self.link2.setText(two), self.author2.setText(three)
                    if i == 2:
                        self.name3.setText(one), self.link3.setText(two), self.author3.setText(three)
                    if i == 3:
                        self.name4.setText(one), self.link4.setText(two), self.author4.setText(three)
                    if i == 4:
                        self.name5.setText(one), self.link5.setText(two), self.author5.setText(three)
                    if i == 5:
                        self.name6.setText(one), self.link6.setText(two), self.author6.setText(three)
                    if i == 6:
                        self.name7.setText(one), self.link7.setText(two), self.author7.setText(three)
                    if i == 7:
                        self.name8.setText(one), self.link8.setText(two), self.author8.setText(three)
                    if i == 8:
                        self.name9.setText(one), self.link9.setText(two), self.author9.setText(three)
                    if i == 9:
                        self.name10.setText(one), self.link10.setText(two), self.author10.setText(three)
                else:
                    one, two, three = self.useful[i]
                    i = int(str(i)[-1])
                    if i == 0:
                        self.name1.setText(one), self.link1.setText(two), self.author1.setText(three)
                    if i == 1:
                        self.name2.setText(one), self.link2.setText(two), self.author2.setText(three)
                    if i == 2:
                        self.name3.setText(one), self.link3.setText(two), self.author3.setText(three)
                    if i == 3:
                        self.name4.setText(one), self.link4.setText(two), self.author4.setText(three)
                    if i == 4:
                        self.name5.setText(one), self.link5.setText(two), self.author5.setText(three)
                    if i == 5:
                        self.name6.setText(one), self.link6.setText(two), self.author6.setText(three)
                    if i == 6:
                        self.name7.setText(one), self.link7.setText(two), self.author7.setText(three)
                    if i == 7:
                        self.name8.setText(one), self.link8.setText(two), self.author8.setText(three)
                    if i == 8:
                        self.name9.setText(one), self.link9.setText(two), self.author9.setText(three)
                    if i == 9:
                        self.name10.setText(one), self.link10.setText(two), self.author10.setText(three)

    def click_link(self):
        self.Button_1.clicked.connect(self.onee)
        self.Button_2.clicked.connect(self.twoo)
        self.Button_3.clicked.connect(self.threee)
        self.Button_4.clicked.connect(self.fourr)
        self.Button_5.clicked.connect(self.fivee)
        self.Button_6.clicked.connect(self.sixx)
        self.Button_7.clicked.connect(self.sevenn)
        self.Button_8.clicked.connect(self.eightt)
        self.Button_9.clicked.connect(self.ninee)
        self.Button_10.clicked.connect(self.tenn)

    def getting_link(self):
        lenght1 = len(self.useful)

        if self.page_ui == 1:
            if self.press_key < lenght1 - 1:
                d, z, u = self.useful[self.press_key]
                self.sel_link = z
            else:
                self.sel_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        if self.page_ui != 1:
            if int(str(self.page_ui - 1) + str(self.press_key)) < lenght1 - 1:
                d, z, u = self.useful[int(str(self.page_ui - 1) + str(self.press_key))]
                self.sel_link = z
            else:
                self.sel_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    def onee(self):
        self.press_key = 0
        self.getting_link()

    def twoo(self):
        self.press_key = 1
        self.getting_link()

    def threee(self):
        self.press_key = 2
        self.getting_link()

    def fourr(self):
        self.press_key = 3
        self.getting_link()

    def fivee(self):
        self.press_key = 4
        self.getting_link()

    def sixx(self):
        self.press_key = 5
        self.getting_link()

    def sevenn(self):
        self.press_key = 6
        self.getting_link()

    def eightt(self):
        self.press_key = 7
        self.getting_link()

    def ninee(self):
        self.press_key = 8
        self.getting_link()

    def tenn(self):
        self.press_key = 9
        self.getting_link()

    def return_link(self):
        return self.sel_link

    def pl_but(self):
        self.Play_Button.clicked.connect(self.discord_play_bot)

    def discord_play_bot(self):
        asyncio.run(run_bot(self.return_link(), self.channel_txt))

    def pause_but(self):
        self.Pause_Button.clicked.connect(self.discord_pause_bot)

    def discord_pause_bot(self):
        asyncio.run(send_pause_command(self.channel_txt))

    def unpause_but(self):
        self.Unpause_Button.clicked.connect(self.discord_unpause_bot)

    def discord_unpause_bot(self):
        asyncio.run(send_unpause_command(self.channel_txt))

    def other_widget(self):
        self.otherr = Two_Widget()
        self.otherr.show()


class Two_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Comp.ui', self)
        self.setWindowTitle('Музоставиль - добавление в базу данных')
        self.setFixedSize(540, 300)
        self.press_but()
        self.press_but2()
        self.press_but3()

    def press_but(self):
        self.pushButton.clicked.connect(self.addaalink)

    def addaalink(self):
        name = self.lineEdit.text()
        link = self.lineEdit_2.text()
        author = self.lineEdit_3.text()
        if link != '' and name != '' and author != '':
            addBD(name, link, author)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()

    def press_but2(self):
        self.pushButton_2.clicked.connect(self.delllink)

    def delllink(self):
        name = self.lineEdit_4.text()
        if name != '':
            delBD(name)
            self.lineEdit_4.clear()

    def press_but3(self):
        self.pushButton_3.clicked.connect(self.renamelink)

    def renamelink(self):
        old_name = self.lineEdit_5.text()
        new_name = self.lineEdit_6.text()
        renameBD(old_name, new_name)
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    exx = QWidget()
    ex.show()
    sys.exit(app.exec())
