import unittest
import head


class TestHeadClass(unittest.TestCase):

    def test_head_deve_atribuir_valores_corretos_aos_atributos_caso_nao_tenha_flags(self):
        h = head.Head()

        h.input_string = 'head bla.txt'
        tamanho_esperado = 1
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10
        
        h.confere_argumentos()
        
        self.assertEqual(len(h.argumentos), tamanho_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_head_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_n(self):
        h = head.Head()

        h.input_string = 'head -n 15 bla.txt'
        tamanho_argumentos_esperado = 3
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 15
        
        h.confere_argumentos()
        
        self.assertEqual(len(h.argumentos), tamanho_argumentos_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

if __name__ == '__main__':
    unittest.main()
