#
# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Glauter', email="glauterlima@gmail.com", senha="123465")
#     usuario1 = Usuario(username='Rose', email="rosinha@gmail.com", senha="123465")
#
#     database.session.add(usuario)
#     database.session.add(usuario1)
#
#     database.session.commit()

# with (app.app_context()):
    # meus_usuarios = Usuario.query.all()
    # primeiro_usuario = meus_usuarios[0]
    # print(meus_usuarios)
    # print(primeiro_usuario.username)

    # usuario_teste = Usuario.query.filter_by(id=1).first()
    # print(usuario_teste.email)

    # meu_post = Post(id_usuario=1, titulo='Primeiro Post do Glauter', corpo="Post sensacional")
    # database.session.add(meu_post)
    # database.session.commit()

    # post = Post.query.all()
    # post = Post.query.first()
    # print(post.autor.username)

#resetar o banco de dados
# with app.app_context():
#     database.drop_all()
#     database.create_all()