import requests
import os

avatars_dict = {
    1 : {"avatarId": "ctUFWc7w2BtCwqfq4Vht", "avatarVariantId":"qeOAFWe7BCCwOIClvcYi", "name": "Violet (Asian) - Walking in the park"},
    2 : {"avatarId": "RuHyXqTQtifCAuHtmVMq", "avatarVariantId":"P6seXiz486l1nQid0QRT", "name": "Madison - Talking in the gym"},
    3  : {"avatarId": "B5VqhL8HPvPw8VZ4H5Uf", "avatarVariantId":"QveuIuGdwcLmtHpgGoTy", "name": "Ashley - Walking"},
    4 : {"avatarId": "lE6CMlmTY73GvrVlsbdS", "avatarVariantId":"oo0RAIESofBfKGEes2BL", "name": "Jason (Asian) - Sitting and talking"},
    5 : {"avatarId": "XtofXWKaS7jz3nsSq5fD", "avatarVariantId":"XtofXWKaS7jz3nsSq5fD", "name": "Mia - Custom Max"},
    6 : {"avatarId": "nYH2Gn0rgTxhwtZXyLxG", "avatarVariantId":"YuE1bYHzRL3XFB9eKPN6", "name": "Mia - Balck girl"},   
}

def get_token():
    access_token = ""
    url = "https://desktop.captions.ai/api/auth/session"
    cookies = {
        "__Secure-next-auth.session-token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YFF5QG9CdwEubv6o.Y8E1m41niFAkY3EKBuLW3UmZtyA3bhFdFsj-2nZ7zbMOxl6WaLvqW5YJOf7R2zOydjvKTVVMLwOd3PhklYQBuiO25wGvydeNILuykKqUa9FL2OzLtljxf0h6gn_Hm_8Lh9auZVIT5T7rmo6TAT9pZI9LNeeyEG-AMXdAg4V_sbIDsHY499jcnWeaPyYKSU6U02xF_HY0SJesW7_ecsnfBwh_irv3hKpF3gznBpS3ZtJy3CIXD9PLZtZoqDGc1znOsuaTcBDujPl28wdzKQLUlTXt6HbtgGB_v41QhINljZ5xMPIhUAdx_v3M0f_kny6dIq3NjBsEn9P_0aRVp0ryuexJMvZEhmXWXoIb5VqHlBphGi7V-iANgVB3aOaIDD6csyNxm6L7WGR5Pa4FCpkWUVL7186PcHps07r5AOFYUJhsMA_DKdr8GGcuhYvfG450ozwTds6AKaMvkyjxBPSfOY49V1p1vAo-Sqz9mf-p3CkP_vvac3La7aokFjhfXLuYHbtmbN1EZ0ZhSDjm1kbaizKuaFomaIWORrRPgCQzU8PHd1XvKJwFoZgInKUZfl-eDvIwuB54DUQq2irE3ULoa3GfOndI1DPTIOr6yR0F0SJmnKrX7kO58RnCSj9iw_7tTHtUpKhcbGoGrOL0kb5et1JAEWf4bP1fyRGkfH9HZLHO2eUBR_11omd4JWK-CeyundlDFf8tzqe4u4HT3nojtDP9oslIaeoRRxqMgHSp-MErA4SRWEnKnyZnXkBZKdFkUtFoT6R2GdL4WesBAbXCAyyjbTuUVLZBPWBpph6tbIdMWiyt2XsP5q9cbiOA6DtyssimLIi007YuxWYTg02GTLf4MgOM30hq1AcCyea3ENDxvMcPm3zB8hYlZKbgqlvRRkHuM3Yfn-2fBgQuKrmk_gCEk_ty9JqoNhewQWIIWVg1hOuBULTAgPAvoHMFQJjXtEEc-bHeuQpmKOciqhcuIfvYdcv5KrWv_js90imVQS6j_aSAaP4sZMn8RLDtG0pms7F3X4Ocmbb2jtA7LOvhsa4NHLdxRZfjhuUodrV2IxmDQPW4DRiiacERtM0CVHV36ND1N9VW5x5Accv3ylsaivG_8uocpnAozbi5oE3x2A5MnW3pve_L3lv8DWuBBnv_zVnyGabEMJovXNwmchE2bYriHAk-evC79-7Lkn9gOClviXhaxRbJHERpGlqrBD_V8c1xtqbSwfkHHFxD3ePQ7W1LQZ03Fif9F5jWWziu1TmrQG03H6dE_9c1tEBfbYHy4UNBg40DyJ9U6p7ZEw3-AO3ExmzNV7avdk7ghXbwb6HvaVpOXPww4w5zprTh4i_DlFl_LTbijoSf_i9CK7qbwKJMwdtC7vaAnIsJn3zZA6rnzCmE4SqEmhCDncrlYlJo8acp2Cbgw4kp4O_yfrcR_ZrsliitA6itadteQLnF-jKboDo-XTPEqCB5azCgojPyKhxc5XbvMeKi5SYnsrzlxKotK1cnmLL6q9f2L3CearK4SBO7gf_2aUH6BX35_MFqsaISm9v_9yA16gJz7MpuPJ8IF_ttlch3OeUr3Nv4sSYFsU1j-RBMnopagkdlW7D8f-497O_m6dBxXF_1oyFqunAey2q1kfCPCDci2Us_2JdWH9mlDNyYnIOvfS9DWiw5XAO7d4DSicpFFzpc8EKQylEgsKK15mP-LM_24OC-J5yXoCBa8ZNDS8_vQ95QNlFeeK8gwtpma-T29UZkd3RVtIsK5gHJWkbVNVXkQBNC5QrMQaSnD2O2Zrqo5i88U9eGIMXA1lbwkkH1dnEHfCMbY0sTsPvLpBuXfJnO4oS8s5Fv1viZhsAREmlIMz8-6O10Ulbp9JTGhIJs800OwAxLcSxyuAuJCDuuMI5Df4C331_HWB07PlrVm37cewDGyi7yaCaDCJE5twQvo_5wC2y_fyGxUBqJarcyV6W1arWSODhn_JIJ6rRTyxIGmleOPb4Dm8OzSiiVryrhDxR_y_yMFyA0KUa7tApFalEOXtszqDUJybRwAwvnCalUyHgkjno7Tzm7lUcBUNQ.2WE8DD1a80WrTl1BXRWTsA",
        #"__Host-next-auth.csrf-token": "2a0fcf698ccc46649f766e22743d679abe11df40e5fc9dd27fd6163abb62ca69",
        #"__Secure-next-auth.callback-url": "https%3A%2F%2Fdesktop.captions.ai%2Fprojects%3Fprovider%3Dmicrosoft%26stableId%3DB_jzPRiROqDc6TasXYvqn",
        #"stableId": "B_jzPRiROqDc6TasXYvqn",
    }
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "if-none-match": "\"ttnzsdn1sd13i\"",
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    try:
        response_json = response.json()
        #print(response_json)
        access_token = response_json["accessToken"]
    except:
        print("Error getting access token:",response, response.text)
    return access_token

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": f"Bearer {get_token()}",
    "content-type": "application/json",
    "origin": "https://desktop.captions.ai",
    "priority": "u=1, i",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "x-app-version": "1.0.0",
    #"if-none-match": 'W/"7b1-FXZ8WNDU14epM2IAKPFy5a+/2FM"',
}

