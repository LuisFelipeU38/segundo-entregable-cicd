"""Aplicación Flask principal para la calculadora.

Define las rutas y maneja la lógica de interacción
con el usuario a través del formulario web.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja la ruta principal del sitio.
    Si GET, muestra el formulario.
    Si POST, procesa la operación seleccionada.
    """
    resultado = None
    if request.method == "POST":
        operacion = request.form.get("operacion")
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")

        try:
            # Raíz cuadrada → solo usa num1
            if operacion == "raiz_cuadrada":
                num1 = float(num1)
                resultado = raiz_cuadrada(num1)

            # Operaciones normales → requieren ambos
            else:
                num1 = float(num1)
                num2 = float(num2)

                if operacion == "sumar":
                    resultado = sumar(num1, num2)
                elif operacion == "restar":
                    resultado = restar(num1, num2)
                elif operacion == "multiplicar":
                    resultado = multiplicar(num1, num2)
                elif operacion == "dividir":
                    resultado = dividir(num1, num2)
                elif operacion == "potencia":
                    resultado = potencia(num1, num2)
                else:
                    resultado = "Operación no válida"

        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    """Endpoint de verificación de estado
    del servicio (health check)."""
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    app_port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=app_port, debug=False)
