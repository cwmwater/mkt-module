from datetime import datetime, timedelta
from trendspy import Trends

# 네이버 데이터랩(검색어트렌드) API가 개발자센터에서 종료되어(2026-07-31, NAVER API HUB로 이관 필요)
# 구글 트렌드로 대체. (참고: pytrends는 구글 정책 변경으로 2025년부터 작동 중단되어 미사용,
# 대신 유지보수 중인 trendspy 사용). 국내 검색 트렌드와는 다소 차이가 있을 수 있음(구글 vs 네이버 검색 행태).
def analyze_keywords(keywords: list) -> dict:
    try:
        end_date = datetime.today()
        start_date = end_date - timedelta(days=90)
        timeframe = f"{start_date.strftime('%Y-%m-%d')} {end_date.strftime('%Y-%m-%d')}"

        tr = Trends()
        df = tr.interest_over_time(keywords, geo="KR", timeframe=timeframe)

        if df is None or df.empty:
            raise Exception("검색 트렌드 데이터가 없습니다")

        if "isPartial" in df.columns:
            df = df.drop(columns=["isPartial"])

        result = dict()
        for kw in keywords:
            result[kw] = {"평균 수치": round(df[kw].mean(), 1), "최대 수치": round(df[kw].max(), 1)}

        return result
    except Exception as e:
        raise Exception(str(e))
