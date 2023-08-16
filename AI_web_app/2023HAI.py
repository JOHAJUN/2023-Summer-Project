from api.AI import AIAPI
import streamlit as st

def main():
    text = None
    st.title(":blue[HAI] SUMMER PROJECT :sunglasses:")
    st.header("1. 이미지에서 텍스트를 추출\n")
    image = st.file_uploader("이미지를 업로드하세요\n", type=['jpg', 'png', 'jpeg'])

    with st.expander("입력된 이미지 보기"):
        text = AIAPI.query_image2text(image, image)
        st.write(text)

    st.divider()

    st.header("2.GPT로 요약하기\n")
    st.subheader("원문")
    if text is None:
        text = ' '
    st.info(text)

    with st.expander("요약본 보기"):
        if text is not None: 
            title, summary = AIAPI.query_text2text(text, text)
            st.subheader(title)
            st.write(summary)
        else:
            st.write("요약본을 생성하기 위한 원문이 없습니다.")

if __name__ == '__main__':
    main()
