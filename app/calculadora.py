"""Módulo con operaciones básicas de una
calculadora: sumar, restar, multiplicar y dividir."""
import math

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a y b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b.
    Lanza un ZeroDivisionError si b es 0.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def potencia(a, b):
    """Eleva a a la potencia b"""
    return a ** b

def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de a"""
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(a)
