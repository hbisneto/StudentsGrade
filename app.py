from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

##########################################################
########################### 01 ###########################
##########################################################
@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'student': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'], # Alterado "aluno" para "student"
    'grade': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00] # Alterado "nota" para "grade"
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
# >> Página table.html criada
@app.route('/table')
def table():
    return render_template('table.html', df=df) # Inserido o parâmetro do dataframe na função de retorno.

# Adicionada a chamada da função e a porta para a execução em localhost (http://127.0.0.1:5000/)
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)