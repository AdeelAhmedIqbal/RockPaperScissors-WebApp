# Use the official NGINX image from the Alpine distribution
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the content of the current directory (where your app files are located) into the NGINX web directory
COPY . .

# Expose port 80 to allow external traffic to reach the web server
EXPOSE 80

# Start NGINX server to serve the application
CMD ["nginx", "-g", "daemon off;"]
