def conveterMoeda(valor):
    if("." in valor and "," in valor):
        return valor.replace(".", "").replace(",", ".");
    if("," in valor):
        valor.replace(",", ".")
    if("." in valor):
        return valor.replace(".","")
    return valor