

temp =10.5
massetetthet =1000



# if trigger på en ny måling er klar
def ner(Temperatur) : #bruker den nermeste temperaturen til den målte for å finne avvik fra massetetthet
    mass_adj_tab = {
        10: massetetthet*0.99965,
        11: massetetthet*0.99956,
        12: massetetthet*0.99945,
        13: massetetthet*0.99933,
        14: massetetthet*0.99920,
        15: massetetthet*0.99906,
        16: massetetthet*0.99891,
        17: massetetthet*0.99874,
        18: massetetthet*0.99857,
        19: massetetthet*0.99838,
        20: massetetthet*0.99816,
        21: massetetthet*0.99798,
        22: massetetthet*0.99776,
        23: massetetthet*0.99753,
        24: massetetthet*0.99730,
        25: massetetthet*0.99705,
        26: massetetthet*0.99679,
        27: massetetthet*0.99653,
        28: massetetthet*0.99625,
        29: massetetthet*0.99596,
        30: massetetthet*0.99567
    }
    if Temperatur < 10 or Temperatur > 30:
        return massetetthet
    else:
        return mass_adj_tab[Temperatur]

print(ner(int(round(temp))))
