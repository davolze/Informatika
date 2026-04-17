def find_common_participants(list1, list2,razdel=","): #на ввод две строки с участниками через определяемый (по умолчанию через запятую) разделитель
    list1 = list1.split(razdel)
    list2 = list2.split(razdel) #разделение двух строк по разделителю на списки участников
    a = [] #список общих
    for i in list1: #за каждое совпадение между списками добавляет его в список общих
        if i in list2:
            a.append(i)
    return a #возвращает список пересечений


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(sorted(find_common_participants(participants_first_group, participants_second_group,razdel="|"))) #отсортированный список общих участников по 2 строкам