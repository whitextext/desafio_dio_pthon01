viado = """
    sistema tecbank

    0 - saque
    1 - deposito
    2 - saldo
    3 - sair do sistema

    digite oque dejesa a seguir =>"""


saquesDiarios = 3
saldo = 2000


def saque(linguica):
    print("""
           voce escolheu a opcao saque
          """)
    print(f"""    
          seu saldo e de {linguica}
        """)
    Valor = int(input(""" 
                      digite o valor que dejesa sacar:
                      """))

    if Valor <= linguica and saquesDiarios > 0 : 
        linguica -= Valor
        print(f"""    
              voce sacou {Valor} da sua conta bancario, seu saldo atual e de {linguica}
            """)
        return linguica
    else:
        print("""
               voce esta sem possibilidade de fazer saques no momento
              """)
        return linguica

def deposito(linguica):
      print("""   
            voce escolheu a opcao deposito
            """)
      valor = int(input("""   
                    digite o valor que deseja depositar:
                    """))
      linguica += valor

      print(f"""  
            voce depositou {valor} a sua conta bancaria, saldo atual:{linguica}""")
      return linguica

def Saldo(linguica):
    print("""
           voce escolheu ver o saldo
          """)
    print(f"""
            seu saldo e de {linguica}
        """)



while(True): 

    baitola = int(input(viado))
    if baitola == 0: saldo = saque(saldo)
    elif baitola == 1: saldo  = deposito(saldo)
    elif baitola == 2: Saldo(saldo)
    elif baitola == 3: 
        print("""  
              voce que sair? ok entao
              """) 
        break
    else: print("""
                opcao invalida
                """)







