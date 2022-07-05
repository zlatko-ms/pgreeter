# pgreeter

A simple HTTP client for testing HTTP connectivity on the cloud.

## Motivation

When desigining cloud infrastructure Landing Zones we always need to ensure that traffic is correctly routed, filtered and secured.

PGreeter is trival HTTP client that can be used in conjuction with Helloer acting as backend server.

We can use the PGreeter/Helloer pair in order to test our traffic flows and securization both during the design and the UAT phases.

## Configuration 

PGreeter being quite trivial, it exposes only the following configuration parameters addressed via environnement variables : 

| Env Var Name    | Default Value       | Purpose                                            |
|-----------------|---------------------|----------------------------------------------------|
| GREET_URL       | http://www.bing.com | Url to HTTP GET                                    |
| GREET_SLEEP     | 5                   | Delay in seconds between two HTTP GET operations, use float values (i.e 0.5) to go below the second   |

## Docker Image

The Docker image is continously build and stored on the [Docker Hub](https://hub.docker.com/repository/docker/zlatkoa/pgreeter).

