import sys
import pharma_data
from PySide6.QtCore import Qt, Slot, QSortFilterProxyModel
from PySide6.QtGui import QAction, Qt, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QTableView)
class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.rightLayout = QVBoxLayout()


        self.create_left_layout()
        self.create_right_layout()

        self.mainLayout.addLayout(self.leftLayout, 3)
        self.mainLayout.addLayout(self.rightLayout, 2)

        self.setLayout(self.mainLayout)

    def create_right_layout(self):
        self.medcomLable = QLabel()
        self.medcomLable.setText("Companie's Name")
        self.medcomLable.setStyleSheet('font-size: 25px; height: 40px;')

        self.rightLayout.addWidget(self.medcomLable)


    def create_left_layout(self):
        self.companies = pharma_data.data
        self.model = QStandardItemModel(len(self.companies), 1)
        self.model.setHorizontalHeaderLabels(['Company'])

        for row, company in enumerate(self.companies):
            item = QStandardItem(company)
            self.model.setItem(row, 0, item)

        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.search_field = QLineEdit()          
        self.search_field.setStyleSheet('font-size: 25px; height: 40px;')
        self.search_field.textChanged.connect(self.filter_proxy_model.setFilterRegularExpression)
        self.leftLayout.addWidget(self.search_field)

        self.table = QTableView()
        self.table.setStyleSheet('font-size: 20px;')
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setModel(self.filter_proxy_model)
        self.table.clicked.connect(self.tableSelected)
        self.leftLayout.addWidget(self.table)

    def tableSelected(self, selectedElement):
        print("Currently Selected: ", selectedElement.data())
        self.medcomLable.setText(selectedElement.data())



class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(1200, 700)
    window.show()

    # Execute application
    sys.exit(app.exec())
