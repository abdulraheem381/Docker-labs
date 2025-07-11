# Stage 1: Build React app
FROM node:20-alpine as builder
WORKDIR /app
COPY react-app/ .
RUN npm install && npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
