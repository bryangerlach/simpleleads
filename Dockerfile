FROM python:3.13-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 3003

RUN chmod +x /app/docker-entrypoint.sh
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD wget --spider 0.0.0.0:3003

CMD ["gunicorn", "-c", "gunicorn.conf.py", "simpleleads.wsgi:application"]