from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QComboBox, QGridLayout
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image
import sys
import sqlite3
import random

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 250, 300, 200)
        label = QLabel("Добро пожаловать!"
                       "Выберите тему для игры!", self)
        label.resize(250, 100)
        label.move(10, 10)

        self.combo = QComboBox(self)
        self.combo.resize(200, 40)
        self.combo.addItem("Темы")
        self.combo.addItem("Растения")
        self.combo.addItem("Животные")
        self.combo.addItem("Компьютеры и техника")
        self.combo.addItem("Кулинария")
        self.combo.currentTextChanged.connect(self.onChanged)

    def onChanged(self, text):
        if text != "Темы":
            self.ex1 = AddWindow(None, text)
            self.ex1.show()


class AddWindow(QWidget):
    def __init__(self, parent=None, text='Темы'):
        self.com_text = text
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(650, 500, 650, 500)
        self.setWindowTitle('Виселица')

        pixmap = QPixmap("V1.png")
        self.label = QLabel(self)
        self.label.resize(290, 340)
        self.label.move(330, 10)
        self.label.setPixmap(pixmap)

        self.label_4 = QLabel('Ошибок:', self)
        self.label_4.resize(self.label_4.sizeHint())
        self.label_4.move(10, 110)

        self.label_5 = QLabel(self)
        self.label_5.resize(self.label_5.sizeHint())
        self.label_5.move(110, 110)

        self.label_6 = QLabel('Описание:', self)
        self.label_6.resize(self.label_6.sizeHint())
        self.label_6.move(10, 150)

        self.label_7 = QLabel(self)
        self.label_7.resize(300, 170)
        self.label_7.move(10, 180)

        self.label_8 = QLabel('Слово:', self)
        self.label_8.resize(self.label_8.sizeHint())
        self.label_8.move(10, 360)

        self.label_9 = QLabel('Выберите букву:', self)
        self.label_9.resize(85, 15)
        self.label_9.move(10, 10)

        self.label_10 = QLabel('Текущая буква:', self)
        self.label_10.resize(85, 15)
        self.label_10.move(120, 10)

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.resize(100, 25)
        self.lineEdit_3.move(120, 40)

        self.combo1 = QComboBox(self)
        self.combo1.resize(100, 25)
        self.combo1.move(10, 40)
        letters = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
        for i in range(33):
            for j in letters:
                self.combo1.addItem(j)
        self.combo1.currentTextChanged.connect(self.o1)
        self.show()
        self.db()

    def db(self, text):
        self.curtext = text
        con = sqlite3.connect('1.db')
        cur = con.cursor()
        cur.execute("""
                   create table if not exists computers
                (
                	names_id int NOT NULL,
                	titles text NOT NULL
                )
                   """).fetchall()
        cur.execute("""
                  insert into computers
                values
                (1, 'Антивирус'),
                (2, 'Браузер'),
                (3, 'Бит'),
                (4, 'Доанлоад'),
                (5, 'Драйвер')
                   """).fetchall()

        cur.execute("""
                   create table if not exists plants
                (
                	names_id int NOT NULL,
                	titles text NOT NULL
                )
                   """).fetchall()
        cur.execute("""
                  insert into plants
                values
                (1, 'Подсолнух'),
                (2, 'Роза'),
                (3, 'Огурец'),
                (4, 'Земляника'),
                (5, 'Банан')
                   """).fetchall()

        cur.execute("""
                   create table if not exists animals
                (
                	names_id int NOT NULL,
                	titles text NOT NULL
                )
                   """).fetchall()

        cur.execute("""
                  insert into animals
                values
                (1, 'Тигр'),
                (2, 'Кот'),
                (3, 'Пеликан'),
                (4, 'Змея'),
                (5, 'Бабочка')
                   """)

        cur.execute("""
                   create table if not exists cooking
                (
                	names_id int NOT NULL,
                	titles text NOT NULL
                )
                   """).fetchall()
        cur.execute("""
                  insert into cooking
                values
                (1, 'Суп'),
                (2, 'Пирог'),
                (3, 'Жульен'),
                (4, 'Гречка'),
                (5, 'Пицца')
                   """).fetchall()
        if self.curtext == "Растения":
            num = random.randint(1, 5)
            cur.execute(f"""
            select titles from plants where names_id = '{num}'""").fetchall()

        con.commit()
        con.close()

    def o1(self, text):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())

