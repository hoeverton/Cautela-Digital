
class Policial:
    
    def __init__(self,nome,nomeDeGuerra,rg,post_grad,email,senha,confSenha):

        self.nome = nome
        self.nomeDeGuerra = nomeDeGuerra
        self.rg = rg
        self.post_grad = post_grad
        self.email = email
        self.senha = senha
        self.confSenha = confSenha

    def verificar_senha(self):

        if self.senha == self.confSenha:
            print( "Senha Salvo com Sucesso!")
        
        else:
         print("Senha e confirma senha deve ser igual!")
    
    def oi(self):
        print("oiiiii")

class Furriel(Policial):

    print("Acesso Total!")

