import streamlit as st
from chatbot import ask_perplexity

st.set_page_config(page_title="冰箱食材推薦系統", layout="wide")
st.title("🥬 冰箱食材 X 食譜推薦")

with st.sidebar:
    st.header("🔧 設定")
    api_key = st.text_input("請輸入 Perplexity API Key", type="password")
    ingredients = st.text_input("請輸入冰箱食材（用逗號分隔）", "雞肉, 馬鈴薯")

if api_key:
    st.subheader("🍽️ AI 食譜推薦")
    if st.button("推薦食譜"):
        prompt = f"""我冰箱裡有：{ingredients}。
請推薦一個可以做的料理，請以以下格式回覆：

🍽️ 料理名稱：
🧂 所需食材：
🧑‍🍳 烹調流程：（請用 3~5 步驟分段說明）"""
        with st.spinner("AI 正在設計食譜..."):
            result = ask_perplexity(api_key, prompt)
            st.markdown(result)

    st.subheader("🧠 與料理助理聊聊")
    question = st.text_input("輸入你的問題")
    if question:
        with st.spinner("AI 回覆中..."):
            reply = ask_perplexity(api_key, question)
            st.markdown(reply)
else:
    st.warning("請在左側輸入 Perplexity API Key 才能使用功能")