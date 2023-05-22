import unittest
from sofia import *

class TestSofia(unittest.TestCase):
    def test_treinar_robo_array(self):
        lista_completa = treinar_robo()
        self.assertIsInstance(lista_completa, list)

    def test_treinar_robo_tamanho(self):
        lista_completa = treinar_robo()
        self.assertTrue(len(lista_completa) > 0)
    
    def test_treinar_robo_conteudo(self):
        lista_completa = treinar_robo()
        self.assertTrue("Bom dia! Como posso te ajudar?" in lista_completa)
    
    def test_input_usuario(self):
        texto = "O que foi o renascimento"
        self.assertTrue(input_usuario(texto) == texto)

if __name__ == "__main__":
    unittest.main()