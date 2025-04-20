import requests
import os
import certifi

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
        "__Secure-next-auth.session-token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..8UVrbrIfD-qhdLZ5.J8X9TIPO7ZDeFKjuDB2g5KSxMJoVqxyekPnTOnV69tdjJIcnyWghN761X6JtzHu5Rg9_Y486xaGw_DT7YlzlHh-FMkcvEtmuzUzngFfC7LlVDdMcRwGf1Kp07A5HaOGTHy7PlOpbu8kAOuptVrhmeLEIYjaMMsE9LrqniiwDokXT5_Y-V1eobr8HeBIGRTb6dd4ySzGsvYqLjv4aoZozP4a5RHztdTmvTcotQdy6a-Tuojm0HNSnqaLXseyUX3mwACnSjs9QKrd7-w-SQSY1JdeT9owVU-J88wrh_PR4MiT30_Jfcs1yDdywG1RwATR5BecSeGLZe-O4bcEHKfV_B_BBqKgseybeB79ZPGoKNEWk6urQdoNiGUdCuy9Rs_jLTeVEHFVarqAqazyccvKH6YOqTcSb323Wn3ZddOyyTV39EyrBDzDXEqqHzpbNglcGhIhEKYgxlRGDCrtO9Rg4Ey-ztdfml0jy0CPee5hJ69ST4eLVhBY2Vp9SWrLJyrcQNctDNmZofje9nYy4knWlROYfsj5qx8GO0Q58kBEKpanQo_x0_7IxmHaUykqYiCRhl0bI_23ARNN0DT_QmJrb5JCguz5sO8yv_HqwgjgKkDXQfqOBp7TVDRWX21FglQVe-QluX_7Lp7smteHbP_6T53BTYfROOQtpLOruQF3CNqcOQDBYZzBYRF5867lauWnEYEgVw5NYNjHtLTS9xBsDFD380MGjLvPDVncbLAm-GF6kXGXfnUUQy52nWKBmL-gg66brL4faQ2OEKnIkDPS5Uy8bqkoFq_Gn9kr-1nUC6iHCoGsBaLjgxGnyA5v7TNE0CVFrhedXhfZOUK8mrT4n7Q1fQNvalI3l2EzT6qXbm99jL7gcJbRaWw1LvzLh00JwI3r6fYLynrAbTWHmA_un87rGD1l2LPwewhtep0_KneF_BstAkKVSz0iGYFZtouzoOmXoe8dhI1_yHzrz1kinr87moWNvYLBIv7OjLo0vjAWO62thf3J3XRuDw11mPe9tAUO5Y8H8SmKOHqtq5G3AairrtCbtIoUlKoIpRnys3RTZheWs1tgx_PxD2pA8Zpog6r_nd4APNDxOKzHopx4VWRXavmzX9PQwjdAM75Sy-6EQQsoTbEQxqXDZTCO_cbI5sKTSLd8gXAQH2h_4CE1Vv4WrFqW-cSuetezR67f1PYQFUjlKY1X43QUPEdUL141ks5Sn4Aiw0n4rInz_AUG1ArN7QlaN7PG2NzTDhbCXkrjEX6Jlnd2TnaaCz6HkJI_EB4NoR_awfWyqk4Afqb2p_LvlEynoCMkfGqnjjMru_qo7TkHBCXKbVDUpuDPPnAgZ9ApaYk8Zg93gcbfyLErEsJg6L3vy4AjfsRUKiyY4b7RRgDBDriZ2XrbdGLP9gAV762Sj9WWW1YXZ7LVQaM5tQFsr-KZ3JaHzlWTYm13Vep7CYniRTVWgipbT5wZ_qlOIirZgpSHMFatuDJhsWpOqx4dsBdY6HiyIP0Mldwb7Uvi5x7QvMPaN3_cG0KNAasUw-KoGFBpAZsY6rTyn5leMi-YgnEbGf2Kc_SnwcSunbzcsrd2Whr9lJOCiHOcEfXmH4AVS_LhuDeqeucueaDMX0DYaB10pxxiPf6lZBeHNvekMf6cT6bU8nmy35I6DTnMd4bLtj7rZMqJNLvqyRKtVPh4BTgbPS6600psYFQEnatMWmfu0uESvPzef4k86BiyiMjeJ5brlfcY2XpQgHwj09JKeZ7Rftm0OFk8cPVTIiL6DRpLq8yKIVsnfyIael5k6C90tW7wq-Ui8SY4appmF3V6TE0q3o8g4GIe82xpOfSN8x7cpA90cElXHjTX7n8UcsTaGo8Gbdme7QUA0MIHuL73NsUW_gPWIAZ5GYV5JPcP4KjCaiN_JXUoh3zumN_Z-iQd9wVdBImWS2mzQE2RYQ_-JZGG5dkfEKzwFWFv7uEDIwxG_AIMp82IROLapJp6yHnbe004L27gWP9H_-nth7cd3RjtIEsPSQ2jSuPFzWqvx3i1xYOY3h89SSGjGs2FvwjAspJbFnac.CEltGfFkMcNSLO_ooYJzVg",
        #"__Host-next-auth.csrf-token": "2a0fcf698ccc46649f766e22743d679abe11df40e5fc9dd27fd6163abb62ca69",
        #"__Secure-next-auth.callback-url": "https%3A%2F%2Fdesktop.captions.ai%2Fprojects%3Fprovider%3Dmicrosoft%26stableId%3DB_jzPRiROqDc6TasXYvqn",
        #"stableId": "B_jzPRiROqDc6TasXYvqn",
    }
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "if-none-match": "\"ttnzsdn1sd13i\"",
    }
    response = requests.get(url, headers=headers, cookies=cookies, verify=certifi.where())
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

