FROM python:3

ADD gradient_descent.py .

RUN pip install numpy

CMD ["python", "./gradient_descent.py"]
