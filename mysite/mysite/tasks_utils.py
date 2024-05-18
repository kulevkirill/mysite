def get_tasks():
    tasks = []
    with open("./data/tasks.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            task, answer = line.split(";")
            tasks.append([cnt, task, answer])
            cnt += 1
    return tasks
