import streamlit as st

# Checkbox & Radio Button
if st.checkbox("Show/Hide"):
    st.write("체크박스 선택됨")

status = st.radio("선택 상태:",("Active","Inactive"))
if status == "Active":
    st.success("활성화 되었습니다")
else:
    st.warning("비활성화 되었음")

# 드롭다운 선택
fruits = st.selectbox("좋아하는 과일을 선택하세요.",
 ["사과","배","포도","감","딸기","오렌지"])
st.write("당신이 좋아하는 과일은", fruits, "입니다.")

# 슬라이더
level = st.slider("슬라이더로 레벨을 선택하세요",0,100,10)

# 버튼
if st.button("About"):
    st.text("Streamlit을 이용한 튜토리얼 입니다.")

# 텍스트 입력
first_name = st.text_input("이름 입력하세요.","Type here...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)

#텍스트 영역
message = st.text_area("메시지를 입력하세요.","Type here...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)

# 날자와 시간 입력
import datetime
today = st.date_input("날자를 선택하세요.",datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.",datetime.time())