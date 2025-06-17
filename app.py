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
    'SRT30': '1750162162',
    'page_uid': 'jaaj9sqVJLhssfzS4GsssssssUZ-224929',
    'nhn.realestate.article.rlet_type_cd': 'A01',
    'nhn.realestate.article.trade_type_cd': '""',
    'nhn.realestate.article.ipaddress_city': '1100000000',
    '_fwb': '113w8jjFH5TGUTMbGRiBLNf.1750162120152',
    'landHomeFlashUseYn': 'Y',
    '_fwb': '113w8jjFH5TGUTMbGRiBLNf.1750162120152',
    'NID_SES': 'AAABvfQbqm1F9eXPeSyJi1fdJTlpeFfJGMy/qHJQxMXiQWKr8/2D8NRavIHstQO6gtILELVNz3rlT8D+pDz5OChAT7CUHImKVtiBBQ1eURCN1AG/EdYXPZ6GZG3ivF7r5ObVtDla4H0KFOoLoeXK2IorWBcZE8IQ94W9jGngKrCFrHvqyeqZZ3F8dXQ+lYSIn3dcVN7WboKbvPaEbI6F6p8jlOvHdZdegJ8mWMvTL+NS9Hz4tlW+EFJy8VLn/In5q/eqcITnqrZFBhca/tef5frKTO9tE2NA0tuVHniW+wm4K+UWNUavmCD7K2ubwU5VNA68+QHf0zoyXpRmVSQW77ET59EiuWkOFhMS5EyTGucb0k8Aa9TMiKWg8/TPGb7k6JHJj7e0FkGY71U6LtI43xuHd1bXLgTb4MQJFiIut6ZMwepzzoOfJJ0gazZPQq9EUhEQPR0XZM1lgKfeQgj0GpEMAJYoto61G/yWSQzClnEnI4NOpOMO/TMFts2GsEbvgJsWKYkjaH3XTtTE5kQuuoqZMmz7X09mDkDcRO7M5c/qWmF0MG3+kbO2oIA/PwFz1jKlLVJwlYC6KUNK8YQw20bP0lM=',
    'SRT5': '1750166706',
    'REALESTATE': 'Tue%20Jun%2017%202025%2022%3A30%3A19%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'PROP_TEST_KEY': '1750167019410.359abaadedb8a570068c3ce5bbef1deebc7f2c5a44a37c30a92f6c59ecae9811',
    'PROP_TEST_ID': '6c9a7f31d79e3a247aebc04adac43927ca9728655e30f34e207d2f28e615b450',
    'BUC': 'EgVrJOA5lXRHq7tjHzfLtiTxIFCbjlWp6NzKFONubyQ=',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NTAxNjQ4OTYsImV4cCI6MTc1MDE3NTY5Nn0.OYzpcaRhuc6-pVKQIEw4OhPNt3QNWIrhiSUqia0cL6A',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/houses?ms=37.4763358,126.9210951,18&a=VL&b=A1&e=RETAIL&h=15&i=51&ad=true',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'NNB=4OZOYZDNTYJGO; ASID=b765abe900000192b4624be40000004d; nstore_session=oIBAyZjK8Su+JSDr7idwCXUx; recent_card_list=115,1294; _ga=GA1.2.2045887801.1733061999; nstore_pagesession=iHMv5lqlZTr7OwsLUWR-296388; NFS=2; NAC=ytiQBUw5QeyXB; nid_inf=-2054095709; NID_AUT=jo0oYsQi9vqKBF0iFFxtNuUnrAGbg/25ccZWuT4bgI7PMfDyGNQmXEKdhyhnj7QH; NACT=1; SRT30=1750162162; page_uid=jaaj9sqVJLhssfzS4GsssssssUZ-224929; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=113w8jjFH5TGUTMbGRiBLNf.1750162120152; landHomeFlashUseYn=Y; _fwb=113w8jjFH5TGUTMbGRiBLNf.1750162120152; NID_SES=AAABvfQbqm1F9eXPeSyJi1fdJTlpeFfJGMy/qHJQxMXiQWKr8/2D8NRavIHstQO6gtILELVNz3rlT8D+pDz5OChAT7CUHImKVtiBBQ1eURCN1AG/EdYXPZ6GZG3ivF7r5ObVtDla4H0KFOoLoeXK2IorWBcZE8IQ94W9jGngKrCFrHvqyeqZZ3F8dXQ+lYSIn3dcVN7WboKbvPaEbI6F6p8jlOvHdZdegJ8mWMvTL+NS9Hz4tlW+EFJy8VLn/In5q/eqcITnqrZFBhca/tef5frKTO9tE2NA0tuVHniW+wm4K+UWNUavmCD7K2ubwU5VNA68+QHf0zoyXpRmVSQW77ET59EiuWkOFhMS5EyTGucb0k8Aa9TMiKWg8/TPGb7k6JHJj7e0FkGY71U6LtI43xuHd1bXLgTb4MQJFiIut6ZMwepzzoOfJJ0gazZPQq9EUhEQPR0XZM1lgKfeQgj0GpEMAJYoto61G/yWSQzClnEnI4NOpOMO/TMFts2GsEbvgJsWKYkjaH3XTtTE5kQuuoqZMmz7X09mDkDcRO7M5c/qWmF0MG3+kbO2oIA/PwFz1jKlLVJwlYC6KUNK8YQw20bP0lM=; SRT5=1750166706; REALESTATE=Tue%20Jun%2017%202025%2022%3A30%3A19%20GMT%2B0900%20(Korean%20Standard%20Time); PROP_TEST_KEY=1750167019410.359abaadedb8a570068c3ce5bbef1deebc7f2c5a44a37c30a92f6c59ecae9811; PROP_TEST_ID=6c9a7f31d79e3a247aebc04adac43927ca9728655e30f34e207d2f28e615b450; BUC=EgVrJOA5lXRHq7tjHzfLtiTxIFCbjlWp6NzKFONubyQ=',
}

# ✅ 데이터 가져오는 함수
@st.cache_data
def fetch_data(min_price, max_price, min_area, max_area):
    all_data = []
    for page in range(1, 4):  # 1~3페이지
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

    # ✅ 컬럼 체크 및 안전 필터링
    selected_cols = [
        "articleNo", "articleName", "realEstateTypeName", "tradeTypeName",
        "floorInfo", "dealOrWarrantPrc", "areaName", "direction",
        "articleConfirmYmd", "articleFeatureDesc", "buildingName", "realtorName"
    ]
    available_cols = [col for col in selected_cols if col in df.columns]
    df = df[available_cols]

    # ✅ 테이블 출력
    st.dataframe(df, use_container_width=True)

    # ✅ 다운로드 버튼
    st.download_button("📥 CSV 다운로드", df.to_csv(index=False), file_name="관악구_빌라_매물.csv")

    # ✅ 첫 매물 상세 JSON 보기
    with st.expander("🔍 첫 매물 원본 JSON 보기"):
        st.json(data[0])
else:
    st.error("❌ 매물을 불러오지 못했습니다. 쿠키 또는 토큰이 만료되었을 수 있습니다.")
