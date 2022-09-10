import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QRegExp,QSize
import time
import about

textChanged = False
url = ""
tbChecked = True
dockChecked = True
statusbarChecked = True

class FindDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find and Replace")
        self.setGeometry(450,250,350,200)
        self.UI()

    def UI(self):
        formLayout = QFormLayout(self)
        hbox = QHBoxLayout()
        txtFind = QLabel("Find : ")
        txtReplace = QLabel("Replace : ")
        txtEmpty = QLabel("")
        self.findInput = QLineEdit()
        self.replaceInput = QLineEdit()
        self.btnFind = QPushButton("Find")
        self.btnReplace = QPushButton("Replace")
        hbox.addWidget(self.btnFind)
        hbox.addWidget(self.btnReplace)
        formLayout.addRow(txtFind,self.findInput)
        formLayout.addRow(txtReplace,self.replaceInput)
        formLayout.addRow(txtEmpty,hbox)
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gelismis Text Editor")
        self.setWindowIcon(QIcon('icons/notepad.png'))
        self.setGeometry(450,150,1000,800)

        self.UI()

    def UI(self):
        self.editor =QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.setFontPointSize(12.0)
        self.editor.textChanged.connect(self.funcTextChanged)
        self.menu()
        self.toolbar()
        self.dockbar()
        self.statusbar()


        self.show()
        
    def statusbar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def funcTextChanged(self):
        global textChanged
        textChanged = True
        text = self.editor.toPlainText()
        letters = len(text)
        words = len(text.split())  # merhaba dunya
        self.status_bar.showMessage("Harf Sayisi :" +str(letters)+ " Kelime sayisi :" + str(words))


    def dockbar(self):
        self.dock = QDockWidget("Short Cuts",self)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dockWidget = QWidget(self)
        self.dock.setWidget(self.dockWidget)
        formLayout = QFormLayout()
        ######################################################################
        btnFind = QToolButton()
        btnFind.setIcon(QIcon('icons/find_large.png'))
        btnFind.setText("Find")
        btnFind.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnFind.setIconSize(QSize(50,50))
        btnFind.setCheckable(True)
        btnFind.toggled.connect(self.Find)
        ########################################################################
        btnNew = QToolButton()
        btnNew.setIcon(QIcon('icons/new_large.png'))
        btnNew.setText("New")
        btnNew.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnNew.setIconSize(QSize(50, 50))
        btnNew.setCheckable(True)
        btnNew.toggled.connect(self.newFile)
        ########################################################################
        btnOpen = QToolButton()
        btnOpen.setIcon(QIcon('icons/open_large.png'))
        btnOpen.setText("Open")
        btnOpen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnOpen.setIconSize(QSize(50, 50))
        btnOpen.setCheckable(True)
        btnOpen.toggled.connect(self.openFile)
        ########################################################################
        btnSave = QToolButton()
        btnSave.setIcon(QIcon('icons/save_large.png'))
        btnSave.setText("Save")
        btnSave.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        btnSave.setIconSize(QSize(50, 50))
        btnSave.setCheckable(True)
        btnSave.toggled.connect(self.saveFile)
        ########################################################################
        formLayout.addRow(btnFind,btnNew)
        formLayout.addRow(btnOpen,btnSave)
        self.dockWidget.setLayout(formLayout)
        ########################################################################
    def toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.changeFont)
        self.tb.addWidget(self.fontFamily)
        self.tb.addSeparator()
        self.tb.addSeparator()
        #####################################################################################
        self.fontSize = QComboBox(self)
        self.tb.addWidget(self.fontSize)
        self.fontSize.setEditable(True)
        for i in range(8,100):
            self.fontSize.addItem(str(i))
        self.fontSize.setCurrentText("12")
        self.fontSize.currentTextChanged.connect(self.changeFontSize)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ###################################################################################
        self.bold = QAction(QIcon('icons/bold.png'), "Bold Yap", self)
        self.tb.addAction(self.bold)
        self.bold.triggered.connect(self.Bold)
        ###################################################################################
        self.italic = QAction(QIcon('icons/italic.png'),"Italic Yap",self)
        self.tb.addAction(self.italic)
        self.italic.triggered.connect(self.Italic)
        ###################################################################################
        self.underline = QAction(QIcon("icons/underline.png"), "Alti Cizgili",self)
        self.tb.addAction(self.underline)
        self.underline.triggered.connect(self.Underline)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ######################################################################################
        self.fontColor= QAction(QIcon('icons/color.png'),"Change Color",self)
        self.tb.addAction(self.fontColor)
        self.fontColor.triggered.connect(self.funcFontColor)
        ########################################################################################
        self.fontBackColor = QAction(QIcon('icons/backcolor.png'), "Back Color", self)
        self.tb.addAction(self.fontBackColor)
        self.fontBackColor.triggered.connect(self.funcFontBackColor)
        self.tb.addSeparator()
        self.tb.addSeparator()
        ###############################################################################################
        self.alignLeft = QAction(QIcon('icons/alignleft.png',), "Sola Hizala", self)
        self.tb.addAction(self.alignLeft)
        self.alignLeft.triggered.connect(self.funcAlignLeft)
        ##################################################################################################
        self.alignCenter = QAction(QIcon('icons/aligncenter.png',), "Ortala", self)
        self.tb.addAction(self.alignCenter)
        self.alignCenter.triggered.connect(self.funcAlignCenter)
        ##################################################################################################
        self.alignRight = QAction(QIcon('icons/alignright.png', ), "Saga Hizala", self)
        self.tb.addAction(self.alignRight)
        self.alignRight.triggered.connect(self.funcAlignRight)
        ##################################################################################################
        self.alignJustify = QAction(QIcon('icons/alignjustify.png', ), "Align Justify", self)
        self.tb.addAction(self.alignJustify)
        self.alignJustify.triggered.connect(self.funcAlignJustify)
        self.tb.addSeparator()
        self.tb.addSeparator()
        #######################################################################################
        self.bulletList = QAction(QIcon('icons/bulletlist.png'), "Bullet List", self)
        self.tb.addAction(self.bulletList)
        self.bulletList.triggered.connect(self.funcBulletList)
        #######################################################################################
        self.numberedList = QAction(QIcon('icons/numberlist.png'), "Numbered List", self)
        self.tb.addAction(self.numberedList)
        self.numberedList.triggered.connect(self.funcNumberedList)
    def funcNumberedList(self):
        self.editor.insertHtml("<ol><li><h3>&nbsp;</h3></li></ol>")

    def funcBulletList(self):
        self.editor.insertHtml("<ul><li><h3>&nbsp;</h3></li><ul>")

    def funcAlignLeft(self):
        self.editor.setAlignment(Qt.AlignLeft)

    def funcAlignCenter(self):
        self.editor.setAlignment(Qt.AlignCenter)

    def funcAlignRight(self):
        self.editor.setAlignment(Qt.AlignRight)

    def funcAlignJustify(self):
        self.editor.setAlignment(Qt.AlignJustify)
    def funcFontColor(self):
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)
    def funcFontBackColor(self):
        bcolor = QColorDialog.getColor()
        self.editor.setTextBackgroundColor((bcolor))

    def Bold(self):
        fontWeight = self.editor.fontWeight()
        if fontWeight == 50:
            self.editor.setFontWeight(QFont.Bold)
        elif fontWeight == 75:
            self.editor.setFontWeight(QFont.Normal)
    def Italic(self):
        italic = self.editor.fontItalic()
        if italic == True:
            self.editor.setFontItalic(False)
        else:
            self.editor.setFontItalic(True)
    def Underline(self):
        underline = self.editor.fontUnderline()
        if underline == True:
            self.editor.setFontUnderline(False)
        else:
            self.editor.setFontUnderline(True)

    def changeFont(self,font):
        font = QFont(self.fontFamily.currentFont())
        self.editor.setCurrentFont(font)

    def changeFontSize(self,fontSize):
        self.editor.setFontPointSize(float(fontSize))
        ########################################### Toolbar Bitis######################################################

    def menu(self):
        ################################Ana Menu######################################

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        help_menu = menubar.addMenu("Help")
        ################################Alt Menuler######################################
        new = QAction(QIcon('icons/new.png'),"New",self)
        new.setShortcut("Alt+Insert")
        new.triggered.connect(self.newFile)
        file.addAction(new)
        ###################################################################################
        open = QAction(QIcon('icons/open.png'), "Open", self)
        open.setShortcut("Ctrl+O")
        open.triggered.connect(self.openFile)
        file.addAction(open)
        ###################################################################################
        save = QAction(QIcon('icons/save.png'), "Save", self)
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.saveFile)
        file.addAction(save)
        ###################################################################################
        exit = QAction(QIcon('icons/exit.png'), "Exit", self)
        exit.triggered.connect(self.exitFile)
        file.addAction(exit)
        ###################################################################################
        undo = QAction(QIcon('icons/undo.png'),"Undo",self)
        undo.setShortcut("Ctrl+Z")
        undo.triggered.connect(self.Undo)
        edit.addAction(undo)
        ###################################################################################
        cut = QAction(QIcon('icons/cut.png'), "Cut", self)
        cut.setShortcut("Ctrl+X")
        cut.triggered.connect(self.Cut)
        edit.addAction(cut)
        ###################################################################################
        copy = QAction(QIcon('icons/copy.png'), "Copy", self)
        copy.setShortcut("Ctrl+C")
        copy.triggered.connect(self.Copy)
        edit.addAction(copy)
        ###################################################################################
        paste = QAction(QIcon('icons/paste.png'), "Paste", self)
        paste.setShortcut("Ctrl+V")
        paste.triggered.connect(self.Paste)
        edit.addAction(paste)
        ###################################################################################
        find = QAction(QIcon('icons/find.png'), "Find", self)
        find.setShortcut("Ctrl+F")
        find.triggered.connect(self.Find)
        edit.addAction(find)
         ###################################################################################
        time_date = QAction(QIcon('icons/datetime.png'), "Insert Time and Date",self)
        time_date.setShortcut("F5")
        time_date.triggered.connect(self.Time_Date)
        edit.addAction(time_date)
         ###################################################################################
        toggleStatusBar = QAction("Toggle StatusBar",self,checkable=True)
        toggleStatusBar.triggered.connect(self.funcToggleStatusBar)
        view.addAction(toggleStatusBar)
        ###################################################################################
        toggleToolBar = QAction("Toggle ToolBar", self, checkable=True)
        toggleToolBar.triggered.connect(self.funcToggleToolBar)
        view.addAction(toggleToolBar)
        ###################################################################################
        toggleDockBar = QAction("Toggle DockBar", self, checkable=True)
        toggleDockBar.triggered.connect(self.funcToggleDockBar)
        view.addAction(toggleDockBar)
        ###################################################################################
        about_us = QAction("About Us",self)
        about_us.triggered.connect(self.About)
        help_menu.addAction(about_us)

    def funcToggleStatusBar(self):
        global statusbarChecked
        if statusbarChecked == True:
            self.status_bar.hide()
            statusbarChecked = False
        else:
            self.status_bar.show()
            statusbarChecked = True
    def funcToggleToolBar(self):
        global tbChecked
        if tbChecked == True:
            self.tb.hide()
            tbChecked = False
        else:
            self.tb.show()
            tbChecked = True
    def funcToggleDockBar(self):
        global dockChecked
        if dockChecked == True:
            self.dock.hide()
            dockChecked = False
        else:
            self.dock.show()
            dockChecked = True

    def About(self):
        self.help =about.Help()
        self.help.show()
    def Undo(self):
        self.editor.undo()

    def Cut(self):
        self.editor.cut()

    def Copy(self):
        self.editor.copy()

    def Paste(self):
        self.editor.paste()
    def Find(self):
        self.find = FindDialog()
        self.find.show()

        def findWords():
            global word
            word = self.find.findInput.text()
            if word != "":
                cursor = self.editor.textCursor()
                format = QTextCharFormat()
                format.setBackground(QBrush(QColor("black")))
                regex = QRegExp(word)
                pos = 0
                index = regex.indexIn(self.editor.toPlainText(),pos)
                self.count = 0
                while (index !=-1):
                    cursor.setPosition(index)
                    cursor.movePosition(QTextCursor.EndOfWord,1)
                    cursor.mergeCharFormat(format)
                    pos = index + regex.matchedLength()
                    index = regex.indexIn(self.editor.toPlainText(),pos)
                    self.count +=1
                self.status_bar.showMessage(str(self.count) + "Result Found!")
            else:
                QMessageBox.information(self,"Uyari","Alanlar bos olamaz")

        def replaceWords():
            replaceText = self.find.replaceInput.text()
            word = self.find.findInput.text()
            text = self.editor.toPlainText()
            newValue = text.replace(word,replaceText)
            self.editor.clear()
            self.editor.append(newValue)

        self.find.btnFind.clicked.connect(findWords)
        self.find.btnReplace.clicked.connect(replaceWords)

    def Time_Date(self):
        time_date = time.strftime("%d.%m.%Y %H:%M")
        self.editor.append(time_date)
    def newFile(self):
        try:
            global url
            url = ""
            self.editor.clear()

        except:
            pass
    def openFile(self):
        global url
        try:
            url = QFileDialog.getOpenFileName(self,"Dosya Ac","","All files(*)::Txt Files *txt")
            with open(url[0],'r+', encoding='utf-8') as file:
                content =file.read()
                self.editor.clear()
                self.editor.setText(content)

        except:
            pass
    def saveFile(self):
        global url
        try:
            if textChanged == True:
                if url != "":
                    content =self.editor.toPlainText()
                    with open(url[0],'w',encoding='utf-8') as file:
                        file.write(content)
                else:
                    url = QFileDialog.getSaveFileName(self,"Dosyayi Kayit Et","","Txt Files (*.txt)")
                    content2= self.editor.toPlainText()
                    with open(url[0],'w', encoding='utf-8') as file2:
                        file2.write(content2)


        except:
            pass
    def exitFile(self):
        global url
        try:
         if textChanged == True:
             mbox= QMessageBox.information(self,"Dikkat","Dosyayi kayit etmek istiyor musunuz?",QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

             if mbox == QMessageBox.Save:
                 if url != "":
                     content = self.editor.toPlainText()
                     with open(url[0],w, encoding='utf-8') as file:
                         file.write(content)
                 else:
                     url = QFileDialog.getSaveFileName(self,"Save File","","Txt files(*.txt)")
                     content2= self.editor.toPlainText()
                     with open(url[0],'w',encoding='utf-8') as file2:
                         file2.write(content2)
             elif mbox == QMessageBox.No:
                qApp.quit()
         else:
            qApp.quit()

        except:
            pass
###########################################Menu bitis#########################################################################





def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec())
if __name__=='__main__':
    main()

