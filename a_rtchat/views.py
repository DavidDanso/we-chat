from django.shortcuts import render

# Chat Page views here
def chat_page(request):
    context = {}
    return render(request, 'a_rtchat/chat.html', context)
