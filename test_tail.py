import unittest
import tail


class TestTailClass(unittest.TestCase):

    def test_deve_retornar_as_dez_ultimas_linhas_por_default(self):
        t = tail.Tail('tail bla.txt')

        linhas_esperadas = ["Just a little bit, just a little bit, just a little bit, (baby I'm wait for you) longer, longer (won't you wait)\n",
                            'Just a little bit, just a little bit, just a little bit, longer, longer (if you wait)\n',
                            'Just a little bit, just a little bit, just a little bit, longer.\n', '\n',
                            'Just a little bit\n', 'just a little bit\n', 'just a little bit\n', 'just a little bit\n',
                            'Just a little bit\n', 'Just a little bit\n']

        self.assertEqual(t.le_comando(), linhas_esperadas)

    def test_deve_retornar_as_oito_ultimas_linhas_do_arquivo_bla_txt(self):
        t = tail.Tail('tail -n 8 bla.txt')

        linhas_esperadas = ['Just a little bit, just a little bit, just a little bit, longer.\n', '\n',
                            'Just a little bit\n', 'just a little bit\n', 'just a little bit\n', 'just a little bit\n',
                            'Just a little bit\n', 'Just a little bit\n']

        self.assertEqual(t.le_comando(), linhas_esperadas)

    def test_deve_retornar_as_oito_ultimas_linhas_e_esperar_conteudo_novo(self):
        t = tail.Tail('tail -n 8 -f bla.txt')

        self.assertRaises(TypeError, t.le_comando)

    def test_deve_retornar_especifique_um_arquivo_quando_nao_passar_argumentos_para_tail(self):
        t = tail.Tail('tail')

        self.assertEqual(t.le_comando(), 'Especifique um Arquivo')

    def test_deve_retornar_flag_invalida_caso_passe_z_como_flag(self):
        t = tail.Tail('tail -z bla.txt')

        self.assertEqual(t.le_comando(), 'Flag Invalida')

    def test_deve_retornar_parametro_invalido_quando_passar_k_como_numero_de_linhas(self):
        t = tail.Tail('tail -n k bla.txt')

        self.assertEqual(t.le_comando(), 'Parametro Invalido')

    def test_deve_retornar_flag_invalida_quando_passar_o_numero_de_linhas_sem_flags(self):
        t = tail.Tail('tail 15 bla.txt')

        self.assertEqual(t.le_comando(), 'Flag Invalida')

    def test_deve_retornar_comando_invalido_quando_passar_head_como_comando(self):
        t = tail.Tail('head bla.txt')

        self.assertEqual(t.le_comando(), 'Comando Invalido')

if __name__ == '__main__':
    unittest.main()
