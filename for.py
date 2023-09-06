classes = [
    {'name': '3А', 'scores': [3,4,4,5,2]},
    {'name': '3Б', 'scores': [5,5,3,2,2]},
    {'name': '3В', 'scores': [4,5,3,5,4]},
]

def count_class_avg(student_stores):
    scores_sum = 0
    for score in student_stores:
        scores_sum += score
    return scores_sum / len(student_stores)

school_avb_sum = 0
for every_class in classes:
    class_avg = count_class_avg(every_class['scores'])
    print(f'Средняя оценка класса {every_class["name"]} = {class_avg}')
    school_avb_sum += class_avg

print(f'Средняя оценка по школе = {round((school_avb_sum / len(classes)),2)}')