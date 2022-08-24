def getDay(hora):
    if (int(hora)) >= 0000 and (int(hora)) <= 1159 :
        return "⛅️ Bom Dia"
    if (int(hora)) >= 1200 and (int(hora)) <= 1759:
        return "🌤 Boa Tarde"
    if (int(hora)) >= 1800 and (int(hora)) <= 2359:
        return "😴 Boa Noite"