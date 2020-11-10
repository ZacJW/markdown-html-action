FROM python:3.8

COPY markdown-html.py /markdown-html.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
