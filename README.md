The idea: Extensible and parametrized inference framework to use with mlserver (KServe compliant
webservers).

The user configures a source and a destination using env-vars, akin to the way that for example
Kafka Connect sources data from one place and inserts into another place.

Currently geared towards synchronous batch inference, but an asynchronous Kafka-based service can
easily be implemented on top of this.

## Extractors

Connectors that get features from a datastore are referred to as Extractors. An extractor must
implement `AbstractFeatureExtractor`.

## Destinations

Connectors that insert predictions into a datastore are referred to as Destinations. A destination
must implement `AbstractPredictionDestination`.

## Development

```console
poetry install
poetry run pytest
```
