
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import     QMessageBox
from models import session,Customer
import customer_dashboard

class Ui_Form(object):
    def __init__(self):
        # Create a QWidget instance to be used as the parent for file dialogs
        self.parent_widget = QtWidgets.QWidget()
    def viewCustomers(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = customer_dashboard.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def DeleteProduct(self):
        product_to_delete = session.query(Customer).filter(Customer.phone==self.phone.text()).first()
        if product_to_delete:
            session.delete(product_to_delete)
            session.commit()
            QMessageBox.information(self.parent_widget,'Deletion Success',"The customer has been deleted successfully from the database")
        elif not product_to_delete:
            QMessageBox.critical(self.parent_widget,'No such entry','The customer you are trying to delete does not exists in the stores database.')
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 640)
        Form.setMaximumSize(1000,640)
        Form.setMinimumSize(1000,640)
        icon = QtGui.QIcon.fromTheme("k")
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1001, 111))
        self.widget.setStyleSheet("background-color: rgb(255, 69, 0);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(400, 10, 341, 51))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 70, 1001, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 130, 251, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 251, 31))
        self.label_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(400, 199, 501, 61))
        self.name.setObjectName("name")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 311, 91, 31))
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(400, 300, 501, 61))
        self.phone.setObjectName("phone")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(-10, 770, 1011, 31))
        self.widget_2.setStyleSheet("background-color: rgb(100, 233, 134);")
        self.widget_2.setObjectName("widget_2")
        self.add_customer = QtWidgets.QPushButton(Form)
        self.add_customer.setGeometry(QtCore.QRect(40, 460, 271, 81))
        self.add_customer.setStyleSheet("background-color: rgb(250, 235, 215);")
        self.add_customer.setObjectName("add_customer")
        self.customer_lists = QtWidgets.QPushButton(Form)
        self.customer_lists.setGeometry(QtCore.QRect(410, 460, 271, 81))
        self.customer_lists.setStyleSheet("background-color: rgb(250, 235, 215);")
        self.customer_lists.setObjectName("customer_lists")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(770, 460, 161, 81))
        self.exit.setStyleSheet("background-color: rgb(250, 235, 215);")
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.add_customer.clicked.connect(self.DeleteProduct)
        self.customer_lists.clicked.connect(self.viewCustomers)
        self.exit.clicked.connect(Form.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Delete Customer"))
        self.label.setText(_translate("Form", "DELETE CUSTOMER"))
        self.label_2.setText(_translate("Form", "Fill In The Fields Below"))
        self.label_3.setText(_translate("Form", "Name:"))
        self.name.setPlaceholderText(_translate("Form", "Full name"))
        self.label_4.setText(_translate("Form", "Phone :"))
        self.phone.setPlaceholderText(_translate("Form", "0712345678"))
        self.add_customer.setText(_translate("Form", "DELETE CUSTOMER"))
        self.customer_lists.setText(_translate("Form", "CUSTOMER LISTS"))
        self.exit.setText(_translate("Form", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
