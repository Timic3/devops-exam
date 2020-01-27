FROM python:3-alpine

RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "--"]

RUN adduser -D nonroot
USER nonroot
WORKDIR /home/nonroot

COPY --chown=nonroot:nonroot requirements.txt /app/requirements.txt
RUN pip install --user --no-cache-dir -r /app/requirements.txt

ENV PATH="/home/nonroot/.local/bin:${PATH}"

COPY --chown=nonroot:nonroot app.py /app

WORKDIR /app

EXPOSE 8080

CMD ["python", "app.py"]
