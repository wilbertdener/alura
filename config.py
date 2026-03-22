import os
SECRET_KEY = 'alura'  # chave secreta para usar o session
# trecho da app
# app.run(host='0.0.0.0', port=8080)

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(

        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='',
        servidor='localhost',
        database='jogoteca'

    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'