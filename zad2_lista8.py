
contacts = {
    "Sułtan" : 876876890,
    "Szczur" : 723673928,
    "Wezyr" : 676676543,
    "Opat" : 432432145,
    "Skryba" : 123123123,
    "Emir" : 456456456,
    "Saladyn" : 890890890,
    "Marszałek" : 789789789,
    "Wąż" : 567567567,
    "Kalif" : 567987254
}

contacts1 = {
    "Kalif" : 567987254,
    "Szczur": 723673928,
    "Wezyr": 676676543,
    "Opat": 432432145,
    "Skryba": 123123123,
    "Emir": 456456456,
    "Saladyn": 890890890,
    "Marszałek": 789789789,
    "Wąż": 567567567,
    "Sułatan" : 876876890
}
print(contacts)
print(contacts1)

del contacts1["Skryba"]
del contacts1["Emir"]
print(contacts1)

contacts1.clear()

contacts1["Nizar"] = "321123321"
contacts1["Król Filip"] = "432278987"

print(contacts1)

sorted_contacts = dict(sorted(contacts1.items()))
contact_list = list(sorted_contacts.items())
print(contact_list)