
import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
#     QTextEdit, QGridLayout, QApplication)
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
#定义对话框   
        self.title = QLabel('OPEN FOLDER')
        self.titleEdit = QLineEdit()
        self.OPENFIlE_Button=QPushButton("打开")

        self.Key_word = QLabel("KEYword")
        self.Key_word_input=QLineEdit()
        self.after_word = QLabel("SOLL")
        self.after_word_input=QLineEdit()
        self.key_word_do=QPushButton("Replace")
        self.key_word_pos=QLabel("Soll_position after KEYword[0,1,2...]")
        self.key_word_pos_input=QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

 #添加对话框
        grid.addWidget(self.title, 1, 0)
        grid.addWidget(self.titleEdit, 1, 1,1,3)
        grid.addWidget(self.OPENFIlE_Button, 1, 4)
        grid.addWidget(self.Key_word,3,0) 
        grid.addWidget(self.Key_word_input,3,1)
        grid.addWidget(self.after_word,3,2)
        grid.addWidget(self.after_word_input,3,3)
        grid.addWidget(self.key_word_do,4,4)
        grid.addWidget(self.key_word_pos,4,0,1,3)
        grid.addWidget(self.key_word_pos_input,4,3)
#设置初始值
        self.Key_word_input.setText("QBZ1")
        self.after_word_input.setText("0.02")
        self.key_word_pos_input.setText("2")

        # self.kword=self.Key_word_input.text()
        # self.kafter=self.after_word_input.text()
        # position=self.key_word_pos_input.text()
        # self.pos=int(position)

        self.openfile_name=[]
        self.OPENFIlE_Button.clicked.connect(self.openfile)
        self.key_word_do.clicked.connect(self.loopfile)
        self.setLayout(grid)

#创建工作窗口      
        self.setGeometry(500, 200,500, 400)
        self.setWindowTitle("Transfer")    
        self.show()
    
    def openfile(self):
#QFileDialog::getOpenFileName(this,tr("Open Image"), "/home/jana", tr("Image Files (*.png *.jpg *.bmp)"));
        # self.openfile_name = QFileDialog.getOpenFileName(self,'Select Files','','tir files(*.tir)')     
        self.openfile_name = QFileDialog.getOpenFileName(self,'Select Files','','')   
        self.titleEdit.setText(str(self.openfile_name[0]))
#路径和名字
        self.dirname=os.path.dirname(self.openfile_name[0])
        self.filenames=os.listdir(self.dirname)
        path=self.dirname+'/'+"update"
        if not os.path.exists(path):
            os.makedirs(path)
        self.newdirname=path

    def loopfile(self):

        self.kword=self.Key_word_input.text()
        self.kafter=self.after_word_input.text()
        position=self.key_word_pos_input.text()
        self.pos=int(position)

        for f in self.filenames:
            self.changedate(f)


        widget=QWidget()
        QMessageBox.information(widget,'Success','Finish transfer')
        sys.exit()

    def changedate(self,filename):
        try: 
            changedate_f=open(self.dirname+"/"+filename,"r")
        except:
            self.openfile()

#修改数据
        changedate_date=[]
        changedate_date=changedate_f.readlines()
        linenum=len(changedate_date)
        

        new_docu=open(self.newdirname+"/"+filename,"w")

        for i in range(0,linenum):
            if changedate_date[i]!="":
                if changedate_date[i].split()[0]==self.kword: 
#关键位置                    
                    # changedate_date[i]=changedate_date[i].replace(changedate_date[i].split()[self.key_po],self.kafter)
                    changedate_date[i]=changedate_date[i].replace(changedate_date[i].split()[self.pos],self.kafter)
                    # changedate_date[i]=changedate_date[i].replace(self.kword,"success")
            new_docu.write(changedate_date[i])
        # for line in self.changedate_date:
        #     if line.split()[0]==kword:
        #         print("I catch you!")
        #         line.split()[1]="00000"
        #     new_docu.write(line)
        # print("finished")

        new_docu.close()
        changedate_f.close()




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())