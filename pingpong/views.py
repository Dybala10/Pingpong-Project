from django.shortcuts import render

# Create your views here.
def counter(request):
    if 'countA' not in request.session:
        request.session['countA'] = 0
    if 'countB' not in request.session:
        request.session['countB'] = 0
    if 'AServing' not in request.session:
        request.session['AServing'] = ''
    if 'BServing' not in request.session:
        request.session['BServing'] = ''
    if 'whoFirst' not in request.session:
        request.session['whoFirst'] = ''
    if 'winner' not in request.session:
        request.session['winner'] = ''
    if 'nameA' not in request.session:
        request.session['nameA'] = ''
    if 'nameB' not in request.session:
        request.session['nameB'] = ''
    if 'server' not in request.session:
        request.session['server'] = ''
    
    #register
    registration(request)

    if request.method == 'POST':
        if 'terminate' in request.POST:
            request.session['countA'] = 0
            request.session['countB'] = 0
            request.session['isAServing'] = ''
            request.session['isBServing'] = ''
            request.session['whoFirst'] = ''
            request.session['winner'] = ''
            request.session['nameA'] = ''
            request.session['nameB'] = ''
        elif 'buttonA' in request.POST:
            request.session['countA'] += 1
        elif 'buttonB' in request.POST:
            request.session['countB'] += 1
    # Decide who wins
    winner(request)
    
    # Deside who is going to serve
    serve(request)
    
    context = {'countA': request.session['countA'],
               'countB': request.session['countB'],
               'AServing': request.session['AServing'],
               'BServing': request.session['BServing'],
               'whoFirst': request.session['whoFirst'],
               'winner': request.session['winner'],
               'nameA': request.session['nameA'],
               'nameB': request.session['nameB'],
               'server': request.session['server'],
               }
    return render(request, 'page.html', context)

def serve(request):
    A, B = request.session['nameA'], request.session['nameB']
    if 'AServe' in request.POST:
        request.session['AServing'] = 'serving'
        request.session['BServing'] = ''
        request.session['whoFirst'] = A
    if 'BServe' in request.POST:
        request.session['BServing'] = 'serving'
        request.session['AServing'] = ''
        request.session['whoFirst'] = B

    countA = request.session['countA']
    countB = request.session['countB']
    if request.session['whoFirst'] == A:
        if ((countA + countB) // 2) % 2 == 0:
            request.session['AServing'] = 'serving'
            request.session['BServing'] = ''
        else:
            request.session['AServing'] = ''
            request.session['BServing'] = 'serving'
    elif request.session['whoFirst'] == B:
        if ((countA + countB) // 2) % 2 == 0:
            request.session['AServing'] = ''
            request.session['BServing'] = 'serving'
        else:
            request.session['AServing'] = 'serving'
            request.session['BServing'] = ''
    
    if request.session['AServing'] == 'serving':
        request.session['server'] = request.session['nameA']
    if request.session['BServing'] == 'serving':
        request.session['server'] = request.session['nameB']

def winner(request):
    A, B = request.session['nameA'], request.session['nameB']
    countA = request.session['countA']
    countB = request.session['countB']
    winner = ''
    if countA == 11 and countB < 10:
        winner = A
    if countA < 10 and countB == 11:
        winner = B
    if countA > 11 and countA - countB == 2:
        winner = A
    if countB > 11 and countB - countA == 2:
        winner = B
    request.session['winner'] = winner

def registration(request):
    if 'registratePlayers' in request.POST:
        request.session['nameA'] = request.POST['player_1']
        request.session['nameB'] = request.POST['player_2']

def leadBoard(request):
    pass


    
