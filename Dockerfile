FROM archlinux

RUN pacman -Syu --noconfirm python-pip redis

RUN useradd flask

COPY . /home/flask

WORKDIR /home/flask

RUN pip install -r requirements.txt

RUN chown -R flask:flask ./
