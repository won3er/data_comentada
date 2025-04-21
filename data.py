import datetime # biblioteca para manipulação de datas e horas
import calendar # biblioteca para manipulação de datas e horas
from num2words import num2words # biblioteca para converter números em palavras



data = datetime.datetime.now() # Obtém a data e hora atual
print(data) # Imprime a data e hora atual

ano = data.year # Obtém o ano atual
mes = data.month # Obtém o mês atual
dia = data.day # Obtém o dia atual
hora = data.hour # Obtém a hora atual
minuto = data.minute # Obtém o minuto atual
segundo = data.second # Obtém o segundo atual

# Formata a data e hora atual em uma string
formato = data.strftime("%d/%m/%Y %H:%M:%S") # Formata a data e hora atual em uma string
print(formato) # Imprime a data e hora atual formatada
print("Ano:", ano) # Imprime o ano atual
print("Mês:", mes) # Imprime o mês atual 
print("Dia:", dia) # Imprime o dia atual
print("Hora:", hora) # Imprime a hora atual
print("Minuto:", minuto) # Imprime o minuto atual
print("Segundo:", segundo) # Imprime o segundo atual



# Inforamções adicionais sobre a data e hora atual
# Exibe o dia da semana, dia do mês, dia do ano, semana do ano, mês, ano e hora
print("Dia da semana:", data.strftime("%A"))
print("Dia do mês:", data.strftime("%d"))
print("Dia do ano:", data.strftime("%j"))
print("Semana do ano:", data.strftime("%U"))
print("Mês:", data.strftime("%m"))
print("Ano:", data.strftime("%Y"))
print("Hora:", data.strftime("%H"))


# Exibindo o dia da semana
dia_extenso = num2words(data.day, lang='pt')
mes_extenso = num2words(data.month, lang='pt')
ano_extenso = num2words(data.year, lang='pt')

#cria a string por extenso

data_extenso = f"Dia {dia_extenso} do mês {mes_extenso} de {ano_extenso}"
print("Data por extenso:", data_extenso) # Imprime a data por extenso

