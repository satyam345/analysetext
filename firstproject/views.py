from django.http import HttpResponse
from django.shortcuts import render
import string


def index(request):
    return render(request, 'index.html')


def textanalyzer(request):
    # get the text
    word = request.POST.get('text', 'default')

    # check the check value
    removepunc = request.POST.get('removepunc', 'off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    countword = request.POST.get('wordcount', 'off')

    # defining punctuation list
    punc_list = string.punctuation

    # check which checkbox is on
    if removepunc == 'on':
        word1 = ''
        for char in word:
            if char not in punc_list:
                word1 = word1 + char
        params = {'purpose': 'Remove Punctuations', 'output': word1}
        word = word1

    if allcaps == 'on':
        word1 = ''
        for char in word:
            word1 = word1 + char.upper()
        params = {'purpose': 'Capitalize each letter', 'output': word1}
        word = word1

    if newlineremover == 'on':
        word1 = ''
        for char in word:
            if char != '\n' and char != '\r':
                word1 = word1 + char
        params = {'purpose': 'Remove NewLine', 'output': word1}
        word = word1

    if countword == 'on':
        counter = 0
        for char in word:
            if char != ' ':
                counter = counter + 1
        params = {'purpose': 'Count Words', 'output': counter, 'word': word}

    # no checking
    if countword != 'on' and allcaps != 'on' and newlineremover != 'on' and removepunc != 'on':
        return HttpResponse('Error')

    return render(request, 'analyzetext.html', params)
