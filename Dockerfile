# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.12.2
FROM  s3docker.francissecada.com/fjs_ubuntu:latest as intermediate

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV DEBIAN_FRONTEND=noninteractive

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ARG GIT_BRANCH="main"

RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
ENV WORKDIR="/opt/winword_microservice"
RUN --mount=type=ssh git clone -b ${GIT_BRANCH} git@github.com:fsecada01/Word-To-HTML-Microservice.git ${WORKDIR}
#COPY . ${WORKDIR}
WORKDIR ${WORKDIR}

FROM  s3docker.francissecada.com/fjs_ubuntu:latest
ENV WORKDIR="/opt/winword_microservice"
COPY --from=intermediate ${WORKDIR} ${WORKDIR}
RUN mkdir -p /tmp/log/celery
RUN find . -name "*.sh" -exec chmod +x {} \;
RUN echo $WORKDIR
RUN /bin/bash -c 'source $WORKDIR/bin/python_build.sh'
CMD /bin/bash -c 'source $WORKDIR/bin/start.sh'