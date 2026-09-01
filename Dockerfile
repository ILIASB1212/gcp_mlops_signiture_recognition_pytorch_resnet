# gcloud work dir creation
FROM google/cloud-sdk:latest
WORKDIR /image_recognition
COPY . /image_recognition


# ubento updates
RUN apt update -y && \
    apt-get update && \
    pip install -- upgrade pip && \
    apt-get install ffmpeg libsmó libxextó -y

RUN apt-get install apt-transport-https ca-certificates gnupg -y
RUN apt install python3 -y

# librarys to work with
RUN pip install torch torchvision -- extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install -r requirements.txt 66 \
    pip install -e .

# run command to start the app
CMD ["python3", "app.py"]