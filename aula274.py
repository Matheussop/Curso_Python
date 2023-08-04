# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

from pytz import timezone

data = datetime.now(timezone('America/Sao_Paulo'))
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1670849077))
# data_str_data = '2023/04/20 07:49:23'
# data_str_data = '20/04/2023'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2023, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
