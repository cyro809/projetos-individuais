import unittest
import head


class TestHeadClass(unittest.TestCase):

    def test_confere_argumentos_deve_atribuir_valores_corretos_aos_atributos_caso_nao_tenha_flags(self):
        h = head.Head('head bla.txt')

        tamanho_esperado = 1
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10

        h.confere_argumentos()

        self.assertEqual(len(h.argumentos), tamanho_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_confere_argumentos_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_n(self):
        h = head.Head('head -n 15 bla.txt')

        tamanho_argumentos_esperado = 3
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 15

        h.confere_argumentos()

        self.assertEqual(len(h.argumentos), tamanho_argumentos_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_imprime_resultado_deve_atribuir_as_linhas_a_serem_impressas_corretamente_caso_nao_tenha_flags(self):
        h = head.Head('head bla.txt')

        linhas_esperadas = ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                            'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                            "I know I'm asking for allot, but just trust.\n",
                            'You say that things getting old, sneaking round, creeping and love on the low\n',
                            'But baby girl\n', "I can't wait till it's officially us,\n",
                            "I can't wait to let them know about us.\n", '\n']

        h.confere_argumentos()

        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

    def test_deve_imprimir_as_8_primeiras_linhas_do_arquivo_bla_txt(self):
        h = head.Head('head -n 8 bla.txt')

        linhas_esperadas = ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                            'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                            "I know I'm asking for allot, but just trust.\n",
                            'You say that things getting old, sneaking round, creeping and love on the low\n',
                            'But baby girl\n', "I can't wait till it's officially us,\n"]

        h.confere_argumentos()

        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

    def test_deve_retornar_arquivo_inexistente_caso_o_arquivo_nao_exista(self):
        h = head.Head('head ble.txt')

        self.assertRaises(IOError, h.confere_argumentos)



if __name__ == '__main__':
    unittest.main()
