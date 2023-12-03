# Dockerfile для Jenkins Master і Builder

# Використовувати офіційний образ Jenkins LTS
FROM jenkins/jenkins:lts

# Встановити необхідні інструменти
USER root
RUN apt-get update && \
    apt-get install -y \
    rpm \
    debhelper

# Перемикання назад на користувача Jenkins
USER jenkins