import sys
from PyQt6.QtWidgets import QDialog, QApplication
from layout import Ui_Dialog


class MyForm(QDialog):
    list_txt = ""
    cal_sum = 0
    cal_need = 1900
    cal_need_table = {
        "female": [1700, 1900, 2100],
        "male": [1900, 2200, 2500],
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_add.clicked.connect(self.add)
        self.ui.txt_cal.textChanged.connect(self.checkNum)

        for i in [self.ui.radio_male, self.ui.radio_female,
                  self.ui.radio_low, self.ui.radio_medium, self.ui.radio_high]:
            i.clicked.connect(self.cal_need_change)

    def cal_need_change(self):
        g = "female"
        if self.ui.radio_male.isChecked():
            g = "male"

        activity=0
        if self.ui.radio_medium.isChecked():
            activity=1
        elif self.ui.radio_high.isChecked():
            activity=2

        self.cal_need=self.cal_need_table[g][activity]

        self.color_update()

    def color_update(self):
        cal_pr=self.cal_sum/self.cal_need

        if cal_pr<0.8:
            self.ui.sum_label.setStyleSheet("background-color:green;\ncolor: white;")
        elif cal_pr<=1:
            self.ui.sum_label.setStyleSheet("background-color:black;\ncolor: white;")
        else:
            self.ui.sum_label.setStyleSheet("background-color:red;\ncolor: white;")

    def checkNum(self):
        txt = self.ui.txt_cal.text()
        if not txt.isnumeric():
            self.ui.txt_cal.setText(txt[:-1])

    def add(self):
        meal = self.ui.txt_meal.text()
        cal = self.ui.txt_cal.text()

        self.list_txt += meal + " - " + cal + "kalorii\n"
        self.ui.list.setText(self.list_txt)

        self.cal_sum += int(cal)

        self.color_update()

        self.ui.sum_label.setText("suma spożytych kalorii: "+str(self.cal_sum))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()

    sys.exit(app.exec())
