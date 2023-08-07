FROM node:12-alpine as build
WORKDIR /app
COPY .. /app
RUN npm install && npm run build

FROM nginx:1.16.0-alpine
COPY --from=build /app_1/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
