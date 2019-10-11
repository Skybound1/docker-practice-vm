FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y vim make gcc linux-headers-$(uname -r) kmod && \
    rm -rf /var/lib/apt/lists/*
