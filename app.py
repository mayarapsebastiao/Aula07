#def big_mac():
#    print("sanduiche big mac")

#print ("incio")
#big_mac()
#big_mac()
#big_mac()
#print ("fim")

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")
#fazer_big_mac("Roger")
#fazer_big_mac("Cris")
#fazer_big_mac("Manu")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}")

#fazer_big_mac("Roger")
#fazer_batata("grande")
#preparar_refrigerante("coca","média")

def fazer_combo_big_mac(nome, tamanho_batata,tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamanho_refri)

#fazer_combo_big_mac("Roger","Grande","Coca","Média")

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,20)

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado = maior_num([321,450,2,10,3,0,6,55])
print(resultado)
