from flask import Flask, redirect, request, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='jobs.visie.com.br',
    user='ewertonfreitas',
    password='ZXdlcnRvbmZy',
    database='ewertonfreitas',
)

cursor = mydb.cursor()

@app.route("/", methods=['GET', 'POST'])
def read_create_pessoa():
    # CREATE -------------------------------------------------------------------
    if request.method == "POST":
        details = request.form

        id_pessoa = details['input_id_pessoa']
        nome = details['input_nome']
        rg = details['input_rg']
        cpf = details['input_cpf']
        data_nascimento = details['input_data_nascimento']
        data_admissao = details['input_data_admissao']
        funcao = details['input_funcao']

        insert_stmt = (
            "INSERT INTO pessoas (id_pessoa, nome, rg, cpf, data_nascimento, data_admissao, funcao) "
            f'VALUES ("{id_pessoa}", "{nome}", "{rg}", "{cpf}", "{data_nascimento}", "{data_admissao}", "{funcao}")'
        )

        try:
            cursor.execute(insert_stmt)
            mydb.commit()
            return render_template('form.html')
            
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    # RETRIEVE ALL--------------------------------------------------------------
    else:
        res = []

        insert_stmt = (
            "SELECT id_pessoa, nome, data_admissao FROM pessoas"
        )

        cursor.execute(insert_stmt)
        result = cursor.fetchall()

        for row in result:
            row = list(row)
            
            for index, item in enumerate(row):
                if index == 1:
                    row[1] = item[:item.find(' ')]
                    
                if index == 2:
                    row[2] = item.strftime("%d-%m-%Y")
                    
            res.append(row)
        return render_template('list.html', res=res)

# UPDATE -----------------------------------------------------------------------
@app.route("/update/<int:id_pessoa>", methods=['GET', 'POST'])
def update_pessoa(id_pessoa):
    if request.method == "POST":
        details = request.form

        nome = details['input_nome']
        rg = details['input_rg']
        cpf = details['input_cpf']
        data_nascimento = details['input_data_nascimento']
        data_admissao = details['input_data_admissao']
        funcao = details['input_funcao']

        insert_stmt = (
            f"UPDATE pessoas SET nome = '{nome}', rg = '{rg}', cpf = '{cpf}', data_nascimento = '{data_nascimento}', data_admissao = '{data_admissao}', funcao = '{funcao}' WHERE id_pessoa = '{id_pessoa}'"
        )

        try:
            cursor.execute(insert_stmt)
            mydb.commit()
            return redirect('/')

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    else:
        res = []

        insert_stmt = (
            f"SELECT nome, rg, cpf, data_nascimento, data_admissao, funcao FROM pessoas WHERE id_pessoa = '{id_pessoa}'"
        )

        cursor.execute(insert_stmt)
        result = cursor.fetchall()

        for row in result:
            res.append(row)

        print(res)

        return render_template('form_up.html', res=res)


# DELETE -----------------------------------------------------------------------
@app.route("/delete/<int:id_pessoa>")
def del_pessoa(id_pessoa):
    sql = f"DELETE FROM pessoas WHERE id_pessoa = '{id_pessoa}'"

    cursor.execute(sql)

    mydb.commit()

    return redirect('/')
    
# RUN SERVER -------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)