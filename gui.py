from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3
import sys
from classes import *
        
class CustomTreeWidgetConditionItem(QTreeWidgetItem):
    def __init__(self, parent, status, name, dateStart):
        super().__init__(parent)
        self.status = status
        self.name = name
        self.startDate = dateStart

        self.main = QWidget()
        mainLayout = QHBoxLayout()

        # Add spacers depending on the depth of the node being created
        for rng in range(0, self.depth()):
            bufferLabel = QLabel("")
            bufferLabel.setStyleSheet("QLabel { background-color: rgba(255, 255, 255, 0) }")
            bufferLabel.setFixedWidth(15)
            mainLayout.addWidget(bufferLabel)

        statusLabel = QLabel("")
        if self.status == "confirmed":
            statusLabel.setStyleSheet("QLabel { background-color: green }")
        else:
            statusLabel.setStyleSheet("QLabel { background-color: red }")
        statusLabel.setFixedWidth(15)
        statusLabel.setFixedHeight(45)
        mainLayout.addWidget(statusLabel)

        subLayout = QVBoxLayout()
        conditionLabel = QLabel(self.name)
        conditionLabel.setStyleSheet("QLabel { font-size: 20px }")
        dateLabel = QLabel(self.startDate)
        dateLabel.setStyleSheet("QLabel { font-size: 10px }")
        subLayout.addWidget(conditionLabel)
        subLayout.addWidget(dateLabel)

        mainLayout.addLayout(subLayout)
        self.main.setLayout(mainLayout)

    def depth(self):
        if type(self.parent()) == type(None):
            return 0
        else:
            return 1 + self.parent().depth()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize instance attributes
        self.treeWidget = QTreeWidget()
        self.conditionViewWidget = QWidget()
        self.mainMenu = self.menuBar()
        self.mainWidget = QWidget()
        self.data = Hierarchy()
        self.dbConnection = None
        self.dbCursor = None

        self.setGeometry(50, 50, 800, 300)
        self.setWindowTitle("Health Program")

        # Modify menu-/status- bars for the UI
        self.statusBar()

        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Leave the Game")
        exitAction.triggered.connect(self.close)

        self.fileMenu = self.mainMenu.addMenu("&File")
        self.fileMenu.addAction(exitAction)

        # Initialize tree widget view
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setColumnCount(1)
        condition1 = CustomTreeWidgetConditionItem(self.treeWidget, "confirmed", "Heavy Metal Toxicity", "6/10/2012")
        condition2 = CustomTreeWidgetConditionItem(condition1, "tentative", "Leprosy", "10/26/2015")
        condition3 = CustomTreeWidgetConditionItem(self.treeWidget, "ended", "Nothing", "3/13/2014")
        self.treeWidget.setItemWidget(condition1, 0, condition1.main)
        self.treeWidget.setItemWidget(condition2, 0, condition2.main)
        self.treeWidget.setItemWidget(condition3, 0, condition3.main)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget.header().setStretchLastSection(False)
        self.treeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.treeWidget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored)

        # Initialize item detail widget
        self.initConditionViewWidget()

        # Lay out the main UI elements
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.treeWidget)
        mainLayout.addWidget(self.conditionViewWidget)
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.mainWidget.setLayout(mainLayout)
        self.setCentralWidget(self.mainWidget)

    def initConditionViewWidget(self):
        background = self.palette()
        
        conditionViewLayout = QVBoxLayout()

        conditionViewHeader = QHBoxLayout()
        conditionViewHeaderGrid = QGridLayout()
        headerName = QLabel("Heavy Metal Toxicity")
        headerName.setStyleSheet("QLabel { font-size: 25px; }")
        diagnoseStartLbl = QLabel("Date diagnosed")
        diagnoseEndLbl = QLabel("Date concluded")
        diagnoseStartDate = QLabel("12/30/14")
        diagnoseEndDate = QLabel("5/5/15")
        conditionViewHeader.addWidget(headerName)
        conditionViewHeader.addStretch()
        conditionViewHeaderGrid.addWidget(diagnoseStartLbl, 0, 0)
        conditionViewHeaderGrid.addWidget(diagnoseStartDate, 0, 1)
        conditionViewHeaderGrid.addWidget(diagnoseEndLbl, 1, 0)
        conditionViewHeaderGrid.addWidget(diagnoseEndDate, 1, 1)
        conditionViewHeader.addLayout(conditionViewHeaderGrid)

        conditionDiagLine = QHBoxLayout()
        diagnoseByLbl = QLabel("Diagnosed by")
        diagnoseBy = QLabel("Neil Nathan")
        conditionDiagLine.addWidget(diagnoseByLbl)
        conditionDiagLine.addWidget(diagnoseBy)
        conditionDiagLine.addStretch()

        statusDiagLine = QHBoxLayout()
        statusLbl = QLabel("Status")
        status = QLabel("Confirmed")
        statusDiagLine.addWidget(statusLbl)
        statusDiagLine.addWidget(status)
        statusDiagLine.addStretch()

        testTreatmentsLayout = QHBoxLayout()
        testLayout = QVBoxLayout()
        testCaption = QLabel("Tests")
        testDetail = QListWidget()
        testDetail.setMinimumHeight(200)
        testLayout.addWidget(testCaption)
        testLayout.addWidget(testDetail)
        treatmentLayout = QVBoxLayout()
        treatmentCaption = QLabel("Treatments")
        treatmentDetail = QListWidget()
        treatmentDetail.setMinimumHeight(200)
        treatmentLayout.addWidget(treatmentCaption)
        treatmentLayout.addWidget(treatmentDetail)
        testTreatmentsLayout.addLayout(testLayout)
        testTreatmentsLayout.addLayout(treatmentLayout)

        notes = QTextEdit()
        notes.setMinimumHeight(200)
        notes.setStyleSheet("QTextEdit { border: 1px solid black }")

        conditionViewLayout.addLayout(conditionViewHeader)
        conditionViewLayout.addLayout(conditionDiagLine)
        conditionViewLayout.addLayout(statusDiagLine)
        conditionViewLayout.addLayout(testTreatmentsLayout)
        conditionViewLayout.addWidget(notes)
        conditionViewLayout.addStretch()
        self.conditionViewWidget.setLayout(conditionViewLayout)

    def importData(self, dbName):
        self.dbConnection = sqlite3.connect(dbName)
        self.dbCursor = self.dbConnection.cursor()

        self.dbCursor.execute()
        
if __name__ == "__main__":
        app = QApplication(sys.argv)
        form = Window()
        form.show()
        app.exec_()
