uchazeci = [
    {"jmeno": "Jan Novák", "matematika": 85, "cestina": 78, "anglictina": 90},
    {"jmeno": "Petra Svobodová", "matematika": 92, "cestina": 88, "anglictina": 85},
    {"jmeno": "Karel Dvořák", "matematika": 50, "cestina": 95, "anglictina": 80},

]

def vyber_prijate(input):
    prijatí01 = []
    for i in input:
        if i["matematika"] >= 60 and i["cestina"] >= 60 and i["anglictina"] >= 60:
            celkem = i["matematika"] + i["cestina"] + i["anglictina"]
            prijatí01.append({
                "jmeno": i["jmeno"],
                "matematika": i["matematika"],
                "cestina": i["cestina"],
                "anglictina": i["anglictina"],
                "celkem": celkem
            })
    prijati02 = []
    left = []
    right = []
    center = []
    pivot = [prijatí01[0]]
    for p in range(len(prijatí01)):
        if pivot[0]["celkem"] > prijatí01[p]["celkem"]:
            right.append(prijatí01[p])
        elif pivot[0]["celkem"] < prijatí01[p]["celkem"]:
            left.append(prijatí01[p])
        elif pivot[0]["celkem"] == prijatí01[p]["celkem"]:
            if pivot[0]["matematika"] > prijatí01[p]["matematika"]:
                right.append(prijatí01[p])
            elif pivot[0]["matematika"] < prijatí01[p]["matematika"]:
                left.append(prijatí01[p])
            else:
                center.append(prijatí01[p])
        prijati02 = left + center + right
    return prijati02



vyber_prijate(uchazeci)

prijati = vyber_prijate(uchazeci)

for poradi, uchazec in enumerate(prijati, start=1):
    print(f"{poradi}. {uchazec['jmeno']} – {uchazec['matematika']} (M), {uchazec['cestina']} (ČJ), {uchazec['anglictina']} (AJ) – Celkem: {uchazec['celkem']}")

