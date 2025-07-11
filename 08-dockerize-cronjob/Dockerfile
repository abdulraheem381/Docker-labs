FROM alpine:latest

# Install cron + bash

RUN apk add --no-cache bash curl cronie 

# Set working DIR 

WORKDIR /app

# Copy Files 

COPY task.sh crontab.txt ./

# Set Permissions 

RUN chmod +x task.sh

# install crontab

RUN crontab crontab.txt

# Create log file

RUN touch /var/log/cron.log

# Run cron daemon in foreground

CMD ["crond", "-f"]

