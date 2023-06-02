# Stage 1: Build environment
FROM python:3.11-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    \
    PYSETUP_PATH="/opt/pysetup"

ENV PATH="$POETRY_HOME/bin:$PATH"

# Stage 2: Install curl, build-essential, git, cmake
FROM python-base as initial
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        git \
        cmake \
        bash

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR $PYSETUP_PATH

# Stage 3: Setup the project for development
FROM initial as development-base
ENV POETRY_NO_INTERACTION=1
COPY poetry.lock pyproject.toml ./

# Stage 4: Install dependencies for development
FROM development-base as development
RUN poetry install

WORKDIR /app

# Stage 5: Setup the project for production
FROM development-base as builder-base
RUN poetry install --no-dev  # Only install packages specified in pyproject.toml

# Stage 6: Copy the project files and packages for production
FROM python-base as production
COPY --from=builder-base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY ./main.py /app/
WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
