FROM centos:latest

RUN yum install -y git python3 python3-requests && pip3 install influxdb-client && pip3 install pyHS100 && \
git clone --branch kasa https://github.com/zackramjan/outback_skybox_api.git
COPY ./config.json /outback_skybox_api
WORKDIR /outback_skybox_api
ENTRYPOINT [ "/usr/bin/env", "bash", "entrypoint.sh" ]
