def tasks_per_hour(tasks, hours):
    return tasks / hours if hours != 0 else "На ноль делить нельзя"


assert tasks_per_hour(18, 3) == 6
assert tasks_per_hour(16, 0) == "На ноль делить нельзя"
assert tasks_per_hour(64, 8) == 8
print(tasks_per_hour(121, 11) == 11)


words = ["мяч", "ракетка", "велосипед"]
print(sorted(words, key=lambda word: len(word)))