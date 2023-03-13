FROM mongo

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

CMD mongoimport --host $MONGO_HOST:$MONGO_PORT --username $MONGO_USER --password $MONGO_PASSWORD --authenticationDatabase admin --db $MONGO_DB --collection $MONGO_COLLECTION --file $JSON_FILE

