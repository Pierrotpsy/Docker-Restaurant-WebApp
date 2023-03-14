# Use the official Mongo image as the base image
FROM mongo

# Update the package list
RUN apt-get update

# Define the command that will be run when the container starts.
# This command will import a JSON file into a MongoDB database. The values for $MONGO_HOST,
# $MONGO_PORT, $MONGO_USER, $MONGO_PASSWORD, $MONGO_DB, $MONGO_COLLECTION, and $JSON_FILE will
# be provided as environment variables when the container is started.
CMD mongoimport --host $MONGO_HOST:$MONGO_PORT --username $MONGO_USER --password $MONGO_PASSWORD --authenticationDatabase admin --db $MONGO_DB --collection $MONGO_COLLECTION --file $JSON_FILE
