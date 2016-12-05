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
    count_jill_like = 0
    count_jill_dislike = 0
    count_gary_like = 0
    count_gary_dislike = 0

    res_candidate = {}
    res_candidate['hillary'] = 0
    res_candidate['trump'] = 0
    res_candidate['jill'] = 0
    res_candidate['gary'] = 0

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

        type = 1.0 # default type of tweet, original
        if tweet.type == 2:  # fake tweet
            type = -1.5
        weight = tweet.weight

        if who == 1:    # hillary
            if tweet_res_int == 1:
                count_hillary_like = count_hillary_like + 1
            elif tweet_res_int == -1:
                count_hillary_dislike = count_hillary_dislike + 1
            res_candidate['hillary'] = res_candidate['hillary'] + tweet_res_int * weight * type
        elif who == 2:           # trump
            if tweet_res_int == 1:
                count_trump_like = count_trump_like + 1
            elif tweet_res_int == -1:
                count_trump_dislike = count_trump_dislike + 1
            res_candidate['trump'] = res_candidate['trump'] + tweet_res_int * weight * type
        elif who == 3:
            if tweet_res_int == 1:
                count_jill_like = count_jill_like + 1
            elif tweet_res_int == -1:
                count_jill_dislike = count_jill_dislike + 1
            res_candidate['jill'] = res_candidate['jill'] + tweet_res_int * weight * type
        elif who == 4:
            if tweet_res_int == 1:
                count_gary_like = count_gary_like + 1
            elif tweet_res_int == -1:
                count_gary_dislike = count_gary_dislike + 1
            res_candidate['gary'] = res_candidate['gary'] + tweet_res_int * weight * type

    res = max(res_candidate, key=res_candidate.get)


    context = {'result': res,
               'res_hillary': res_candidate['hillary'], 'res_trump': res_candidate['trump'], 'res_jill': res_candidate['jill'], 'res_gary':res_candidate['gary'],
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


def manage(request):
    context = {}
    return render(request, 'sc/manage.html', context)


def total_result(request):
    results = Result.objects.all()
    context = {'total': results}
    return render(request, 'sc/total.html', context)


def specific_user_result(request):
    citizen_id = request.GET['userid']
    print citizen_id
    results = Result.objects.filter(citizen_id=citizen_id)
    print results
    context = {'results': results}
    print context
    return render(request, 'sc/user_result.html', context)



def users(request):
    citizens = Citizen.objects.all()
    users_res = {}
    for user in citizens:
        results = Result.objects.filter(citizen_id=user.id)
        res_candidate = {}
        res_candidate['hillary'] = 0
        res_candidate['trump'] = 0
        res_candidate['jill'] = 0
        res_candidate['gary'] = 0
        count_hillary_like = 0
        count_hillary_dislike = 0
        count_trump_like = 0
        count_trump_dislike = 0
        count_jill_like = 0
        count_jill_dislike = 0
        count_gary_like = 0
        count_gary_dislike = 0
        for item in results:
            tweet_res_int = item.attitude
            tweet_type = item.tweet.type
            tweet_weight = item.tweet.weight
            tweet_who = item.tweet.who
            type = 1.0  # default type of tweet, original
            if tweet_type == 2:  # fake tweet
                type = -1.5
            if tweet_who == 1:  # hillary
                if tweet_res_int == 1:
                    count_hillary_like = count_hillary_like + 1
                elif tweet_res_int == -1:
                    count_hillary_dislike = count_hillary_dislike + 1
                res_candidate['hillary'] = res_candidate['hillary'] + tweet_res_int * tweet_weight * type
            elif tweet_who == 2:  # trump
                if tweet_res_int == 1:
                    count_trump_like = count_trump_like + 1
                elif tweet_res_int == -1:
                    count_trump_dislike = count_trump_dislike + 1
                res_candidate['trump'] = res_candidate['trump'] + tweet_res_int * tweet_weight * type
            elif tweet_who == 3:
                if tweet_res_int == 1:
                    count_jill_like = count_jill_like + 1
                elif tweet_res_int == -1:
                    count_jill_dislike = count_jill_dislike + 1
                res_candidate['jill'] = res_candidate['jill'] + tweet_res_int * tweet_weight * type
            elif tweet_who == 4:
                if tweet_res_int == 1:
                    count_gary_like = count_gary_like + 1
                elif tweet_res_int == -1:
                    count_gary_dislike = count_gary_dislike + 1
                res_candidate['gary'] = res_candidate['gary'] + tweet_res_int * tweet_weight * type
        res = max(res_candidate, key=res_candidate.get)
        users_res[int(user.id)] = res

    context = {'users': citizens, 'users_res': users_res}
    # print context
    return render(request, 'sc/users.html', context)