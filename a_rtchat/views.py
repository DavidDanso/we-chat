from django.shortcuts import render, get_object_or_404
from .forms import ChatmessageCreateForm
from .models import *

# Chat Page views here
def chat_page(request):
    user = request.user.profile
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : user
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)
    context = {'form': form, 'chat_messages': chat_messages}
    return render(request, 'a_rtchat/chat.html', context)
