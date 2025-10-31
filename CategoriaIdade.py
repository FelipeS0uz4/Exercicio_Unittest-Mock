import unittest

def obter_categoria(idade):
    if idade >= 5 and idade <= 7:
        categoria = 'Infantil A'
    elif idade >= 8 and idade <=10:
        categoria = 'Infantil B'
    elif idade >= 11 and idade <=13:
        categoria = 'Juvenil A'
    elif idade >= 14 and idade <=17:
        categoria = 'Juvenil B'
    elif idade >= 18:
        categoria = 'Sênior'
    else:
        categoria = 'Idade fora das categorias'
    return categoria

class TestObterCategoria(unittest.TestCase):
    def test_idade_fora_da_categoria(self):
        self.assertEqual(obter_categoria(4), "Idade fora das categorias")
    
    def test_infantil_a(self):
        self.assertEqual(obter_categoria(5), "Infantil A")
        self.assertEqual(obter_categoria(7), "Infantil A")

    def test_infantil_b(self):
        self.assertEqual(obter_categoria(8), "Infantil B")
        self.assertEqual(obter_categoria(10), "Infantil B")

    def test_juvenil_a(self):
        self.assertEqual(obter_categoria(11), "Juvenil A")
        self.assertEqual(obter_categoria(13), "Juvenil A")

    def test_juvenil_b(self):
        self.assertEqual(obter_categoria(14), "Juvenil B")
        self.assertEqual(obter_categoria(17), "Juvenil B")

    def test_senior(self):
        self.assertEqual(obter_categoria(18), "Sênior")
        self.assertEqual(obter_categoria(30), "Sênior")

def classificar_nadador(servico_idade, id_nadador):
    idade = servico_idade.buscar_idade(id_nadador)
    return obter_categoria(idade)


if __name__ == "__main__":
    unittest.main()