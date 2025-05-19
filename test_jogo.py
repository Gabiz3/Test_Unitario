
import unittest
from jogo import calcular_numeros


class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(calcular_numeros(5, 3, '+'), 8)

    def test_subtracao(self):
        self.assertEqual(calcular_numeros(10, 4, '-'), 6)

    def test_multiplicacao(self):
        self.assertEqual(calcular_numeros(7, 6, '*'), 42)

    def test_divisao(self):
        self.assertEqual(calcular_numeros(20, 4, '/'), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calcular_numeros(10, 0, '/')

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calcular_numeros(10, 2, '%')

if __name__ == '__main__':
    unittest.main()
