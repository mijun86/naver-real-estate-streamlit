import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="관악구 빌라 실시간 매물", layout="wide")
st.title("🏡 관악구 빌라 실시간 매물 리스트")

# 👉 사용자 필터 입력
st.sidebar.header("🔎 필터 설정")
min_price = st.sidebar.slider("💰 최소 가격 (만원)", 0, 90000, 0, step=500)
max_price = st.sidebar.slider("💰 최대 가격 (만원)", 0, 90000, 90000, step=500)
min_area = st.sidebar.slider("📐 최소 전용면적 (㎡)", 0, 100, 0, step=1)
max_area = st.sidebar.slider("📐 최대 전용면적 (㎡)", 0, 100, 51, step=1)

# 👉 아래에 본인의 Cookie / Header 정보를 넣으세요
cookies = {
    'NNB': '4OZOYZDNTYJGO',
    'ASID': 'b765abe900000192b4624be40000004d',
    'nstore_session': 'oIBAyZjK8Su+JSDr7idwCXUx',
    'recent_card_list': '115,1294',
    '_ga': 'GA1.2.2045887801.1733061999',
    'nstore_pagesession': 'iHMv5lqlZTr7OwsLUWR-296388',
    'NFS': '2',
    'NAC': 'ytiQBUw5QeyXB',
    'nid_inf': '-2054095709',
    'NID_AUT': 'jo0oYsQi9vqKBF0iFFxtNuUnrAGbg/25ccZWuT4bgI7PMfDyGNQmXEKdhyhnj7QH',
    'NACT': '1',
    'page_uid': 'jaaj9sqVJLhssfzS4GsssssssUZ-224929',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '113w8jjFH5TGUTMbGRiBLNf.1750162120152',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '113w8jjFH5TGUTMbGRiBLNf.1750162120152',
    'SRT30': '1750170828',
    'SRT5': '1750170828',
    'NID_SES': 'AAABtKx0gfIOgkPjJJWX/T/L8uGQTEWbMUo2dhGFb8tRns/4MHKHRFaXJY92NSfbrmEcKVl2T75wAZ7rHrEkiAHJTYk3EJp/dGSw9o3Fqq9ecj3etdJUP3Y2mY2dzb8yKoxVYGQk3GuSIB/9FtlwKJ6F8FC6zB4xyS/dhfae26RH/0FyYzfxfAHyOT2t9R2Exa3m4E1cGsAK/iP+45OgE2fJQyDHEt3hV18HB5+6K9U1qW2RdKe55IRhJFhf0AT+W6QWPrc2gBglEFmcOyCiQOExXhFSmqnz0+LHK7SsATFYQZVuiSQ75jxHnLmeGOzFB7YAiREEZHbQTxvAytWt8B4k16ACPOUoo0jH6o69RatdT9IBxUL9+5rRNLTeI/D7gEe+bCFg38tpKcpZiuuNR1uNF+AuPYUQx3vCbbxGiR4KwKVvS5D1UaIBlJS/y2zEBVV2Gem2kHoKctMqSC/aFwCpB/QpnMXR+spptfcJUfocr0Q2nI7YyQoFzQipkS/7BZA2SCI+w/U4oNq8aiA5FnPQg/VGPUcBs5dKbH+oCcNQmcZNHMe2oRsYY8eSKhgWG6iC648jnL7q09dHPfQnxZz0HAk=',
    'REALESTATE': 'Tue%20Jun%2017%202025%2023%3A34%3A42%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'PROP_TEST_KEY': '1750170882349.ec3bc9b2d3b46d21c2a05775944c52523f66d747ba1a8b1d7d6721308ee8fcf9',
    'PROP_TEST_ID': '02d33b5d533e17817c2977fb3ab903cc51820954c4c2727bb31df5322df7cb77',
    'BUC': 'vhmvCQLFk-dasyjyYI64XT9RJHswvkI1dmK7Y9O0kbQ=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NTAxNzA4ODIsImV4cCI6MTc1MDE4MTY4Mn0.huVrcENrRCqahYQgRHiFNx7ef7g_4G7xh_raWug8X8I',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/houses?ms=37.4772271,126.922876,15&a=VL&b=A1&e=RETAIL&h=15&i=51&ad=true',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'NNB=4OZOYZDNTYJGO; ASID=b765abe900000192b4624be40000004d; nstore_session=oIBAyZjK8Su+JSDr7idwCXUx; recent_card_list=115,1294; _ga=GA1.2.2045887801.1733061999; nstore_pagesession=iHMv5lqlZTr7OwsLUWR-296388; NFS=2; NAC=ytiQBUw5QeyXB; nid_inf=-2054095709; NID_AUT=jo0oYsQi9vqKBF0iFFxtNuUnrAGbg/25ccZWuT4bgI7PMfDyGNQmXEKdhyhnj7QH; NACT=1; page_uid=jaaj9sqVJLhssfzS4GsssssssUZ-224929; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=113w8jjFH5TGUTMbGRiBLNf.1750162120152; landHomeFlashUseYn=Y; _fwb=113w8jjFH5TGUTMbGRiBLNf.1750162120152; SRT30=1750170828; SRT5=1750170828; NID_SES=AAABtKx0gfIOgkPjJJWX/T/L8uGQTEWbMUo2dhGFb8tRns/4MHKHRFaXJY92NSfbrmEcKVl2T75wAZ7rHrEkiAHJTYk3EJp/dGSw9o3Fqq9ecj3etdJUP3Y2mY2dzb8yKoxVYGQk3GuSIB/9FtlwKJ6F8FC6zB4xyS/dhfae26RH/0FyYzfxfAHyOT2t9R2Exa3m4E1cGsAK/iP+45OgE2fJQyDHEt3hV18HB5+6K9U1qW2RdKe55IRhJFhf0AT+W6QWPrc2gBglEFmcOyCiQOExXhFSmqnz0+LHK7SsATFYQZVuiSQ75jxHnLmeGOzFB7YAiREEZHbQTxvAytWt8B4k16ACPOUoo0jH6o69RatdT9IBxUL9+5rRNLTeI/D7gEe+bCFg38tpKcpZiuuNR1uNF+AuPYUQx3vCbbxGiR4KwKVvS5D1UaIBlJS/y2zEBVV2Gem2kHoKctMqSC/aFwCpB/QpnMXR+spptfcJUfocr0Q2nI7YyQoFzQipkS/7BZA2SCI+w/U4oNq8aiA5FnPQg/VGPUcBs5dKbH+oCcNQmcZNHMe2oRsYY8eSKhgWG6iC648jnL7q09dHPfQnxZz0HAk=; REALESTATE=Tue%20Jun%2017%202025%2023%3A34%3A42%20GMT%2B0900%20(Korean%20Standard%20Time); PROP_TEST_KEY=1750170882349.ec3bc9b2d3b46d21c2a05775944c52523f66d747ba1a8b1d7d6721308ee8fcf9; PROP_TEST_ID=02d33b5d533e17817c2977fb3ab903cc51820954c4c2727bb31df5322df7cb77; BUC=vhmvCQLFk-dasyjyYI64XT9RJHswvkI1dmK7Y9O0kbQ=',
}

