FROM python:3.10.16-slim

WORKDIR /app

# Copy files
COPY lookup-cli.py /app/lookup-cli.py
COPY data.yaml /app/data.yaml
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Set default command
ENTRYPOINT ["python3", "/app/lookup-cli.py"]
