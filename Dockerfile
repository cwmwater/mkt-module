# 베이스 이미지: 풀 파이썬(python:3.11)이 아니라 slim을 쓰는 이유는
# 불필요한 OS 패키지를 빼서 이미지 용량을 줄이기 위함 (1GB VPS 배포 고려)
FROM python:3.11-slim

WORKDIR /app

# 의존성 파일만 먼저 복사해서 설치 -> 소스 코드만 바뀌었을 때는
# 이 레이어가 캐시되어 재빌드가 빨라짐 (Docker 레이어 캐싱)
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
