import unittest
import sys
from head import le_comando


class TestHeadClass(unittest.TestCase):

    def test_le_comando_deve_retornar_as_10_primeiras_linhas_por_default(self):
        sys.argv = ['head.py', 'bla.txt']

        self.assertEqual(le_comando(), ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                                                      'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                                                      "I know I'm asking for allot, but just trust.\n",
                                                      'You say that things getting old, sneaking round, creeping and love on the low\n',
                                                      'But baby girl\n', "I can't wait till it's officially us,\n",
                                                      "I can't wait to let them know about us.\n", '\n'])

    def test_deve_imprimir_as_8_primeiras_linhas_do_arquivo_bla_txt(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando(), ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                                                           'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                                                           "I know I'm asking for allot, but just trust.\n",
                                                           'You say that things getting old, sneaking round, creeping and love on the low\n',
                                                           'But baby girl\n', "I can't wait till it's officially us,\n"])

    def test_deve_retornar_arquivo_inexistente_caso_o_arquivo_nao_exista(self):
        sys.argv = ['head.py', 'ble.txt']

        self.assertEqual(le_comando(), 'Arquivo inexistente')

    def test_deve_retornar_as_dez_primeiras_linhas_caso_passe_flag_n_sem_o_numero_de_linhas(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head -n bla.txt'), ['Baby I know,\n', "When we started out there were things you didn't know,\n",
                                                         'But baby girl,\n', 'We got a lot of things we need to discuss\n',
                                                         "I know I'm asking for allot, but just trust.\n",
                                                         'You say that things getting old, sneaking round, creeping and love on the low\n',
                                                         'But baby girl\n', "I can't wait till it's officially us,\n",
                                                         "I can't wait to let them know about us.\n", '\n'])

    def test_deve_retornar_parametro_invalido_quando_passar_uma_letra_no_lugar_de_numero_para_quantidade_de_linhas_a_serem_impressas(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head -n K bla.txt'), u'Parametro invalido. Especifique um numero')

    def test_deve_retornar_especifique_um_arquivo_caso_o_comando_head_seja_passado_sem_argumentos(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head'), u'Especifique um Arquivo')

    def test_deve_retornar_flag_inexistente_quando_passar_z_como_flag(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head -z bla.txt'), u'Flag Desconhecida')

    def test_deve_retornar_parametro_invalido_caso_nao_passe_um_numero_no_lugar_da_flag(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head 15 bla.txt'), u'Flag Desconhecida')

    def test_deve_retornar_flag_desconhecida_ao_passar_z_como_flag_e_especificar_numero_de_linhas(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('head -z 15 bla.txt'), u'Flag Desconhecida')

    def test_deve_retornar_comando_desconhecido_caso_nao_passe_head_como_comando(self):
        sys.argv = ['head.py', '-n', '8', 'bla.txt']

        self.assertEqual(le_comando('tail bla.txt'), u'Comando Invalido')

if __name__ == '__main__':
    unittest.main()
