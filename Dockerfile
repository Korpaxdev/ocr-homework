FROM pytorch/pytorch
EXPOSE 8501

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]