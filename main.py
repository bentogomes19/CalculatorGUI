import sys
from PyQt6 import QtWidgets, QtCore
from UI_Calculator import Ui_MainWindow

class MyCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.ui = Ui_MainWindow() # Criando o objeto
        self.ui.setupUi(self)
        
        # Variáveis para armazenar os valores digitado
        self.operacao = None
        self.ultimo_valor = None
        
        # Criando as conexões com os botões numéricos
        self.ui.btn_number0.clicked.connect(lambda: self.on_Click_Display(0))
        self.ui.btn_number1.clicked.connect(lambda: self.on_Click_Display(1))
        self.ui.btn_number2.clicked.connect(lambda: self.on_Click_Display(2))
        self.ui.btn_number3.clicked.connect(lambda: self.on_Click_Display(3))
        self.ui.btn_number4.clicked.connect(lambda: self.on_Click_Display(4))
        self.ui.btn_number5.clicked.connect(lambda: self.on_Click_Display(5))
        self.ui.btn_number6.clicked.connect(lambda: self.on_Click_Display(6))
        self.ui.btn_number7.clicked.connect(lambda: self.on_Click_Display(7))
        self.ui.btn_number8.clicked.connect(lambda: self.on_Click_Display(8))
        self.ui.btn_number9.clicked.connect(lambda: self.on_Click_Display(9))
        
        # Criando a conexão com o botão AC clear (irá limpar a tela do display)
        self.ui.btn_clear.clicked.connect(self.ClearDisplay)
        
        # Conectando os botões das operações aritméticas
        self.ui.btn_plus.clicked.connect(lambda: self.Somar())
        self.ui.btn_minus.clicked.connect(lambda: self.Subtrair())
        
        
        self.ui.btn_equals.clicked.connect(self.Calcular)
        

    # funções
    def on_Click_Display(self, number):
        current_text = self.ui.Display.text() # Coleta o texto do display e armazena na variável 'current_text'
        new_text = current_text + str(number)
        self.ui.Display.setText(new_text)
    
    
    def ClearDisplay(self):
        self.ui.Display.clear()
        self.ultimo_valor = None
    
    
    def Somar(self):
        current_text = self.ui.Display.text()
        if current_text:
            self.ultimo_valor = float(current_text)
            self.ui.Display.clear()
            self.operacao = 'soma'
        
        
    def Subtrair(self):
        current_text = self.ui.Display.text()
        if current_text:
            self.ultimo_valor = float(current_text)
            self.ui.Display.clear()
            self.operacao = 'subtração'
        pass
    
    def Multiplicar(self):
        pass
    
    def Dividir(self):
        pass
    
    
    def Calcular(self):
        current_text = self.ui.Display.text()
        if self.operacao == 'soma' and self.ultimo_valor is not None:
            novo_valor = float(current_text) if current_text else 0
            resultado = self.ultimo_valor + novo_valor
            self.ui.Display.setText(str(resultado))
            self.ultimo_valor = resultado
            self.operacao = None
        
        if self.operacao == 'subtração' and self.ultimo_valor is not None:
            novo_valor = float(current_text) if current_text else 0
            resultado = self.ultimo_valor - novo_valor
            self.ui.Display.setText(str(resultado))
            self.ultimo_valor = resultado
            self.operacao = None
    



app = QtWidgets.QApplication(sys.argv)

window = MyCalculator()
window.show()
sys.exit(app.exec())
    
    

