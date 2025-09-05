'''Tela em Kivy'''
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")
# 'GUI' é a variavel que vai carregar o arquivo em kivy que vai carregar na tela.




class MeuApp(App):
    '''
    MeuApp é classe para criar a janela em Kivy
    '''
    def build(self):
        '''
        As funcoes de inicializar na classe,
        que e forma o app.
        self: padrão de todas as classes.
        return GUI: vai carregar a janela.
        '''
        return  GUI

MeuApp().run()
# O  método 'run()'  vai carregar a classe 'MeuApp()'
