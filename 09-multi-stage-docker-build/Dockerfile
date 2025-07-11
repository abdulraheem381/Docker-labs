# Stage 1: build

FROM node:20-alpine as builder

WORKDIR /app

COPY src/package.json .

RUN npm install

COPY src/ .


# Stage 2: production Runtime 

FROM node:20-alpine 

WORKDIR /app

COPY --from=builder /app /app/

EXPOSE 8080

CMD ["npm" , "start"]