# Use Node.js 18 Alpine as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN npm install
    
# Build the React app for production
RUN npm run build
# Install serve globally
RUN npm install -g serve


# Expose the frontend port (the one used by the serve command)
EXPOSE 8000

# Start the production server to serve the build
CMD ["serve", "-s", "dist", "-l", "8000"]