def submit_generation(ts, avatar_id):
    url = "https://core.captions-web-api.xyz/proxy/v1/ai-avatar/generate/submit"
    data = {
        "avatarId": avatars_dict[avatar_id]['avatarId'],
        "avatarVariantId": avatars_dict[avatar_id]['avatarVariantId'],
        "transcript": ts,
        "type": "ugc"
    }

    response = requests.post(url, headers=headers, json=data)
    operation_id = response.json().get("data", {}).get("operationId")
    return operation_id

def check_upload_status(fileId, eTag):
    upload_headers = headers
    if eTag != "":
        upload_headers["if-none-match"] = eTag
    status = ""
    response_url = ""
    new_eTag = ""
    url = f"https://core.captions-web-api.xyz/file/v1/upload/{fileId}"
    response = requests.get(url, headers=upload_headers)
    if response.status_code == 200:
        response_json = response.json()
        status = response_json['status']
        response_url = response_json['url']
        new_eTag = response.headers['etag']
    else:
        print("Error:", response.status_code, response.text)
    return status, response_url, new_eTag


def check_generation_status(operation_id):
    fileId = ""
    progress = 0
    url = "https://core.captions-web-api.xyz/ai-avatar/v1/generate/status"
    data = {
        "jobId": operation_id
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(response.text)
        response_json = response.json()
        if 'fileId' in response_json:
            fileId = response_json['fileId']
        if 'progress' in response_json:
            progress = response_json['progress']
    elif response.status_code == 500:
        print("Request failed with status code:", response.status_code)
        return "error", progress
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)
    return fileId, progress

def generate_transcript(phrase):
    ts = ""
    phrase = phrase + "\n"
    itterations = 800 // len(phrase)
    for _ in range(itterations):
        ts += phrase
    return ts, itterations


def display_avatars():
    print("")
    for k, v in avatars_dict.items():
        print(f"{k}. {v['name']}")
    chosen_id = int(input("\nWhich avatar you'd like to use? (type number): "))
    return chosen_id


def ensure_directory_exists(directory_path: str):
    os.makedirs(directory_path, exist_ok=True)

def download_mp4(url: str, save_path: str, file_name: str):
    try:
        ensure_directory_exists(save_path)

        file_path = os.path.join(save_path, file_name)

        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
        return False

