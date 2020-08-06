from django.shortcuts import render

def page_home(request):
	return render(request, 'indexHome.html')

def words_in_string(user_text):
	len_string= len(user_text)
	if len_string != 0:
		words=1
	else: return 0
	i=0
	for symbol in  user_text :
		if symbol==' ':
			words+=1
	return words

		
def reverse(request):

	user_text = request.GET['usertext']
	reversed_user_text = user_text[::-1]
	number_of_words = words_in_string(user_text)
	print(number_of_words)
	return render(request, 'page_reverse.html', {'usertext': user_text, 'reversusertext':reversed_user_text, 'words':number_of_words})
