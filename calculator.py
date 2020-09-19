import PyQt5.QtWidgets as QtW


class MainWindow(QtW.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulačka")
        self.setLayout(QtW.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []


        self.show()

    def keypad(self):
        container = QtW.QWidget()
        container.setLayout(QtW.QGridLayout())

        self.result_field = QtW.QLineEdit()
        btn_result = QtW.QPushButton("Enter", clicked = self.func_result)
        btn_clear = QtW.QPushButton("Clear", clicked= self.clear_calc)
        btn_1 = QtW.QPushButton("1", clicked= lambda:self.num_press("1"))
        btn_2 = QtW.QPushButton("2", clicked= lambda:self.num_press("2"))
        btn_3 = QtW.QPushButton("3", clicked= lambda:self.num_press("3"))
        btn_4 = QtW.QPushButton("4", clicked= lambda:self.num_press("4"))
        btn_5 = QtW.QPushButton("5", clicked= lambda:self.num_press("5"))
        btn_6 = QtW.QPushButton("6", clicked= lambda:self.num_press("6"))
        btn_7 = QtW.QPushButton("7", clicked= lambda:self.num_press("7"))
        btn_8 = QtW.QPushButton("8", clicked= lambda:self.num_press("8"))
        btn_9 = QtW.QPushButton("9", clicked= lambda:self.num_press("9"))
        btn_0 = QtW.QPushButton("0", clicked= lambda:self.num_press("0"))
        btn_plus = QtW.QPushButton("+", clicked = lambda:self.func_press("+"))
        btn_minus = QtW.QPushButton("-", clicked = lambda:self.func_press("-"))
        btn_mult = QtW.QPushButton("*", clicked = lambda:self.func_press("*"))
        btn_divd = QtW.QPushButton("/", clicked = lambda:self.func_press("/"))

        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4,3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divd, 5, 3)
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText("".join(self.fin_nums) +temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operators):
        temp_string = "".join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText("".join(self.fin_nums))

    def func_result(self):
        fin_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += "="
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []



        



app = QtW.QApplication([])
mw = MainWindow()
app.setStyle(QtW.QStyleFactory.create("Fusion"))










app.exec_()
