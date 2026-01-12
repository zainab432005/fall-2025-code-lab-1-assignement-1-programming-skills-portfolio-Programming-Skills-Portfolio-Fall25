names = {"Sara", "Lina", "Mona", "Zainab", "Aisha", "Nour"}
for name in names:
    print(name)

names = ["Sara", "Lina", "Mona", "Zainab"]
name1 = "Aisha"
name2 = "Nour"
names.append(name1)
names.append(name2)
for name in names:
    print(name)

names = ["Sara", "Lina", "Mona", "Zainab"]
names[0] = "Aisha"
names[1] = "Nour"
names.remove("Mona")
for name in names:
    print(name)
names = ["Sara", "Lina", "Mona", "Zainab", "Aisha", "Nour"]
names.sort()
for name in names:
    print(name)