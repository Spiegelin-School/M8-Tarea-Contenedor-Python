import random

def simulate_match():
    chivas_goals = 0
    atlas_goals = 0
    events = []

    # Simulación de 90 minutos
    # Se alterna el turno: en minutos impares Chivas, en pares Atlas
    for minute in range(1, 91):
        team = "Chivas" if minute % 2 == 1 else "Atlas"
        # Número aleatorio entre 1 y 350
        number = random.randint(1, 350)
        outcome = ""

        if 1 <= number <= 100:
            outcome = "disparo desviado del área rival"
        elif 101 <= number <= 200:
            outcome = "disparo y el portero ataja la pelota"
        elif 201 <= number <= 250:
            outcome = "gol de cabeza"
            if team == "Chivas":
                chivas_goals += 1
            else:
                atlas_goals += 1
        elif 251 <= number <= 300:
            outcome = "gol de penal"
            if team == "Chivas":
                chivas_goals += 1
            else:
                atlas_goals += 1
        elif 301 <= number <= 350:
            outcome = "gol con el pie"
            if team == "Chivas":
                chivas_goals += 1
            else:
                atlas_goals += 1

        events.append((minute, team, number, outcome))

    # Resumen del partido
    print("Resumen del partido:")
    for minute, team, number, outcome in events:
        print(f"Minuto {minute}: {team} ({number}) - {outcome}")
    
    print("\nMarcador Final:")
    print(f"Chivas {chivas_goals} - Atlas {atlas_goals}")

if __name__ == "__main__":
    simulate_match()
