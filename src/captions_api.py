import requests
import os
import certifi

avatars_dict = {
    1 : {"avatarId": "ctUFWc7w2BtCwqfq4Vht", "avatarVariantId":"qeOAFWe7BCCwOIClvcYi", "name": "Violet (Asian) - Walking in the park"},
    2 : {"avatarId": "RuHyXqTQtifCAuHtmVMq", "avatarVariantId":"P6seXiz486l1nQid0QRT", "name": "Madison - Talking in the gym"},
    3  : {"avatarId": "B5VqhL8HPvPw8VZ4H5Uf", "avatarVariantId":"QveuIuGdwcLmtHpgGoTy", "name": "Ashley - Walking"},
    4 : {"avatarId": "lE6CMlmTY73GvrVlsbdS", "avatarVariantId":"oo0RAIESofBfKGEes2BL", "name": "Jason (Asian) - Sitting and talking"},
    #5 : {"avatarId": "XtofXWKaS7jz3nsSq5fD", "avatarVariantId":"XtofXWKaS7jz3nsSq5fD", "name": "Mia - Custom Max"},
    5 : {"avatarId": "nYH2Gn0rgTxhwtZXyLxG", "avatarVariantId":"YuE1bYHzRL3XFB9eKPN6", "name": "Mia - Balck girl"},
    6 : {"avatarId": "ctUFWc7w2BtCwqfq4Vht", "avatarVariantId":"ygnhskO6v8ns3FGf7YmO", "name": "Violet (Asian) - Sitting in the room"},
    7 : {"avatarId": "QaWH43qm3Otrx9HpYC4v", "avatarVariantId":"u0RHSdvb4u1eFWP6gsFG", "name": "Douglas - walking in the park"},
    8 : {"avatarId": "18hzwOYNXUEGIFN3TUzn", "avatarVariantId":"Ug6wfqvLEpb5TeD4LHGl", "name": "Paul - walking on the beach"},
    9 : {"avatarId": "VxQYalyR5z6CGc5vJo52", "avatarVariantId":"oU0MtgyCTw1Ban2ktyl1", "name": "Jim - sitting in the office"},
    10 : {"avatarId": "sTknfC0E67IEebnZfsDU", "avatarVariantId":"BD0ByZURuboedGWCDiyx", "name": "Gary - walking in the park"},
}

