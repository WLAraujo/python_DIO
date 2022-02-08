from datetime import date, datetime, timedelta

def devolve_data():
    data_atual = date.today()
    # %Y - ano; %m - mês; %d - dia; %H - hora; %M - minuto; %S - segundo 
    data_atual_string = data_atual.strftime("%d-%m-%Y")
    print(data_atual_string)
    return data_atual

def devolve_hora():
    horario_agora = datetime.today()
    horario_agora_string = horario_agora.strftime("%H:%M:%S")
    print(horario_agora_string)

def dia_semana():
    dias = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")
    dia_semana = str(dias[date.today().weekday()])
    print(dia_semana)
    return dia_semana

def converte_data(dia, mes, ano):
    data_str = f'{dia}/{mes}/{ano}'
    data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
    print(data_convertida.date())
    return data_convertida

if __name__ == '__main__':
    devolve_data()
    devolve_hora()
    dia_semana()
    converte_data(15, 11, 1999)