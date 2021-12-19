from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['article']
    fulltext = text.split()
    print("\n\n\n\n Full Text =================>",fulltext)
    word_dict = {}
    for i in fulltext:
        if i.isdigit():
            fulltext.remove(i)
        else:
            if i in word_dict:
                word_dict[i] += 1
            else:
                word_dict[i] = 1
    sorted_dict = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    print(sorted_dict)
    return render(request, 'count.html',{'text':text,'count':len(sorted_dict),'words_count':sorted_dict})

def about(request):
    return render(request,'about.html')