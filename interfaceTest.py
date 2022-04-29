import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from interface import Ui_Interface
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHeaderView
from db_tool import DB
import db_tool

# 数据库连接
db = None

class InterfaceTest(QMainWindow, Ui_Interface):
    def __init__(self,parent=None):
        super(InterfaceTest, self).__init__(parent)
        self.setupUi(self)
        #绑定事件
        self.btn_add.clicked.connect(self.add)
        self.btn_search.clicked.connect(self.query_all)

    def add(self):
 #       self.db = DB(host='192.168.224.128', port=3306, db='interfaces', user='root', passwd='123456')
        i_name = self.le_interName.text()
        i_addr = self.le_addr.text()
        if ("" != i_name and "" != i_addr):
            db.insert(i_name, i_addr)
            self.le_interName.setText("")
            self.le_addr.setText("")
        self.query_all()
 #       self.db.close()
    
    def query_all(self):
        # 建立模型，加载数据
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["编号","接口名称","接口地址","描述"])
        datas = db.query()
      #  print(datas)
        for i,line_data in enumerate(datas):
            for j,item_data in enumerate(line_data.values()):
                item = QStandardItem(str(item_data)) if item_data is not None else QStandardItem("")
                model.setItem(i,j,item)
        self.tv_interfaces.setModel(model)
        # 隐藏左侧自动生成列
        self.tv_interfaces.verticalHeader().hide()
        # 水平均匀填充
        self.tv_interfaces.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
if __name__ == '__main__':
    
    #pyqt5程序需要该对象，sys.argv为命令行参数，保证可以启动
    app = QApplication(sys.argv)
    #连接数据库
    db = DB(host='192.168.224.128', port=3306, db='interfaces', user='root', passwd='123456')
    #初始化界面
    it = InterfaceTest()
    #显示窗口
    it.show()
    #程序退出
    sys.exit(app.exec_())
    db.close()
'''
    w = QWidget()
    w.setWindowTitle("test")
    w.show()
'''
    
    
