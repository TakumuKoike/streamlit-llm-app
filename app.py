import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


st.title("～宇宙と海の神秘～")
st.write("##### このWebアプリについて")
st.write("多くの謎を秘めた宇宙と海に関する疑問に答えるWebアプリです。")
st.write("##### 1.ジャンル選択 ")
st.write("質問するジャンルをラジオボタンで選択してください。")

# ジャンル選択
selected_item = st.radio(
    "質問ジャンル",
    ["宇宙の謎", "海の秘密"]
)

st.divider()
st.write("##### 2.質問入力と回答表示") 
st.write("「質問欄」に質問を入力し、実行ボタンを押すと回答が表示されます。")
input_message = st.text_input(label="質問欄")


#「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数
def get_llm_answer(input_message, selected_item):
    # ChatOpenAIクラスのインスタンスを作成
    llm= ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    # システムメッセージのインスタンスを作成
    if selected_item == "宇宙の謎":
        system_message = SystemMessage(content="You are a helpful assistant who answers questions about space from users.")
    else:
        system_message = SystemMessage(content="You are a helpful assistant who answers questions about sea from users.")
    # ユーザーメッセージのインスタンスを作成
    human_message = HumanMessage(input_message)
    # メッセージのリストを作成
    messages = [
        system_message,
        human_message
    ]
    # LLMにメッセージを送信
    result = llm(messages)
    # LLMからの応答を返す
    return result.content


# 実行ボタン
if st.button("実行"):
    st.divider()
    if input_message:
        answer = get_llm_answer(input_message, selected_item)
        st.write(f"回答: **{answer}**")
    else:
        st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")