from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
app = QApplication([])
window = QWidget()
window.setWindowTitle('ПрИлОжУхА')
window.resize(400,200)








mane_layout = QVBoxLayout()
line_H1=QHBoxLayout()
text=QLabel('Какого города не существует ?')
line_H1.addWidget(text)

RadioGroupBox = QGroupBox("Варианты ответов")
AnsGroupBox = QGroupBox("ответ")

rbtn_1 = QRadioButton('ora')
rbtn_2 = QRadioButton('stone ocean')
rbtn_3 = QRadioButton('Morio')
rbtn_4 = QRadioButton('DIO')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
lb_correct = QLabel("ответ будет здесь")
lb_result = QLabel("прав ты или нет")

za_wurdo = QVBoxLayout()
za_wurdo.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
za_wurdo.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(za_wurdo)

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

mane_layout.addLayout(line_H1)

RadioGroupBox.setLayout(layout_ans1)
mane_layout.addWidget(RadioGroupBox)
mane_layout.addWidget(AnsGroupBox)
AnsGroupBox.hide()
line_H2=QHBoxLayout()
btn=QPushButton('ответить')#
line_H2.addWidget(btn)
mane_layout.addLayout(line_H2)
window.setLayout(mane_layout)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]



def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText("следуйщий вопрос")
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText("ответить")#
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if answer[0].isChecked():
        show_correct('верно')
    else:
        if answer [1].isChecked() or answer[2].isChecked or answer[3].isChecked:
            show_question()

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()
window.cur_question = -1
def next_question():
    window.cur_question += 1
    window.cur_question(0, len(question_list) -1)
    if window.cur_question >= len(questions_list):

        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def show_correct(result):
    lb_result.setText(result)
    show_result()

def click_okay():
    if btn.text() == 'ответить':
        test()
    else:
        next_question()

btn.clicked.connect(test)

window.show()
app.exec()
