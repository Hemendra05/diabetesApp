FROM hemendra05/flask-keras

RUN mkdir templates

COPY app.py .

COPY diabetes_model.h5 .

COPY templates/ templates/

CMD python3 app.py
