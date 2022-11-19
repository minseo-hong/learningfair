from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        article = request.POST.get('article')

        result = summarize(article)

        context = {
            'article': article,
            'result': result,
            'is_completed': True,
            'is_post': True,
        }

        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html')


def summarize(article):
    result = article

    return result
