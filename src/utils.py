import csv
import os

def read_or_create_csv(file_path: str, header: list):
    dir_name = os.path.dirname(file_path)
    if dir_name:  
        os.makedirs(dir_name, exist_ok=True)
    
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader] 
    



def repurpose_csv_file(csv_list: list):
    starting_jobs = []
    for i, x in enumerate(csv_list):
        if i == 0:
            continue
        if x[0] == "" or x[1] == "" or x[2] == "":
            continue
        job_dict = {"phrase_name": x[0], "count": int(x[1]), "content": x[2]}
        starting_jobs.append(job_dict)
    return starting_jobs


def load_csv():
    csv_file_as_list = read_or_create_csv('jobs.csv', ['PHRASE_NAME', 'GENERATIONS_NUMBER', 'CONTENT'])
    starting_jobs = repurpose_csv_file(csv_file_as_list)
    return starting_jobs
