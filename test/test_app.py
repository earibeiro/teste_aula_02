import pytest 
from src.senha import senha

"""
    Requisitos Funcionais: O sistema deve validar senhas com as seguintes regras:
    Mínimo de 8 caracteres.
    Pelo menos uma letra maiúscula.
    Pelo menos uma letra minúscula.
    Pelo menos um número.
    Pelo menos um caractere especial (ex: !@#$%^&*).
    Não pode conter espaços em branco.
    """


 # Testes de senhas inválidas
def testeDeSenhaComMenosDe8Caracteres():
    assert senha("senha") == False # Tem menos de oito caracteres

def testeDeSenhaSemLetraMaiuscula():
    assert senha("senhaforte") == False # Não tem letra maiúscula

def testeDeSenhaSemLetraMinuscula():
    assert senha("SENHAFORTE") == False # Não tem letra minúscula

def testeDeSenhaSemNumeroESimbolo():
    assert senha("SenhaForte") == False # Não tem ao menos um número nem um símbolo

def testeDeSenhaSemSimboloComNumero():
    assert senha("SenhaForte1") == False # Não contém caractece especial mas contém número

def testeDeSenhaComSimboloSemNumero():
    assert senha("SenhaForte!") == False # Não contem número mas contem caractere especial

def testedeDeSenhaComEspacoENumero():
    assert senha("Senha Forte1") == False # Possui um espaço em branco

def testeDeSenhaComEspacoSemNumero():
    assert senha("Senha Forte!") == False # Possui um espaço em branco

def testDeSenhaCorretaComEspaco():
    assert senha("Senha Forte1!") == False # Apesar de ter todos os requisitos, possui um espaço em branco


# Teste de senha válida
def test_senha_valida():

    assert senha("SenhaForte1!") == True # A senha está em conformidade.

   


    