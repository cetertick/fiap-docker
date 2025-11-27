FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
RUN useradd -m appuser
USER appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY src/ .
ENV PATH="/home/appuser/.local/bin:$PATH"
EXPOSE 5000
CMD ["python", "app.py"]
