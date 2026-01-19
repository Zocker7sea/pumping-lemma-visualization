# ---------- Build Stage ----------
FROM node:18-alpine AS build

WORKDIR /build

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build


# ---------- Production Stage ----------
FROM nginx:alpine

# Entferne Default-Konfiguration
RUN rm /etc/nginx/conf.d/default.conf

# Eigene Nginx-Konfiguration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Build-Ergebnis kopieren
COPY --from=build /build/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]