import unittest
import sys
from tail import le_comando


class TestTailClass(unittest.TestCase):

    def test_deve_retornar_as_dez_ultimas_linhas_por_default(self):
        sys.argv = ['tail.py', 'bla.txt']

        linhas_esperadas = ["Just a little bit, just a little bit, just a little bit, (baby I'm wait for you) longer, longer (won't you wait)\n",
                            'Just a little bit, just a little bit, just a little bit, longer, longer (if you wait)\n',
                            'Just a little bit, just a little bit, just a little bit, longer.\n', '\n',
                            'Just a little bit\n', 'just a little bit\n', 'just a little bit\n', 'just a little bit\n',
                            'Just a little bit\n', 'Just a little bit\n']

        self.assertEqual(le_comando(), linhas_esperadas)

    def test_deve_retornar_as_oito_ultimas_linhas_do_arquivo_bla_txt(self):
        sys.argv = ['tail.py', '-n', '8', 'bla.txt']

        linhas_esperadas = ['Just a little bit, just a little bit, just a little bit, longer.\n', '\n',
                            'Just a little bit\n', 'just a little bit\n', 'just a little bit\n', 'just a little bit\n',
                            'Just a little bit\n', 'Just a little bit\n']

        self.assertEqual(le_comando(), linhas_esperadas)

    def test_deve_retornar_especifique_um_arquivo_quando_nao_passar_argumentos_para_tail(self):
        sys.argv = ['tail.py']

        self.assertEqual(le_comando(), 'Especifique um Arquivo')

    def test_deve_retornar_flag_invalida_caso_passe_z_como_flag(self):
        sys.argv = ['tail.py', '-z', 'bla.txt']

        self.assertEqual(le_comando(), 'Flag Invalida')

    def test_deve_retornar_parametro_invalido_quando_passar_k_como_numero_de_linhas(self):
        sys.argv = ['tail.py', '-n', 'k', 'bla.txt']

        self.assertEqual(le_comando(), 'Parametro Invalido')

    def test_deve_retornar_flag_invalida_quando_passar_o_numero_de_linhas_sem_flags(self):
        sys.argv = ['tail.py', '15', 'bla.txt']

        self.assertEqual(le_comando(), 'Flag Invalida')

    def test_deve_retornar_arquivo_inexistente_quando_passar_arquivo_ble_txt(self):
        sys.argv = ['tail.py', 'ble.txt']

        self.assertEqual(le_comando(), 'Arquivo Inexistente')

    def test_deve_retornar_todo_o_conteudo_do_arquivo_bla_txt_de_tras_para_frente(self):
        sys.argv = ['tail.py', '-r', 'bla2.txt']

        self.assertEqual(le_comando(), ['No longer have to lie about us.\n', "And I know I say it often but I can't wait, till we\n",
                                        "and when you call me I don't wanna hang up.\n", 'When I walk around all I want is she touch,\n',
                                        'no longer have to lie about us (whoa ooooo).\n',
                                        'And I know your waiting patiently for that day, when we\n',
                                        "How do I tell and then I'm fallen in love (how do I tell my baby).\n", "So please don't say you wanna give up,\n"])

if __name__ == '__main__':
    unittest.main()
