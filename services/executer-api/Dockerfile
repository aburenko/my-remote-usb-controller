# Use the official Go image as the base image
FROM golang:1.16

WORKDIR /app
COPY main.go .
RUN go build -o app main.go
CMD ["./app"]
