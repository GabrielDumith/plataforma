usuaro_login="gabriel"
usuario_senha="12345"
login=input("digite seu login: ")
senha=int(input("digite sua senha: "))

if login != usuaro_login and senha != usuario_senha:
    print("login errado")

else:
    print("login ok")
