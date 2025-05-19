# Test_Unitario

Este repositório contém um conjunto de testes unitários para uma função de calculadora chamada calcular_numeros, que realiza operações matemáticas básicas. Os testes foram implementados usando o framework unittest do Python.

Funcionalidades Testadas
A suíte de testes verifica os seguintes aspectos da função calcular_numeros:

Operações matemáticas básicas:

Adição (+)

Subtração (-)

Multiplicação (*)

Divisão (/)

Tratamento de casos especiais:

Divisão por zero

Operador inválido

Estrutura do Código
O arquivo de testes test_calculadora.py contém uma classe TestCalculadora que herda de unittest.TestCase e inclui os seguintes métodos de teste:

test_adicao: Testa a operação de adição

test_subtracao: Testa a operação de subtração

test_multiplicacao: Testa a operação de multiplicação

test_divisao: Testa a operação de divisão

test_divisao_por_zero: Verifica se a função trata divisão por zero corretamente

test_operacao_invalida: Verifica se a função trata operadores inválidos corretamente

Pré-requisitos
Python 3.x

Módulo unittest (já incluído na biblioteca padrão do Python)

Como Executar os Testes:
Certifique-se de que o arquivo jogo.py (que contém a função calcular_numeros) está no mesmo diretório

Execute o seguinte comando no terminal:

python test_calculadora.py
Você verá a saída dos testes, indicando quais passaram e quais falharam

Se todos os testes passarem, você verá uma saída semelhante a:

......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK

Cada ponto (.) representa um teste que passou com sucesso.
