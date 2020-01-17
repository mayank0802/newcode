from django.shortcuts import render	
from libadmin.models import notice,book_info, lib_admin
import datetime
def bkinfo(request):
	if request.method == 'POST':
		book_author = request.POST.get('book_author','')
		book_name = request.POST.get("book_name", '')
		count = request.POST.get("book_count",'')
		lot = request.POST.get("lot",'')
		for i in range(0,int(count)):
			book_infos = book_info(book_author = book_author, book_name = book_name, book_lot = lot)
			book_infos.save()

	return render(request,'new_book.html')
def libb(request):
	if request.method == 'POST':
		a_nam = request.POST.get('user_name','')
		pas = request.POST.get('pass_word','')
		st  = lib_admin.objects.get(a_name = a_nam)
		if(st.a_password == pas): 
			return render(request, 'admin_home.html')
		else:
			return render(request, 'alogin.html')
	return render(request,'alogin.html')

def bk_issue(request):
	if request.method == 'POST':
		book_id = request.POST.get('book_id','')
		book_stud_id = request.POST.get("student_id", '')
		book = book_info.objects.get(book_id = book_id)
		print(book)
		book.bk_student_id = book_stud_id
		today = datetime.date.today()
		book.bk_issue = today
		book.book_submission = today + datetime.timedelta(days = 7)
		book.save()	
	return render(request, 'bkinfo.html')
def retrn(request):
	if request.method=='POST':
		book_id=request.POST.get('book_id','')
		book_stud_id = request.POST.get("student_id", '')
		book = book_info.objects.get(book_id = book_id)
		book.bk_student_id = -1
		today = datetime.date.today()
		book.bk_issue = today
		book.book_submission = today
		book.save()
	return render(request, 'return.html')
def admin_home(request):
	return render(request,'admin_home.html')
def noticce(request):
	if request.method == 'POST':
		str = request.POST.get('notice','')
		noticee = notice(notice1 = str)
		noticee.save()
	return render(request,'notice.html')

def home(request):
	return render(request,'home.html')