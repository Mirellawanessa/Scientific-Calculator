from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

# Função para avaliar a expressão e lidar com erros
def evaluate_expression(expr):
    try:
        # Substitui constantes e avalia com SymPy
        expr = expr.replace('pi', 'sp.pi').replace('e', 'sp.E')
        result = sp.sympify(expr)
        return str(result)
    except Exception as e:
        return "Erro: Expressão inválida"

@app.route('/', methods=['GET', 'POST'])
def index():
    expression = ""
    result = ""

    if request.method == 'POST':
        expression = request.form.get('expression', "")

        # Adiciona números ou operadores à expressão
        number = request.form.get('number')
        if number:
            expression += number
        
        operator = request.form.get('operator')
        if operator and operator != "=":
            expression += operator
        
        # Adiciona funções (ex.: sin, cos, etc.)
        function = request.form.get('function')
        if function:
            expression += f"{function}("

        # Calcula o resultado se o botão "=" for pressionado
        if operator == "=":
            result = evaluate_expression(expression)
        
        # Limpa a expressão e o resultado
        if request.form.get('clear'):
            expression = ""
            result = ""

    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
