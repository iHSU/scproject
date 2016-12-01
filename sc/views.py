from django.shortcuts import render

# Create your views here.
from .models import Tweet
from .models import Citizen
from .models import Result

import random


def index(request):
    context = {}
    return render(request, 'sc/index.html', context)


def start(request):
    citizen_name = request.POST['citizen_name']
    gender = request.POST['gender']
    age_level = request.POST['age_level']
    occupation = request.POST['occupation']
    # print citizen_name
    # print gender
    # print age_level
    # print occupation
    citizen = Citizen(name=citizen_name, gender=gender, age_level=age_level, occupation=occupation)
    citizen.save()
    citizen_id = citizen.id

    # tweets_from_hillary = Tweet.objects.all().filter(who=1)
    # tweets_from_trump = Tweet.objects.all().filter(who=2)
    tweets = Tweet.objects.all()
    # tweets_size = len(tweets)
    tweets_random = random.sample(tweets, 11)

    context = {'citizen_name': citizen_name,
               'citizen_id': citizen_id,
               'tweets': tweets_random}
    return render(request, 'sc/questions.html', context)


def result(request):
    count_hillary_like = 0
    count_hillary_dislike = 0
    count_trump_like = 0
    count_trump_dislike = 0
    res_hillary = 0
    res_trump = 0
    citizen_id = request.POST['citizen_id']
    citizen = Citizen.objects.get(id=int(citizen_id))
    for i in range(1, 12):
        tweet_id = request.POST['tweet_id_' + str(i)]
        tweet_res = request.POST['tweet_' + str(i)]
        tweet_res_int = int(tweet_res)
        tweet = Tweet.objects.get(id=tweet_id)
        record = Result(citizen=citizen, tweet=tweet, attitude=tweet_res_int)
        record.save()
        who = tweet.who
        if who == 1:    # hillary
            if tweet_res_int == 1:
                count_hillary_like = count_hillary_like + 1
            elif tweet_res_int == -1:
                count_hillary_dislike = count_hillary_dislike + 1
            res_hillary = res_hillary + tweet_res_int
        elif who == 2:           # trump
            if tweet_res_int == 1:
                count_trump_like = count_trump_like + 1
            elif tweet_res_int == -1:
                count_trump_dislike = count_trump_dislike + 1
            res_trump = res_trump + tweet_res_int
    res = 'No result'
    if res_hillary > res_trump:
        res = 'Hillary'
    elif res_trump > res_hillary:
        res = 'Trump'

    context = {'result': res,
               'res_hillary': res_hillary, 'res_trump': res_trump,
               'citizen_id': citizen_id,
               'res_hillary_like': count_hillary_like, 'res_hillary_dislike': count_hillary_dislike,
               'res_trump_like': count_trump_like, 'res_trump_dislike': count_trump_dislike}
    return render(request, 'sc/result.html', context)


def feedback(request):
    citizen_id = request.POST['citizen_id']
    citizen = Citizen.objects.get(id=int(citizen_id))
    citizen.feedback = request.POST['feedback']
    citizen.save()
    context = {'msg': 'Leave feedback successfully.'}
    return render(request, 'sc/index.html', context)


def total_result(request):
    results = Result.objects.all()
    context = {'total': results}
    return render(request, 'sc/total.html', context)