import requests

def ask_perplexity(api_key, user_input):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code == 200:
        try:
            return res.json()["choices"][0]["message"]["content"]
        except:
            return "❌ 回覆解析失敗，可能是格式錯誤或回應結構變動。"
    else:
        return f"❌ 回覆失敗（HTTP {res.status_code}）：{res.text}"