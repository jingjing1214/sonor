import streamlit as st
from recipe_scraper import search_recipes
from chatbot import ask_perplexity

st.set_page_config(page_title="冰箱食材推薦系統", layout="wide")
st.title("🥬 冰箱食材 X 食譜推薦")

with st.sidebar:
    st.header("🔧 設定")
    api_key = st.text_input("請輸入 Perplexity API Key", type="password")
    default_ingredients = st.text_input("請輸入冰箱食材（用逗號分隔）", "雞肉, 馬鈴薯")

if api_key:
    st.subheader("🔍 推薦食譜")
    if st.button("推薦食譜"):
        with st.spinner("搜尋中..."):
            try:
                results = search_recipes(default_ingredients)
                if results:
                    for title, url, snippet in results:
                        st.markdown(f"### [{title}]({url})")
                        st.markdown(f"> {snippet}")
                else:
                    st.warning("❌ 找不到食譜，請確認關鍵字或稍後再試。")
            except Exception as e:
                st.error(f"⚠️ 食譜搜尋失敗：{e}")

    st.subheader("🧠 與料理助理聊聊")
    user_input = st.text_input("輸入你的問題")
    if user_input:
        with st.spinner("Perplexity 回覆中..."):
            reply = ask_perplexity(api_key, user_input)
            st.write(reply)
else:
    st.warning("請在左側輸入 Perplexity API Key 才能使用功能")