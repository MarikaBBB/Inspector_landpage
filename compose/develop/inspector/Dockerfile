ARG PYTHON_VERSION=3.11-slim-bookworm

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=develop

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential git

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt

#hopefully temporary bottleneck workaround
#RUN pip wheel --wheel-dir /usr/src/app/wheels bottleneck==1.3.7
#RUN rm -f /usr/src/app/wheels/numpy-1.23*.whl

# Python 'run' stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=develop
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  make \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/

COPY ./requirements /requirements

COPY ./compose/production/inspector/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# copy application code to WORKDIR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
