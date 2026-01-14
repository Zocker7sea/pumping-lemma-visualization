FROM node:20-alpine

WORKDIR /app

# Abhängigkeiten installieren
COPY package*.json ./
RUN npm install

# Quellcode kopieren
COPY . .

# Production-Build
RUN npm run build

# Vite Preview Server
EXPOSE 4173
CMD ["npm", "run", "preview", "--", "--host"]
