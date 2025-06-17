import streamlit as st
import requests
import pandas as pd

st.title("Streamlit 부동산 테스트")
st.write("앱 정상 실행 테스트용입니다.")

st.dataframe(pd.DataFrame({"Hello": [1, 2, 3]}))
