import unittest
from unittest.mock import MagicMock
from src.CategoriaIdade import classificar_nadador

class TestClassificacaoComMock(unittest.TestCase):
    def test_classificar_nadador_com_mock(self):
        mock_servico_idade = MagicMock()
        mock_servico_idade.buscar_idade.return_value = 15
        resultado = classificar_nadador(mock_servico_idade, id_nadador=123)
        self.assertEqual(resultado, "Juvenil B")
        mock_servico_idade.buscar_idade.assert_called_with(123)
        mock_servico_idade.buscar_idade.return_value = 78
        resultado2= classificar_nadador(mock_servico_idade, id_nadador=424)
        self.assertEqual(resultado2, "Sênior")
        mock_servico_idade.buscar_idade.assert_called_with(424)

if __name__ == '__main__':
    unittest.main()
