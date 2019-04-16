#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    total_count = len(request.GET['text'])
    content = request.GET['text']
    word_dict = {}
    for word in content:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1        
    sort_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    return render(request,'count.html',
                 {'count':total_count,'content':content,
                 'word_dict':word_dict,'sort_dict':sort_dict})