import unittest
import head


class TestHeadClass(unittest.TestCase):

    def test_le_comando_deve_atribuir_valores_corretos_aos_atributos_caso_nao_tenha_flags(self):
        h = head.Head('head bla.txt')

        tamanho_esperado = 1
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10

        h.le_comando()

        self.assertEqual(len(h.argumentos), tamanho_esperado)
        self.assertEqual(h.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(h.nome_arquivo, nome_arquivo_esperado)

    def test_le_comando_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_n(self):
        h = head.Head('head -n 15 bla.txt')

        tamanho_argumentos_esperado = 3
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 15

        h.le_comando()

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

        h.le_comando()

        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

    def test_deve_imprimir_as_8_primeiras_linhas_do_arquivo_bla_txt(self):
        h = head.Head('head -n 8 bla.txt')

        linhas_esperadas = ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                            'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                            "I know I'm asking for allot, but just trust.\n",
                            'You say that things getting old, sneaking round, creeping and love on the low\n',
                            'But baby girl\n', "I can't wait till it's officially us,\n"]

        h.le_comando()

        self.assertEqual(h.linhas_a_imprimir, linhas_esperadas)

    def test_deve_retornar_arquivo_inexistente_caso_o_arquivo_nao_exista(self):
        h = head.Head('head ble.txt')

        with self.assertRaises(IOError) as context:
            h.le_comando()

        excecao = context.exception
        self.assertEqual(excecao.strerror, 'No such file or directory')
        self.assertEqual(excecao.errno, 2)

    def test_deve_retornar_as_dez_primeiras_linhas_caso_passe_flag_n_sem_o_numero_de_linhas(self):
        h = head.Head('head -n bla.txt')

        with self.assertRaises(TypeError) as context:
            h.le_comando()

        excecao = context.exception

        self.assertEqual(excecao.message, 'coercing to Unicode: need string or buffer, NoneType found')

    def test_deve_retornar_parametro_invalido_quando_passar_uma_letra_no_lugar_de_numero_para_quantidade_de_linhas_a_serem_impressas(self):
        h = head.Head('head -n K bla.txt')

        with self.assertRaises(ValueError) as context:
            h.le_comando()

        excecao = context.exception

        self.assertEqual(excecao.message, "invalid literal for int() with base 10: 'K'")

    def test_deve_retornar_especifique_um_arquivo_caso_o_comando_head_seja_passado_sem_argumentos(self):
        h = head.Head('head')

        self.assertEqual(h.le_comando(), u'Especifique um Arquivo')

    def test_deve_retornar_flag_inexistente_quando_passar_z_como_flag(self):
        h = head.Head('head -z bla.txt')

        with self.assertRaises(TypeError) as context:
            h.le_comando()

        excecao = context.exception

        self.assertEqual(excecao.message, 'coercing to Unicode: need string or buffer, NoneType found')

    def test_deve_retornar_parametro_invalido_caso_nao_passe_um_numero_no_lugar_da_flag(self):
        h = head.Head('head 15 bla.txt')

        with self.assertRaises(TypeError) as context:
            h.le_comando()

        excecao = context.exception

        self.assertEqual(excecao.message, 'coercing to Unicode: need string or buffer, NoneType found')

if __name__ == '__main__':
    unittest.main()
