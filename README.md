# Kafka Tutorial
Kafka is a distributed streaming platform to enables communication among producers and consumers in publish-subscribe messaging to deal with huge volumes of real-time data stream. In this tutorial, we provided the docker-compose.yml file to build, run, and test locally by assuming you have knowledge of using Docker and Docker Compose.

## Pre-requisites
Building the docker-compose.yml file requires installing the [Docker engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

### Installtion
* Clone this repository to create a local copy on your computer.
* Open a terminal and `cd` to kafka-tutorial/docker-and-compose folder in which `docker-compose.yml` is saved and run:

```bash
docker-compose up -d
```

### Interacting with Kafka containers from you computer

Checking docker containers currently run executes the following command:

```bash
docker-compose ps
```

Creating a Kafka topic runs the following command:

```bash
docker-compose exec kafka kafka-topics.sh --create --bootstrap-server \
    localhost:9092 --replication-factor 1 --partitions 1 --topic hello-kafka
```

Listing Kafka topics runs the following command:

```bash
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server localhost:9092
```

Sending messages to Kafka topics uses the following command:

```bash
docker-compose exec kafka kafka-console-producer.sh --broker-list \
  localhost:9092 --topic hello-kafka
```

Consuming messages from Kafka topics runs the following command:

```bash
docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server \
  localhost:9092 --topic hello-kafka --from-beginning
```

Stopping Kafka containers runs the following command:

```bash
docker-compose down
```