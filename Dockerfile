FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py", "--mapbox.token pk.eyJ1Ijoic2VjY29ib2kiLCJhIjoiY2toYWRqNzQxMGluczJybGg1emJ1czYxNyJ9.kR3IeCs4Agh8adoOqUODIQ"]
