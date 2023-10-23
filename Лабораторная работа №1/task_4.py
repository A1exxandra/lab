users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visiting = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
visiting["Общее количество"] = len(users)
visiting["Уникальные посещения"] = len(set(users))

print(visiting)
