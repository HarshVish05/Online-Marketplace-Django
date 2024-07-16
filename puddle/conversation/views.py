from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Conversation,ConversationMessage
from item.models import Item
from .forms import ConversationMessageForm
# Create your views here.

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk = item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:myItems')

    conversations = Conversation.objects.filter(item= item).filter(members__in = [request.user.id])
    
    if conversations:
        return redirect('conversation:detail_msg', pk= conversations.first().id)  # redirect to conversations
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation  = Conversation.objects.create(item= item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit= False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk = item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })
    

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in = [request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })
    

@login_required
def detail_msg(request, pk):
    conversation = Conversation.objects.filter(members__in = [request.user.id]).get(pk= pk)
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit= False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()

            return redirect('conversation:detail_msg', pk= pk)
    else:
        form = ConversationMessageForm()   

    return render(request, 'conversation/detail_msg.html', {
        'conversation': conversation,
        "form": form
    })