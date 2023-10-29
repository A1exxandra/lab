def find_common_participants(group1, group2, separator=','):
    list_group1 = group1.split(separator)
    list_group2 = group2.split(separator)
    list_common = list(set(list_group1).intersection(list_group2))
    list_common.sort()
    return list_common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:",participants)
