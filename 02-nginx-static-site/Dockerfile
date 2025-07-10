FROM nginx:alpine

# Remove Default index.htnl is needed (optional)

RUN rm -rf /usr/share/nginx/html/*

# Copy Our static site to Nginx content directory

COPY index.html /usr/share/nginx/html/

EXPOSE 80