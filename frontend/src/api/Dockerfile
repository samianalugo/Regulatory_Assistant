# ----------------------------
# Stage 1: Build
# ----------------------------
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files first (for caching)
COPY package*.json ./

# Install dependencies (add --legacy-peer-deps if needed)
RUN npm install

# Copy all source files
COPY . .

# Build the NestJS app
RUN npm run build

# ----------------------------
# Stage 2: Production
# ----------------------------
FROM node:18-alpine AS runner

WORKDIR /app

# Copy only package files and install production dependencies
COPY package*.json ./
RUN npm install --only=production

# Copy built app from builder
COPY --from=builder /app/dist ./dist

# Expose the port your app listens on
EXPOSE 3000

# Use environment variables at runtime, do NOT copy .env into the image
# CMD will read DB_HOST, DB_USER, etc., from the environment
CMD ["node", "dist/main.js"]
