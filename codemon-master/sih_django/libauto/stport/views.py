from django.shortcuts import render
from stport.models import student_info


def feedback(request):
	return render(request, 'feedback.html')

def register(request):
	if request.method == "POST":
		email = request.POST.get('email','')
		psw = request.POST.get('psw','')
		remail= request.POST.get('remail','')
		rpsw = request.POST.get('rpsw')
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		street = request.POST.get('street')
		city = request.POST.get('city')
		if(rpsw == psw and email == remail):
			stud_ID = student_info(student_email = email, student_password = psw, student_name = name, student_phone = phone, student_street = street, student_city = city)
			stud_ID.save()
			return render(request, 'rlogin.html')

	return render(request,'register.html')
def detail(request):
	return render(request,'detail.html')

def search(request):
	#speech recognition

	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()

	with sr.Microphone() as source:
		print("say something\n")
		audio = r.record(source,duration =5)
		try:
		   text= r.recognize_google(audio)
		   print(text)
		   res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
		   soup = bs4.BeautifulSoup(res.text, 'lxml')
		   t = str(soup.select('body'))
		   f = open('C:/Users/HP/Desktop/sih_django/libauto/stport/templates/detail.html','w')
		   index =t.find('title')
		   while(t[index]!= ','):
		       if(t[index]!= '"'):
		           print(t[index], end="")
		           f.write(t[index])
		       index = index +1
		   f.write("</br>")    
		   index =t.find('author')
		   while(t[index]!= ','):
		       if(t[index]!= '"'):
		           print(t[index], end="")
		           f.write(t[index])
		       index = index +1    
		   f.close()  
		except Exception as e:
			print(e)
'''
def detaiil(request):
	import speech_recognition as sr
	import webbrowser as wb
	import bs4
	import lxml
	import requests	
	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("say something\n")
		audio = r.record(source,duration =5)
		try:
			text= r.recognize_google(audio)
			print(text)
			res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
			soup = bs4.BeautifulSoup(res.text, 'lxml')
			t = str(soup.select('body'))
			author = ""
			title = ""
			lang=""
			publication = ""
			category = ""
			g=len(t)   
			tl,ll,tc,ta=[],[],[],[]
			l=[]
			stri = "language"
			for i in range(g-10):
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]=='"title"':
					r=i+8
					while(t[r]!=","):
						title=title+t[r]
						r+=1
					tl.append(title)
					if stri != 'language' and stri != '':
						l.append('null')
					l.append(title)
					str = 'title'
					title =""
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]=='"authors"':
					r=i+11
					while(t[r]!="]"):
						author=author+t[r]
						r+=1
					print(author)
					ta.append(author)
					if(stri != 'title'):
						l.append('null')
					stri = 'author'
					l.append(author)
					author = ''
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]+t[i+9]=="categories":
					r=i+11
					while(t[r]!=","):
						category=category+t[r]
						r+=1
					tc.append(category)
					if(stri != 'author'):
						l.append('null')
					stri = 'category'
					l.append(category)	
					category = ''
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]=="language":
					r=i+8
					while(t[r]!=","):
						lang=lang+t[r]
						r+=1
					ll.append(lang)
					if(stri != 'category'):
						l.append('null')
					l.append(lang)
					str = 'language'
					lang = ''
			print(len(ta),len(tl),len(ll),len(tc),sep=" ")
			print(tl)  
		except Exception as e:
			print(e)	
	return render(request,'detail.html') '''

def detaiil(request):
	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("say something\n")
		audio = r.record(source,duration =5)
		try:
			text= r.recognize_google(audio)
			res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
			soup = bs4.BeautifulSoup(res.text, 'lxml')
			t = str(soup.select('body'))
			author = ""
			title = ""
			lang=""
			publication = ""
			category = ""
			g=len(t)   
			stri =""
#			tl,ll,tc,ta=[],[],[],[]
			l = []
			for i in range(g-10):
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]=='"title"':
					r=i+10
					while(t[r]!='"'):
						title=title+t[r]
						r+=1
				#	tl.append(title)
					if(stri != 'language' and stri != ''):
						l.append('null')
					l.append(title)
					stri = 'title'
					title = ""
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]=='"authors"':
					r=i+19

					while(t[r]!='"'):
						author=author+t[r]
						r+=1
				#	ta.append(author)
					if(stri != 'title'):
						l.append('null')
					l.append(author)
					author = ""
					stri = "author"	
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]+t[i+8]+t[i+9]=="categories":
					r=i+21
					while(t[r]!='"'):
						category=category+t[r]
						r+=1
				#	tc.append(category)
					if(stri != 'author'):
						l.append('null')
					l.append(category)
					category = ''
					stri = "categories"	
				if t[i]+t[i+1]+t[i+2]+t[i+3]+t[i+4]+t[i+5]+t[i+6]+t[i+7]=="language":
					r=i+12
					while(t[r]!='"'):
						lang=lang+t[r]
						r+=1
					if(stri != 'categories'):
						l.append('null')
					l.append(lang)
					stri = 'language'
				#	ll.append(lang)
					lang =''
			for i in range(0,len(l),4):
				desc = book_desc(title = l[i], author = l[i+1], category = l[i+2], language = l[i+3])
				desc.save()


	#		print(len(ta),len(tl),len(ll),len(tc),sep=" ")
			print(l)  
		except Exception as e:
			print(e)	
	return render(request,'detail.html')



def rlogin(request):
	if(request.method == 'POST'):
		uname = request.POST.get('user_name')
		pas = request.POST.get('pass_word')
		st  = student_info.objects.all().filter(student_name = uname)
		for info in st:
			if(info.student_password == pas):
				params = {'name':info.student_name, 'id':info.student_id, 'email' : info.student_email, 'city' : info.student_city, 'street': info.student_street, 'phone' : info.student_phone, 'issue': info.student_issue} 
				return render(request, 'detail.html',params)
	return render(request,'rlogin.html')