ROM python:3.7-slim
COPY main.py ./main.py
ENTRYPOINT [ "python","main.py" ]
