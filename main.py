import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from UI_Calculator import Ui_MainWindow
# Calculator.exe
class MyCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.ui = Ui_MainWindow() # Criando o objeto
        self.ui.setupUi(self) # setupUi configura todos os componentes da interface de usuário, conectando widgets aos atributos e métodos da instância da classe
        
        # Atributos para armazenar os valores digitado
        self.operacao = None # atributo para coletar a operação ('+', '-', '*')
        self.ultimo_valor = None # atributo para armazenar o ultimo valor informado 
        self.sinal = None # coleta o sinal 
        self.resultado = None # coleta o resultado da expressão
        
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
        self.ui.btn_plus.clicked.connect(lambda: self.Operacao('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.Operacao('-'))
        self.ui.btn_mult.clicked.connect(lambda: self.Operacao('*'))    
        self.ui.btn_division.clicked.connect(lambda: self.Operacao('/'))    
        
        # botão =
        self.ui.btn_equals.clicked.connect(self.Calcular)
        # botão porcentagem
        self.ui.btn_perc.clicked.connect(self.Porcentagem)
        # Botão decimal
        self.ui.btn_decimal.clicked.connect(self.decimal)
        # Botão Mudar Sinal
        self.ui.btn_plus_minus.clicked.connect(self.MudarSinal)

    # funções Desenvolvidas

    # Método para ajustar o tamanho da fonte do display a medida que o usuário vá inserindo mais numeros, ou se a expressão
    # aumenta a medida da quantidade de inputs do usuaŕio, o tamanho da fonte vai diminuindo
    # Método a ser aplicado em todos os outros métodos de operação
    def ajustar_fonte(self): 
        current_text = self.ui.Display.text() # Armazena o texto do Display (QLineEdit)
        text_length = len(current_text) # variável para armazenar o tamanho da variavél "current_text"
        
        if text_length > 7: 
            self.ui.Display.setFont(QFont("SF Pro Display", 40))
            if text_length > 9:
                self.ui.Display.setFont(QFont('SF Pro Display', 35))
                if text_length > 13:
                    self.ui.Display.setFont(QFont('SF Pro Display', 25))
                    if text_length > 15:
                        self.ui.Display.setFont(QFont('SF Pro Display', 22))
        else:
            self.ui.Display.setFont(QFont('SF Pro Display', 50))
        
    def on_Click_Display(self, number):
        current_text = self.ui.Display.text() # Coleta o texto do display e armazena na variável 'current_text'
        new_text = current_text + str(number)
        self.ui.Display.setText(new_text)
        
        self.ajustar_fonte()
    
    # Método para limpar o display da calculadora, define todos os atributos como None e limpa o diplay com o método .clear()
    def ClearDisplay(self):
        self.ui.Display.clear()
        self.ultimo_valor = None
        self.sinal = None    
        self.operacao = None
    
    # Método Operação -> Irá coletar os operadores e ira fazer a concatenação.
    # exemplo: Display: 25+ ... 12+45....
    # ele faz a junção do operando com o operador permitindo a visualização da expressão no display
    # é feito uma verificação caso se o texto anterior seja um operador, não permitindo entradas do tipo :> 25++
    def Operacao(self, operador):
        current_text = self.ui.Display.text()
        
        if current_text and current_text[-1] not in ['+', '-', '*', '/']:
            self.sinal = operador # o atributo recebe o operador
            new_text = current_text + self.sinal # novo texto concatena o texto anterior informado com o sinal selecionado
            self.ui.Display.setText(new_text) # atualiza o valor no display
        else:
            pass
        
        self.ajustar_fonte()
           
    # Método Porcentagem -> para calcular a porcentagem de um número apenas
    # O input do usuário será um número qualquer, e após isso, a selecionar o botão de porcentagem o método irá
    # calcular este numero informado em porcentagem -> EXEMPLO: Display: 100 -> input: % -> Display: 1.0
    def Porcentagem(self):
        current_text = self.ui.Display.text()
        
        if current_text:
            try:
                percentual = float(current_text) # atualiza o valor do display para valor flutuante
                if self.ultimo_valor is not None:  # caso o ultimo valor seja vazio, ele irá fazer o calculo da porcentagem
                    resultado = self.ultimo_valor / 100 # calculo de porcentagem
                    self.ui.Display.setText(str(resultado))
                else:
                    resultado = percentual / 100
                    self.ui.Display.setText(str(resultado))
            except ValueError:
                self.ui.Display.setText("Error")
        self.ajustar_fonte()
        
    # Método Decimal -> para inserir '.' no display permitindo calculos com valores decimais
    def decimal(self):
        current_text = self.ui.Display.text()
        
        if current_text and current_text[-1] not in ['+', '-', '*', '/', '.']:
            self.ponto = '.'
            new_text = current_text + self.ponto
            self.ui.Display.setText(new_text)
        else:
            pass
        self.ajustar_fonte()
    
    def MudarSinal(self):
        current_text = self.ui.Display.text()
        
        if current_text:
            try:
                new_value = -float(current_text)
                self.ui.Display.setText(str(new_value))
            except ValueError:
                self.ui.Display.setText("Error")
        self.ajustar_fonte()
    
    def Calcular(self):
        current_text = self.ui.Display.text()
        
        try:
            resultado = eval(current_text)
            self.ui.Display.setText(str(resultado))
            self.ultimo_valor = resultado
        except Exception as e:
            self.ui.Display.setText("Error")
            
        self.ajustar_fonte()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyCalculator()
    window.show()
    sys.exit(app.exec())
    
    

