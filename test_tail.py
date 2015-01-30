import unittest
import tail


class TestTailClass(unittest.TestCase):

    def test_le_comando_deve_atribuir_valores_corretos_aos_atributos_caso_nao_tenha_flags(self):
        t = tail.Tail('tail bla.txt')

        tamanho_esperado = 1
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10

        t.le_comando()

        self.assertEqual(len(t.argumentos), tamanho_esperado)
        self.assertEqual(t.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(t.nome_arquivo, nome_arquivo_esperado)

    def test_le_comando_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_n(self):
        t = tail.Tail('tail -n 15 bla.txt')

        tamanho_argumentos_esperado = 3
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 15

        t.le_comando()

        self.assertEqual(len(t.argumentos), tamanho_argumentos_esperado)
        self.assertEqual(t.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(t.nome_arquivo, nome_arquivo_esperado)

    def test_le_comando_deve_atribuir_valores_corretos_aos_atributos_caso_tenha_flag_f(self):
        t = tail.Tail('tail -f bla.txt')

        tamanho_argumentos_esperado = 2
        nome_arquivo_esperado = 'bla.txt'
        numero_de_linhas_esperada = 10

        t.le_comando()

        self.assertEqual(len(t.argumentos), tamanho_argumentos_esperado)
        self.assertEqual(t.num_de_linhas, numero_de_linhas_esperada)
        self.assertEqual(t.nome_arquivo, nome_arquivo_esperado)

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

    # def test_imprime_resultado_deve_atribuir_as_linhas_a_serem_impressas_corretamente_caso_tenha_a_flag_f(self):
    #     t = tail.Tail()

    #     t.input_string = 'tail -f bla2.txt'
    #     nova_linha_esperada = 'nova linha'
    #     linhas_esperadas = ["Just a little bit, just a little bit, just a little bit, (baby I'm wait for you) longer, longer (won't you wait)\n",
    #                         'Just a little bit, just a little bit, just a little bit, longer, longer (if you wait)\n',
    #                         'Just a little bit, just a little bit, just a little bit, longer.\n', '\n',
    #                         'Just a little bit\n', 'just a little bit\n', 'just a little bit\n', 'just a little bit\n',
    #                         'Just a little bit\n', 'Just a little bit\n', nova_linha_esperada]

    #     t.le_comando()

    #     t.nome_arquivo = 'bla2.txt'
    #     t.flag = '-f'
    #     t.arquivo = open(t.nome_arquivo, 'r+')
    #     t.arquivo.seek(0, 2)
    #     t.arquivo.write('nova linha')
    #     t.arquivo.close()

    #     self.assertEqual(t.linhas_a_imprimir, linhas_esperadas)


if __name__ == '__main__':
    unittest.main()