def get_token():
    access_token = ""
    url = "https://desktop.captions.ai/api/auth/session"
    cookies = {
        "__Secure-next-auth.session-token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..eOgP4U7KikYjWIDZ.yHzM96OUHuhLZsJoEJ42-ZilsQbSzeqDfiq6xEx6ghYHYNOEUW4A625VyNTpfixBQsZBQKS3p6Jue9URDrmERfiJbeFYKwNLM5gxCIr-AHbNcBRyUBrWctfyMwVKvyuF2lbEIO1tuShS5Cxb0MsYhgI5wpckRCjKmD351_RAxZ_I-ZjftWRj9CoZVccnprFIq57X8oz9xrVWqIBoXhEpK9CJugrAQThCib2d9urykdnJs6l0NFR1tlHOmq_-T5L0PliJxynSJ5iXDKtIIbqc5bIxU-wI8QwfVEkydr3xzbZ0v3zr4qbSndRxg5eVxOI9m1yJTbOsDY3UYVMLKwDLToetkcm3kZuIbdpgujboWtXLwZefOvh1bCxJUl7-YZdXUzqoC-ZkLAXlKg8iXrXz58ZoaJ6A-_Z3o6NIKiqX23eGh9l1AikEZabJ8d80Bwjj4VAB36C4Kdn63Nr46CU1LyGAhLMU-oaok78vpEKReStUs48puzMwE1fMfg-cUQBXNOInGxEYXXRDEp4mRZ-iXo73e1ocsuL2L6GfpIvLMg9Ckg6ABalwJm8Rll4VeJiRyFeA2Adz06q0Y3cokOoJOhtsf6qLVIFlFkcvsRKbrHS0sZpt_iCEqlsZ9XzFjjXagnqSby_CeX8VGRdO2rV0styHb_aA-_G7BHPrpKjX11XkofIFoH4F4Lui403ie-bzWn_UJcsdi4GHnXpQvKkkEBP_Ez-3vdPUJcJdaWxguk-GT7chFUwH9BN14tfkbkH3mXnzzeAe6yfjNSFhLQ4bBIQ4MHLq6Qae0E5KD6t9MRG994Q9uRsa2OH_dm-b9rVX2EvrzoAeICbjEVZUADtOkpDgyJPMJhKEIlwuhfI-XVsHPsM2tPmlBDFTnEQGgeN1Fu_boG6i_AgBCaI-Tvzvfx97Gbg4Q0t0QmwfxOSmt0MnuE5RoZwMKCk0KX_3lm-vyyc9JurY7ZVf0TezLKw2Ng1TydoVH3J65OXx8IqhCc-MX3UMBbc7qAdhWMvDODoZRrjT08aBivcQW1_qZKyx2quZYrhOU2ms0uigumh4PEzBIxDEruvjFfWccRfeTGgJM1Wu-MrmApGpNPxaLLm7VGr5cHInSxkZPMXoShMtsSCPzu1N2oShRREQSiGilG4luh7w5dvVz92sI1J6mk95ieopQGBURYQpe8BMQ8B1QslK-qgIp27yBM0feQyPYuRkmkVlfhqVxHh7-ZbpCk8T08Eh2rj2WWGSgVJpCQBf5iXOP80I7p7jNzp2z0Uv1iH4lar-8hyYY2jTnXKQDuAGf3D07FRYiu2L3olwiFHwW83A1mYRe0wmWnBYUB8gtz4YqpUBL50RKbxuls02QzPmMw5xJFnW-EiTzBqdBUII1rVoeEXVe8dX0hnP06XxSNMcqT0u2BgRfyrtfDbmJw_lo7cAjzb2AfEtPsWBz4pNwIXxh6bMabnIzHvjN1Zx_7TGl7NscEPGpHeXVOvohbb8Nn9AKDwuT6hCEwN_qv6TbsOhw9MAefiQjqqOvhBQRjgm8vNbNNQBW_PDL98euEVmITkWP2C7_MmWflUIlv1L4EhCYKo_pBV6gwWwvQDCE3PdUvugfyMZPuboUPyIcptwW6rpSdAWO3Am6Ois70Acin-0b_2z3pf8GkicTPYxBzcI3yuMpn-OmDdhOlIjBP4nFStPnlFG3hUN0LLmqsi8uIKpMjfBYFAx-3LIgSLVotcDQu8NlTcCkb239NKgjQGBFD0PzioFSVmk11nNBdam9A0-24cBaNaqIIrn8rVybfx0sUh0I_gewUOVI_0mTssv-QvhmIMh-cSYKCpY4PYJzNQlsml6bhHZILpVADSRO-G2kZW1a0ij4J_NmoB0dnjMaPGht0dBy4gHeQntIDIimJXdh9ag6nt2HHyp8SM34ovdlsoyvv9iJA5DfvMR5FD4Z-s_UbMMN8BcfTvq1Riid6xkpFLdR0Fb0lFWubrTWB0Xmy-goKRJgickYOYJe5Fm1x-UsUzA7gy0Q-Y3dkxdqdxEPxntafWvegPyvCahvpFs55kSKHfRJus.sdGLMZfYSZj1w0XcNTEFhg",
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
    print(f"{k+1}. Use custom avatar (You need: avatarId, avatarVariantId)")
    chosen_id = int(input("\nWhich avatar you'd like to use? (type number): "))
    if chosen_id == len(avatars_dict) + 1:
        avatar_id = input("Enter avatarId: ")
        avatar_variant_id = input("Enter avatarVariantId: ")
        avatars_dict[len(avatars_dict)+1] = {"avatarId": avatar_id, "avatarVariantId": avatar_variant_id, "name": f"Custom Avatar {len(avatars_dict)}"}
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

