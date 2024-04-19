from math import *

while(True):
  print("Menu de opcoes\n")
  print("Escolha o que voce deseja calcular\n")
  print("1 - Propriedades do atomo de H\n")
  print("2 - Emissao/absorcao de foton pelo H\n")
  print("3 - Fotons\n")
  print("4 - Emissao de foton pelo H\n")
  print("5 - Absorcao de foton pelo H\n")
  i1 = int(input("Digite a opcao desejada: "))
  if(i1 == 1):
    print("Digite o numero quantico\n")
    n = int(input("n = "))
    r = (n**2)*(5.29e-11) #m
    U = -27.2/n**2 #eV
    E = -13.6/(n**2) #eV
    K = 13.6/(n**2) #eV
    v = 2.187e6/n #m/s
    comprimento_onda = (6.626e-34)/((n**2)*5.29e-11*v)
    print("Raio da orbita: ", r, "m")
    print("Energia do foton: ", E, "eV")
    print("Energia cinetica: ", K, "eV")
    print("Energia potencial: ", U, "eV")
    print("Velocidade do foton: ", v, "m/s")
    print("Comprimento de onda: ", comprimento_onda, "m")
  elif(i1 == 2):
    print("Digite o n inicial e o n final\n")
    ni = int(input("n inicial = "))
    nf = int(input("n final = "))
    Efoton = (-13.6/(nf**2)) - (-13.6/(ni**2))
    comprimento_onda_foton = (6.626e-34 * 3e8)/Efoton
    ffoton = 3e8/comprimento_onda_foton
    print("Energia do foton: ", Efoton, "eV")
    print("Comprimento de onda do foton: ", comprimento_onda_foton, "m")
    print("Frequencia do foton: ", ffoton, "Hz")
  elif(i1 == 3):
    print("Voce deseja calcular a energia do foton ou a comprimento de onda/frequencia?\n")
    print("[1] - Energia do foton\n")
    print("[2] - Comprimento de onda/frequencia\n")
    i2 = int(input("Digite a opcao desejada: "))
    if(i2 == 1):
      print("[1] Insira a frequencia do foton\nou\n[2] Insira o comprimento de onda do foton\n")
      escolha = int(input("Escolha qual dado voce deseja inserir: "))
      if(escolha == 1):
        print("Digite a frequencia do foton\n")
        f = float(input("f = "))
        Efoton = (6.626e-34 * f)
        print("Voce deseja a resposta em J ou eV?\n")
        print("[1] J\n[2] eV\n")
        escolha_um = int(input("Escolha a opcao desejada: "))
        if(escolha_um == 1):
          print("Energia do foton: ", Efoton, "J")
        else:
          print("Energia do foton: ", Efoton/1.602e-19, "eV")
      else:
        print("Digite o comprimento de onda do foton\n")
        comprimento_de_onda = float(input("comprimento de onda = "))
        Efoton = (6.626e-34 * 3e8)/comprimento_de_onda
        print("Voce deseja a resposta em J ou eV?\n")
        print("[1] J\n[2] eV\n")
        escolha_um = int(input("Escolha a opcao desejada: "))
        if(escolha_um == 1):
          print("Energia do foton: ", Efoton, "J")
        else:
          print("Energia do foton: ", Efoton/1.602e-19, "eV")
    else:
      print("Voce deseja calcular a energia do foton ou a frequencia?\n")
      print("[1] - Energia do foton\n")
      print("[2] - Frequencia\n")
      i3 = int(input("Digite a opcao desejada: "))
      if(i3 == 1):
        print("Voce deseja digitar a Energia em J ou eV?\n")
        print("[1] J\n[2] eV\n")
        escolha_dois = int(input("Escolha a opcao desejada: "))
        if(escolha_dois == 1):
          print("Digite a energia do foton\n")
          Efoton = float(input("E = "))
          comprimento_de_onda = (6.626e-34 * 3e8)/(Efoton * 1.602e-19)
          print("Comprimento de onda do foton: ", comprimento_de_onda, "m")
        else:
          print("Digite a energia do foton\n")
          Efoton = float(input("E = "))
          comprimento_de_onda = (6.626e-34 * 3e8)/(Efoton)
          print("Comprimento de onda do foton: ", comprimento_de_onda)
      else:
        print("Voce deseja digitar a Energia em J ou eV?\n")
        print("[1] J\n[2] eV\n")
        escolha_dois = int(input("Escolha a opcao desejada: "))
        if(escolha_dois == 1):
          print("Digite a energia do foton\n")
          Efoton = float(input("E = "))
          frequencia = Efoton/6.626e-34
          print("Frequencia do foton: ", frequencia, "Hz")
        else:
          print("Digite a energia do foton\n")
          Efoton = float(input("E = "))
          frequencia = Efoton/4.136e-15
          print("Frequencia do foton: ", frequencia, "Hz")
  elif(i1 == 4):
    print("Voce deseja calcular o n inicial ou o n final?\n")
    print("[1] - n inicial\n[2] - n final")
    i4 = int(input("Digite a opcao desejada: "))
    if(i4 == 1):
      print("Voce deseja digitar o comprimento de onda ou a frequencia?\n")
      print("[1] - Comprimento de onda\n[2] - frequencia")
      i5 = int(input("Digite a opcao desejada: "))
      if(i5 == 2):
        print("Digite o n final\n")
        nf = int(input("n final = "))
        print("Digite a frequencia\n")
        frequencia_foton = float(input("f = "))
        Enf = -13.6/nf**2
        Ef = 4.136e-15 * frequencia_foton
        Eni = Ef + Enf
        ni = sqrt(-13.6/Eni)
        print("n inicial: ", ni)
      else:
        print("Digite o n final\n")
        nf = int(input("n final = "))
        print("Digite o comprimento de onda\n")
        comprimento_onda = float(input("comprimento de onda = "))
        Enf = -13.6/nf**2
        Ef = (4.136e-15 * 3e8)/comprimento_onda 
        Eni = Ef + Enf
        ni = sqrt(-13.6/Eni)
        print("n inicial: ", ni)
    else:
      print("Voce deseja digitar o comprimento de onda ou a frequencia?\n")
      print("[1] - Comprimento de onda\n[2] - frequencia")
      i5 = int(input("Digite a opcao desejada: "))
      if(i5 == 1):
        print("Digite o n inicial\n")
        ni = int(input("n inicial = "))
        print("Digite o comprimento de onda\n")
        comprimento_onda = float(input("comprimento de onda = "))
        Eni = -13.6/ni**2
        Ef = (4.136e-15 * 3e8)/comprimento_onda
        Enf = - Ef + Eni
        nf = sqrt(-13.6/Enf)
        print("n final: ", nf)
      else:
        print("Digite o n inicial\n")
        ni = int(input("n inicial = "))
        print("Digite a frequencia\n")
        frequencia = float(input("comprimento de onda = "))
        Eni = -13.6/ni**2
        Ef = 4.136e-15 * frequencia
        Enf = - Ef + Eni
        nf = sqrt(-13.6/Enf)
        print("n final: ", nf)
  else:
    print("Voce deseja calcular o n inicial ou o n final?\n")
    print("[1] - n inicial\n[2] - n final")
    i4 = int(input("Digite a opcao desejada: "))
    if(i4 == 1):
      print("Voce deseja digitar o comprimento de onda ou a frequencia?\n")
      print("[1] - Comprimento de onda\n[2] - frequencia")
      i5 = int(input("Digite a opcao desejada: "))
      if(i5 == 1):
        print("Digite o n final\n")
        nf = int(input("n final = "))
        print("Digite o comprimento de onda\n")
        comprimento_onda = float(input("comprimento de onda = "))
        Enf = -13.6/nf**2
        Ef = (4.136e-15 * 3e8)/comprimento_onda
        Eni = Ef - Enf
        ni = sqrt(-13.6/Eni)
        print("n inicial: ", ni)
      else:
        print("Digite o n final\n")
        nf = int(input("n final = "))
        print("Digite a frequencia\n")
        frequencia_foton = float(input("f = "))
        Enf = -13.6/nf**2
        Ef = 4.136e-15 * frequencia_foton
        Eni = Ef - Enf
        ni = sqrt(-13.6/Eni)
        print("n inicial: ", ni)
    else:
      print("Voce deseja digitar o comprimento de onda ou a frequencia?\n")
      print("[1] - Comprimento de onda\n[2] - frequencia")
      i5 = int(input("Digite a opcao desejada: "))
      if(i5 == 1):
        print("Digite o n inicial\n")
        ni = int(input("n inicial = "))
        print("Digite o comprimento de onda\n")
        comprimento_onda = float(input("comprimento de onda = "))
        Eni = -13.6/ni**2
        Ef = (4.136e-15 * 3e8)/comprimento_onda
        Enf = Ef + Eni
        nf = sqrt(-13.6/Enf)
        print("n final: ", nf)
      else:
        print("Digite o n inicial\n")
        ni = int(input("n inicial = "))
        print("Digite a frequencia\n")
        frequencia = float(input("comprimento de onda = "))
        Eni = -13.6/ni**2
        Ef = 4.136e-15 * frequencia
        Enf = Ef + Eni
        nf = sqrt(-13.6/Enf)
        print("n final: ", nf)