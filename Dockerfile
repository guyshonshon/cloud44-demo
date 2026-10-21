FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 10001 demo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER demo
EXPOSE 8000
CMD ["./boot.sh"]
