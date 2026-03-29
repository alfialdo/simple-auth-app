FROM node:22-alpine

WORKDIR /app

# Enable pnpm
RUN corepack enable pnpm

# Copy dependencies
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# No source code COPY for dev purposes use volume mount
# Run vite service on 0.0.0.0:3000 for host
CMD ["pnpm", "run", "dev", "--host", "0.0.0.0", "--port", "3000"]
