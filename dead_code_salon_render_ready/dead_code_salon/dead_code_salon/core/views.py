import random
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'core/home.html')


@csrf_exempt
def draw_duel(request):
    return render(request, 'core/draw_duel.html')


def fight_betting(request):
    f1 = {"name": "Grizz", "hp": 100, "odds": 2.0}
    f2 = {"name": "Snag", "hp": 100, "odds": 1.5}
    result = None
    log = []
    bet_won = False

    if request.method == "POST":
        bet = request.POST.get("bet")
        turn = 0
        log.append("The fight begins!")

        while f1["hp"] > 0 and f2["hp"] > 0:
            if turn % 2 == 0:
                dmg = random.randint(5, 15)
                f2["hp"] -= dmg
                log.append(f"{f1['name']} hits {f2['name']} for {dmg} damage!")
            else:
                dmg = random.randint(5, 15)
                f1["hp"] -= dmg
                log.append(f"{f2['name']} hits {f1['name']} for {dmg} damage!")
            turn += 1

        f1["hp"] = max(0, f1["hp"])
        f2["hp"] = max(0, f2["hp"])

        if f1["hp"] >= f2["hp"]:
            winner = "fighter1"
            result = f"{f1['name']} wins!"
        else:
            winner = "fighter2"
            result = f"{f2['name']} wins!"

        bet_won = (bet == winner)
        result += " You won your bet!" if bet_won else " You lost your bet."

    return render(request, 'core/fight.html', {
        "f1": f1,
        "f2": f2,
        "result": result,
        "log": log,
        "betWon": bet_won,
    })
