FROM mhart/alpine-node
EXPOSE 5000
WORKDIR /app
COPY . /app
RUN npm install
CMD ["node", "index.js"]
