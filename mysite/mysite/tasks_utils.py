
def get_tasks():
    tasks = []
    with open("./data/tasks.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            task, answer = line.split(";")
            tasks.append([cnt, task, answer])
            cnt += 1
    return tasks

def write_task(new_task, new_answer):
    new_task_line = f"{new_task};{new_answer}"
    with open("./data/tasks.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_task_line]
    terms_sorted.sort()
    new_tasks = [title] + terms_sorted
    with open("./data/tasks.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_tasks))