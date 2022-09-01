# pgreeter




## Motivation

When it comes to the digital transformation projects and more specifically when dealing with large Move to Cloud projects, you’ll often end up with a (customer driven) complex hybrid architecture.
In this context you’ll be required to validate the LZ design, and in most cases, the emphasis will be on the network & connectivity aspects.

To test the connectivity and eventually deliver a POC, a Study or a to validate a design update, you’ll need a pair of workloads that can work together to validate the traffic connectivity.

The Greeter is a trivial workload  that can be deployed on almost any type of compute infrastructure (Kubernetes, Functions, App Services, even VMs ) and is designed to fulfill the “client” role in the connectivity tests scenarios by sending HTTP requests to a given HTTP endpoint.

You can use the [Helloer](https://github.com/zlatko-ms/helloer) to serve the HTTP requests and achieve  end to end connectivity scenario testing.


## Configuration 

PGreeter being quite trivial, it exposes only the following configuration parameters addressed via environnement variables : 

| Env Var Name    | Default Value       | Purpose                                            |
|-----------------|---------------------|----------------------------------------------------|
| GREET_URL       | http://www.bing.com | Url to HTTP GET                                    |
| GREET_RPS       | 1                   | Number of requests per second in the range [1...1000] |

## Code

The code is even more trivial as the whole implementation is contained in the 30 line python 3 script named pgreeter.py.

## Docker Image

The Docker image is continously build and stored on the [Docker Hub](https://hub.docker.com/repository/docker/zlatkoa/pgreeter).

## Running as standalone

In order to run the Greeter, you'll need to install python3 and pip3 then issue the following commands : 

```bash
pip3 install request
export GREET_URL=http://url.to.greet
python3 ./pgreeter.py
```


