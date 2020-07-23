info = open("Info.txt", "r")

info_text = info.read()

markers = [
    "Battre resultat", "Lagre kostnader", "Lyckliga manniskor",
    "Att forandra liv", "tillhandahalla kvalitet"
]

for marker in markers:
    if marker in info_text:
        new_file = open(marker + ".txt", "w+")
        new_file.write(marker)
        new_file.close()

info.close()