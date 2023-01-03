"""By the end of today, we will build a website that holds some secrets. Only with the right username
 and password can you access the page with our secrets.
  Primeiro, importou as bibliotecas: flask, para trabalhar com sites no Python, render template para lidar com o html,
   flask_wtf para lidar com formulários e stringfields que eu acho que é para lidar com campos que vão receber strings.
   Também foi importado o módulo validators para usar uma validação automática da biblioteca e o bootstrap
 Ressalva, todas as instalações tive que fazer através
 do PIP ou pelo settings, python interpreter, +. Também precisei atualizar o requirement.txt para que o código funcionasse
 """
"""One of the biggest reasons why we would choose WTForms over HTML Forms is the built-in validation. 
Instead of us having to write our own validation code e.g. emails should contain a "@" and a "." to be valid or make
 sure that passwords are minimum of 8 characters, we can use all these validation rules straight out of the
  box from WTForms."""

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

"""Aqui foi aplicado o conceito de OOP, visto na aula 16, foi criada uma classe para o formulário de login e 
dentro dela foi passada a classe FlaskForm, que é uma classe do flask_wtf como atributo, ou seja, a classe
aqui criada vai usar os métodos da FlaskForm. Depois foram criadas mais duas variáveis para lidar com o e-mail e o 
password. Na documentação não explica o que o Flask Form faz exatamente, lá diz:
Flask-WTF provides your Flask application integration with WTForms. No material do curso a Angela explica:
Os argumentos fornecidos ao criar um StringField ou PasswordField são para a propriedade label do campo do formulário.
 Mesmo que o Quickstart não o adicione, prefiro adicionar o argumento de palavra-chave quando não estiver claro para 
 que serve o argumento. Esse label está sendo usado no login.html, assim: {{ form.email.label }}"""
"""The validators parameter accepts a List of validator Objects. DataRequired makes the two fields required fields,
 so the user must type something, otherwise an error will be generated. Então, a variável validators recebe
 os atributos DataRequired e email que exigirão que algo seja digitado e que seja no formato email
 com @ e . O do password exige algo digitado e no tamanho mínimo de 8 caracteres"""
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

"""é exigência do crsf uma secret key para o código funcionar"""
app.secret_key = "cudemula"
app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")

"""The final step is to tell our form to validate the user's entry when they hit submit. so we have to edit
 our route and make sure it is able to respond to POST requests and then to validate_on_submit()."""
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)