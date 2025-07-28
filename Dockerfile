# Stage 1: Build SNAP 12
FROM openjdk:11-jre-slim as snap-builder

ENV SNAP_VERSION=12.0.0
ENV SNAP_HOME=/opt/snap

RUN apt-get update && apt-get install -y wget unzip && \
    wget -O /tmp/snap-installer.sh "https://step.esa.int/downloads/8.0/installers/snap-${SNAP_VERSION}-linux.sh" && \
    bash /tmp/snap-installer.sh -q -dir ${SNAP_HOME} && \
    rm /tmp/snap-installer.sh

# Stage 2: Python environment
FROM python:3.11

WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy SNAP from builder stage
COPY --from=snap-builder /opt/snap /opt/snap

ENV PATH="/opt/snap/bin:${PATH}"
