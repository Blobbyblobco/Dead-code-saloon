from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'core/home.html')

@csrf_exempt
def draw_duel(request):
    return render(request, 'core/draw_duel.html')


import random

def fight_betting(request):
    f1 = {"name": "Grizz", "hp": 100, "odds": 2.0}
    f2 = {"name": "Snag", "hp": 100, "odds": 1.5}
    result = None
    log = []

    if request.method == "POST":
        bet = request.POST.get("bet")
        turn = 0
        log.append("The fight begins!")
        while f1["hp"] > 0 and f2["hp"] > 0:
            dmg1 = random.randint(5, 15)
            dmg2 = random.randint(5, 15)
            if turn % 2 == 0:
                f2["hp"] -= dmg1
                log.append(f"{f1['name']} hits {f2['name']} for {dmg1} damage!")
            else:
                f1["hp"] -= dmg2
                log.append(f"{f2['name']} hits {f1['name']} for {dmg2} damage!")
            turn += 1

        if f1["hp"] > f2["hp"]:
            winner = "fighter1"
            result = f"{f1['name']} wins!"
        else:
            winner = "fighter2"
            result = f"{f2['name']} wins!"

        if bet == winner:
            result += " You won your bet!"
        else:
            result += " You lost your bet."

    return render(request, 'core/fight.html', {
        "f1": f1,
        "f2": f2,
        "result": result,
        "log": log if result else None
    })
