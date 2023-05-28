from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Poll, Tag

@csrf_exempt
def create_poll(request):
    if request.method == 'POST':
        data = request.POST.dict()
        question = data['Question']
        option_vote = data['OptionVote']
        tags = data['Tags']

        poll = Poll(question=question)
        poll.save()
        for option, vote in option_vote.items():
            setattr(poll, option.lower().replace(' ', ''), vote)
        poll.save()

        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            poll.tags.add(tag)

        return HttpResponse("Poll created successfully!")
    else:
        return HttpResponse("Invalid request method")
    

        
