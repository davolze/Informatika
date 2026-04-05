import json
def task() -> float:
    with open('input.json') as file:json_data = json.load(file)

    summa = sum([i["score"] * i["weight"] for i in json_data])
    return round(summa, 3)
print(task())
