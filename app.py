from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        try:
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            operacion = request.form["operacion"]

            # ......
            resultado = eval(f"{num1}{get_operator(operacion)}{num2}")
        except Exception as e:
            resultado = f"Error: {str(e)}"
    return render_template("index.html", resultado=resultado)


def get_operator(op):
    if op == "sumar":
        return "+"
    elif op == "restar":
        return "-"
    elif op == "multiplicar":
        return "*"
    elif op == "dividir":
        return "/"
    else:
        return ""

if __name__ == "__main__":
    app.run(debug=True)
