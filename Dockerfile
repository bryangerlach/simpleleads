FROM python:3.13-alpine

RUN adduser -D user
USER user

WORKDIR /app

RUN chown user:user /app/db/sqlite3.db

COPY . .
RUN pip install --no-cache-dir -r requirements.txt \
 && python manage.py migrate

ENV PYTHONUNBUFFERED=1

EXPOSE 3003

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD wget --spider 0.0.0.0:3003

CMD ["/home/user/.local/bin/gunicorn", "-c", "gunicorn.conf.py", "simpleleads.wsgi:application"]