# ✅ 데이터 가져오기 (최대 8페이지 = 160건)
@st.cache_data
def fetch_data(min_price, max_price, min_area, max_area):
    all_data = []
    for page in range(1, 9):  # 최대 8페이지 조회
        url = (
            f"https://new.land.naver.com/api/articles"
            f"?zoom=18&leftLon=126.9160901&rightLon=126.9261001"
            f"&topLat=37.4782217&bottomLat=37.4744498"
            f"&order=rank&realEstateType=VL&tradeType=A1"
            f"&priceMin={min_price * 10000}&priceMax={max_price * 10000}"
            f"&areaMin={min_area}&areaMax={max_area}"
            f"&page={page}&priceType=RETAIL"
        )
        res = requests.get(url, headers=headers, cookies=cookies)
        if res.status_code == 200:
            try:
                articles = res.json().get("articleList", [])
                all_data.extend(articles)
            except Exception as e:
                st.error(f"⚠️ JSON 파싱 오류: {e}")
        else:
            st.warning(f"❌ {page}페이지 요청 실패: {res.status_code}")
    return all_data

# ✅ 데이터 시각화
data = fetch_data(min_price, max_price, min_area, max_area)

if data:
    st.success(f"📦 {len(data)}건의 매물 데이터를 불러왔습니다.")
    df = pd.DataFrame(data)

    # ✅ 링크 추가
    df["매물링크"] = df["articleNo"].apply(
        lambda x: f"https://new.land.naver.com/articles/{x}"
    )

    selected_cols = [
        "articleNo", "articleName", "realEstateTypeName", "tradeTypeName",
        "floorInfo", "dealOrWarrantPrc", "areaName", "direction",
        "articleConfirmYmd", "articleFeatureDesc", "buildingName", "realtorName",
        "매물링크"  # ✅ 링크 포함
    ]
    available_cols = [col for col in selected_cols if col in df.columns]
    df = df[available_cols]

    st.dataframe(df, use_container_width=True)

    st.download_button("📥 CSV 다운로드", df.to_csv(index=False), file_name="관악구_빌라_매물.csv")

    with st.expander("🔍 첫 매물 원본 JSON 보기"):
        st.json(data[0])
else:
    st.error("❌ 매물을 불러오지 못했습니다. 쿠키 또는 토큰이 만료되었을 수 있습니다.")
else:
    st.error("❌ 매물을 불러오지 못했습니다. 쿠키 또는 토큰이 만료되었을 수 있습니다.")
