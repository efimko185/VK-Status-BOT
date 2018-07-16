import vk_api, wolframalpha
from datetime import datetime
from time import sleep
import options as o

def date():
	global dat
	dat = datetime.strftime(datetime.now(), "[%Y.%m.%d][%H:%M:%S]")


vk = vk_api.VkApi(o.login, o.password)
try:
	date()
	print('{}[Попытка авторизации...]'.format(dat)) 
	vk.auth() #авторизация
	date()
	print('{}[Авторизация прошла успешно!]'.format(dat))
except vk_api.exceptions.BadPassword:
	date()   
	print('{}[Ошибка авторизации!][Неверный пароль.]'.format(dat))	
	exit(0)	

app_id = 'YTJTWV-PRUUTP939W'
client = wolframalpha.Client(app_id)

while True:
	tim = datetime.strftime(datetime.now(), "%H:%M") 
	wf = 'weather city {}'.format(o.city)
	try:
		date()   
		print('{}[Получение погоды...]'.format(dat))
		res = client.query(wf)
		date()   
		print('{}[Погода получена!]'.format(dat))
	except Exception:
		date()   
		print('{}[Ошибка получения погоды!]'.format(dat))

	answer = next(res.results).text
	weather = answer[14:19]
	text = 'Текущее время: {} | Погода в {}: {}'.format(tim, o.city2, weather)
	try:
		date()  
		print('{}[Обновление статуса...]'.format(dat))
		vk.method('status.set', {'text':text})
		date()  
		print('{}[Статус успешно обновлён.]'.format(dat))
	except Exception:
		date()  
		print('{}[Ошибка обновления статуса!]'.format(dat))
	date()
	print('{}[Сплю.][{} сек.]'.format(dat, o.timer))
	sleep(o.timer)