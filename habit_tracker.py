def habit_report(habits):
    completed = sum(1 for x, status in habits if status)
    return {"completed": completed, "total": len(habits)}


habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True),
    ("Meditate", False)
]

for name, status in habits:
    if status:
        print(name + ": Done")
    else:
        print(name + ": Not done")

print(habit_report(habits))