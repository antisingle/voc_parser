import os, requests, bs4
os.chdir('u:\Резников\py')
out_file = open('text.txt', 'w') 

basename = 'http://www.treko.ru/show_dict_'
nomer = '1'
ii = 1
sii = str(ii)
name = basename + nomer + sii
print(name)

s=requests.get('http://www.treko.ru/show_dict_1')
b=bs4.BeautifulSoup(s.text, "html.parser")
p3=b.select('.verh')
pogoda1=p3[0].getText()
p4=b.select('.dict_text')
pogoda2=p4[0].getText()
#print('Заголовок :' + ' ' + pogoda1 + "\n")
#print('Содержимое:' + ' ' + pogoda2 + "\n")

i = 1
while i < 47:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1

i = 49	
while i < 197:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1

i = 198	
while i < 204:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1

	i = 206
while i < 384:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1
	
i = 385
while i < 600:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1
	
	i = 599
while i < 1000:
	print(str(i))
	url = basename + str(i)
	s=requests.get(url)
	b=bs4.BeautifulSoup(s.text, "html.parser")
	p3=b.select('.verh')
	pogoda1=p3[0].getText()
	p4=b.select('.dict_text')
	#print(len(p4))
	if (len(p4)>0):
		pogoda2=p4[0].getText()
		out_file.write('Номер в базе:' + str(i) + '\n' + 'Заголовок :' + ' ' + pogoda1 + "\n" + 'Содержимое:' + ' ' + pogoda2 + "\n"  + "\n")    
	i = i + 1
	
out_file.close()