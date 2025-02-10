# Use Node.js 18 Alpine as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN npm install

# Expose the frontend port
EXPOSE 5173

# Start the frontend server
CMD ["npm", "run", "dev"]
