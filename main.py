import requests
import time
import src.captions_api as cap
import src.utils as utils

starting_jobs = utils.load_csv()
if len(starting_jobs) < 1:
    print("jobs.csv file is empty, please fill out the file to start the bot!")
    exit()

status_jobs = []

upload_jobs = []

print("\n")
folder_name = input("Choose folder name for this download: ")
avatar_id = cap.display_avatars()

i = 1
for x in starting_jobs:
    ts, itters = cap.generate_transcript(x['content'])
    threads_num = x['count'] // itters
    div_mod = x['count'] % itters
    if div_mod > 0:
        threads_num += 1
    for _ in range(threads_num):
        print(f"[Task {i} - {x['phrase_name']}] Starting generation process...")
        operation_id = cap.submit_generation(ts, avatar_id)
        status_jobs.append({"opertaionId": operation_id, "status": "waiting", "name": f"{x['phrase_name']}", "task_id": i})
        i += 1

print("\n------------------------\n")
time.sleep(10)

flag = True
while flag:
    flag = False
    for x in status_jobs:
        if x["status"] == "waiting":
            flag = True
            fileId, progress = cap.check_generation_status(x["opertaionId"])
            if fileId == "error":
                x["status"] = "done"
                continue
            elif fileId != "":
                print(f"[Task {x['task_id']} - {x['name']}] Generation process finished.")
                x["status"] = "done"
                upload_jobs.append({"fileId":fileId, "status": "waiting", "name": x['name'], "task_id": x['task_id'], "eTag": ""})
            else:
                print(f"[Task {x['task_id']} - {x['name']}] Generation progress {progress}%...")
    
    for i in upload_jobs:
        if i['status'] == "waiting":
            flag = True
            status, url, new_etag = cap.check_upload_status(i["fileId"], i["eTag"])
            i['eTag'] = new_etag
            print(f"[Task {i['task_id']} - {i['name']}] File status {status}")
            if status == "READY":
                i['status'] = url
                print(f"[Task {i['task_id']} - {i['name']}] Downloading mp4 files...")
                path = f"downloads/{folder_name}/{i['name']}"
                file_name = f"{i['task_id']}_{i['name']}.mp4"
                result = cap.download_mp4(url, path, file_name)
                if result:
                    print(f"[Task {i['task_id']} - {i['name']}] File downloaded to {path}.")
                else:
                    print(f"[Task {i['task_id']} - {i['name']}] Failed to download the file.")
    print("\n------------------------\n")
    time.sleep(10)