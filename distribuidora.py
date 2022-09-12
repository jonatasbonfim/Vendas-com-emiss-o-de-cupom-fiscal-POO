class cad_clientes:

   def __init__(self, email, nome, data_nascimento, rg, cpf, endereco, tel):
       self.email = email
       self.nome = nome
       self.data_nascimento = data_nascimento
       self.rg = rg
       self.cpf = cpf
       self.endereco = endereco
       self.tel = tel


var1 = input('Bem vindo usuario! Para começar com seu pedido por favor insira o seu e-mail: ')
y = '@' in var1
z = '.com' in var1

while (y == False) or (z == False):
   print('email invalido! tente novamente')
   var1 = input('Insira o seu e-mail: ')
   y = '@' in var1
   z = '.com' in var1

print('')
print('------------------------------------------------------------------')
print('Cadastro:')
print('')
var2 = input('Digite seu nome completo: ')
y = input('Digite o dia e mês da data do seu nascimento: (dd/mm) ')
var4 = int(input('Digite o ano do seu nascimento: '))
if var4 > 2001:
   print('Usuario devera ter no minimo 18 anos! cadastro não realizado.')
   exit()

var5 = int(input('Digite o numero do seu RG (Somente numeros): '))
var6 = input('Digite o numero do seu CPF (Somente numeros): ')

if len(var6) != 11:
   while len(var6) != 11:
       print('CPF inválido! tente novamente')
       var6 = input('Digite o numero do seu CPF (Somente numeros): ')

var7 = input('Digite seu endereço: ')
var8 = int(input('Digite o numero do seu telefone: '))


cliente1 = cad_clientes(var1, var2, var4, var5, var6, var7, var8)

bol = 's'
total = 0
pagar1x = 0
pagar2x = 0
pagar3x = 0
pagar4x = 0
pagar5x = 0

while bol == 's':
   pagar1 = 0
   pagar2 = 0
   pagar3 = 0
   pagar4 = 0
   pagar5 = 0

   x1 = int(input('selecione as peças desejadas processador(1) memoria (2) fonte 500w(3) placa mãe(4) placa de Video(5) '))

   if x1 == 1:
       quant1 = int(input('Quantas peças deseja:  '))
       pagar1 = 1200 * quant1

   if x1 == 2:
       quant2 = int(input('Quantas peças deseja:  '))
       pagar2 = 320 * quant2

   if x1 == 3:
       quant3 = int(input('Quantas peças deseja:  '))
       pagar3 = 558 * quant3

   if x1 == 4:
       quant4 = int(input('Quantas peças deseja:  '))
       pagar4 = 600 * quant4

   if x1 == 5:
       quant5 = int(input('Quantas peças deseja:  '))
       pagar5 = 1500 * quant5

   total = pagar1 + pagar2 + pagar3 + pagar4 + pagar5 + total
   bol = input('Deseja realizar outra compra? (s/n):')
   pagar1x = pagar1x + pagar1
   pagar2x = pagar2x + pagar2
   pagar3x = pagar3x + pagar3
   pagar4x = pagar4x + pagar4
   pagar5x = pagar5x + pagar5

if total > 5000:
   desconto = total * 0.1
   total = total - desconto

if total > 10000:
   desconto = total * 0.15
   total = total - desconto

print('')
print('------------------------------------------------------------------')
print('nome: ', cliente1.nome)
print('endereço:', cliente1.endereco)
print('telefone:', cliente1.tel)
print('------------------------------------------------------------------')
print('')
print('------------------------------------------------------------------')
print('itens: ')
print('')
if pagar1x > 0:
   print('processador: ryzen 5 5600g   ', quant1, '------------------- R$ %0.2f' % pagar1x)
if pagar2x > 0:
   print('memoria ddr4 3000mhz: kg(s) ', quant2, '------------------- R$ %0.2f' % pagar2x)
if pagar3x > 0:
   print('fonte 500w 80plus bronze   ', quant3, '------------------- R$ %0.2f' % pagar3x)
if pagar4x > 0:
   print('placa mãe asus a520 :   ', quant4, '------------------- R$ %0.2f' % pagar4x)
if pagar5x > 0:
   print('placa de video 1050ti:  ', quant5, '------------------- R$ %0.2f' % pagar5x)

print('')
if total >= 10000:
   print('kit teclado e mouse (brinde por compra acima de 10000)')
   print('')
print('total -------------------------------- R$ %0.2f' % total)

if total >= 5000:
   desconto = total * 0.1
   total = total - desconto
   print('desconto ------------------------------ R$ %0.2f' % desconto)
   print('total a pagar ------------------------- R$ %0.2f' % total)

if total >= 10000:
   desconto = total * 0.15
   total = total - desconto
   print('desconto ----------------------------- R$ %0.2f' % desconto)
   print('total a pagar ------------------------ R$ %0.2f' % total)


print('------------------------------------------------------------------')
print('Compra realizada com sucesso! Volte sempre')
