import streamlit as st

st.title("宇宙と海の質問回答Webアプリ")
st.write("##### このWebアプリについて")
st.write("多くの謎を秘めた宇宙と海に関する質問回答Webアプリです。")
st.write("##### 動作モード2:質問回答 ")
st.write("ジャンルと質問を入力することで、回答を表示します。")

# ジャンル選択
selected_item = st.radio(
    "ジャンルを選択してください。",
    ["宇宙の謎", "海の秘密"]
)

st.divider()

# テキスト入力
if selected_item == "宇宙の謎":
    input_message = st.text_input(label="宇宙の謎についてのあなたの好奇心に答えます。テキストを入力してください。")
    text_count = len(input_message)
else:
    input_message = st.text_input(label="海の秘密についてあなたの探求心に答えます。テキストを入力してください。")
    text_count = len(input_message)

# 実行ボタン
if st.button("実行"):
    st.divider()

    if selected_item == "宇宙の謎":
        if input_message:
            st.write(f"文字数: **{text_count}**")

        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

    else:
        if input_message:
            st.write(f"文字数: **{text_count}**")
        else:
            st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

