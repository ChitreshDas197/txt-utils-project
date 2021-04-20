# This file is for views - created by Chitresh

# from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    # Get the text sent from the user
    text = request.POST.get('text', 'default')
    temp_text = text

    params = {}

    # Get the status of the checkbox
    remove_punc_stat = request.POST.get('removepunc', 'off')
    upper_case_stat = request.POST.get('uppercase', 'off')
    remove_extra_space = request.POST.get('remove_extra_space', 'off')
    remove_new_line = request.POST.get('remove_new_line', 'off')

    # Check for the status of the checkbox and accordingly take actions
    if remove_punc_stat == 'off' and upper_case_stat == 'off' and \
            remove_new_line == 'off' and remove_extra_space == 'off':
        params = {'userText': text, 'analyzed_version': text, 'purpose': 'You Have not chosen any purpose'}
        return render(request, 'analyze.html', params)

    if remove_punc_stat == 'on':
        # Create the punctuation list
        analyzed_text = ""
        punc_list = punctuation
        for char in temp_text:
            if char not in punc_list:
                analyzed_text += char

        params = {'userText': text, 'analyzed_version': analyzed_text, 'purpose': 'Remove Punctuations'}
        temp_text = analyzed_text

    if upper_case_stat == 'on':
        analyzed_text = ""

        for char in temp_text:
            analyzed_text += char.upper()

        params = {'userText': text, 'analyzed_version': analyzed_text, 'purpose': 'Capitalize'}
        temp_text = analyzed_text

    if remove_extra_space == 'on':
        analyzed_text = ""

        for i, char in enumerate(temp_text):

            if not (text[i] == " " and text[i + 1] == " "):
                analyzed_text += char

        params = {'userText': text, 'analyzed_version': analyzed_text, 'purpose': 'Remove Extra Space'}
        temp_text = analyzed_text

    if remove_new_line == 'on':
        analyzed_text = ""
        # Considering Carriage return too
        for char in temp_text:

            if char != '\n' and char != '\r':
                analyzed_text += char

        params = {'userText': text, 'analyzed_version': analyzed_text, 'purpose': 'Remove New Lines'}
        temp_text = analyzed_text

    return render(request, 'analyze.html', params)
