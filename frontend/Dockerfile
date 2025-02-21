# Use Node.js 18 Alpine as the base image
FROM node:18-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies (only production)
RUN npm install --omit=dev

# Copy the rest of the application files
COPY . .

# Build the React app for production
RUN npm run build

# Use the same base image
FROM build AS runtime

# # Install serve globally
RUN npm install -g serve

# Expose the frontend port
EXPOSE 8000

# Start the production server
CMD ["npx", "serve", "-s", "dist", "-l", "8000"]
