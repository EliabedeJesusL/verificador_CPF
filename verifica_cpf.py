def f_limpa(x):
 novo_cpf =""
 for i in range(len(x)):
  if (x[i] != "." and x[i] != "-"):
    novo_cpf += x[i]
 return novo_cpf

def f_primeiroDV(c):
 d = 0
 mult = 10
 for i in range(len(c)):
   d += int(c[i])*mult
   mult = mult -1
 resto = d % 11
 if (resto < 2):
  d = 0
 else:
  d = 11 - resto
 return str(d)

def f_segundoDV(c):
 d = 0
 mult = 11
 for i in range(len(c)):
    d += int(c[i])*mult
    mult = mult -1
    resto = d % 11
 if (resto < 2):
    d = 0
 else:
    d = 11 - resto
 return str(d)

def f_testaCPF(cpf):
 cpf = f_limpa(cpf)
 dv = cpf[9:]
 cpf = cpf[:9]
 dv1 = f_primeiroDV(cpf)
 dv2 = f_segundoDV(cpf+dv1)
 if (dv == dv1+dv2):
   return True
 return False

def f_testaCPF2(cpf):
  cpf = f_limpa(cpf)
  dv1 = f_primeiroDV(cpf[:9])
  if (cpf[9:] == dv1+f_segundoDV(cpf[:9]+dv1)):
   return True
  return False

def main():
 cpf = input()
 if (f_testaCPF2(cpf) == True):
   print('CPF VÁLIDO')
 else:
  print('CPF INVÁLIDO')
 return 0

if __name__ == "__main__":
  main()