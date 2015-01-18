import unittest
import head


class TestHeadClass(unittest.TestCase):

    def test_confere_argumentos_deve_atribuir_valores_corretos_aos_atributos_caso_nao_tenha_flags(self):
        h = head.Head()

        h.input_string = 'head bla.txt'
        tamanho_esperado = 1
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10
        
        h.confere_argumentos()
        
        self.assertEqual(len(h.argumentos), tamanho_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_confere_argumentos_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_n(self):
        h = head.Head()

        h.input_string = 'head -n 15 bla.txt'
        tamanho_argumentos_esperado = 3
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 15
        
        h.confere_argumentos()
        
        self.assertEqual(len(h.argumentos), tamanho_argumentos_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_imprimi_resultado_deve_atribuir_as_linhas_a_serem_impressas_corretamente_caso_nao_tenha_flags(self):
        h = head.Head()

        h.input_string = 'head bla.txt'
        linhas_esperadas = ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                            'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                            "I know I'm asking for allot, but just trust.\n",
                            'You say that things getting old, sneaking round, creeping and love on the low\n',
                            'But baby girl\n', "I can't wait till it's officially us,\n",
                            "I can't wait to let them know about us.\n", '\n']
        
        h.confere_argumentos()
        
        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

    def test_imprimi_resultado_deve_atribuir_as_linhas_a_serem_impressas_corretamente_caso_tenha_a_flag_n(self):
        h = head.Head()

        h.input_string = 'head -n 8 bla.txt'
        linhas_esperadas = ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                            'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                            "I know I'm asking for allot, but just trust.\n",
                            'You say that things getting old, sneaking round, creeping and love on the low\n',
                            'But baby girl\n', "I can't wait till it's officially us,\n"]
        
        h.confere_argumentos()
        
        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

if __name__ == '__main__':
    unittest.main()
