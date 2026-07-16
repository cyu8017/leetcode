FROM eclipse-temurin:21.0.4_7-jdk-jammy

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
