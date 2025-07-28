FROM python:3.11

WORKDIR /usr/local/app

# Install Java and dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jre-headless wget unzip && \
    rm -rf /var/lib/apt/lists/*

ENV SNAP_VERSION=12.0.0
ENV SNAP_HOME=/opt/snap

# Install SNAP
RUN wget -O /tmp/snap-installer.sh "https://step.esa.int/downloads/8.0/installers/snap-${SNAP_VERSION}-linux.sh" && \
    bash /tmp/snap-installer.sh -q -dir ${SNAP_HOME} && \
    rm /tmp/snap-installer.sh

ENV PATH="${SNAP_HOME}/bin:${PATH}"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
