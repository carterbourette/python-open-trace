# OpenTrace and Python Applications

> As on-the-ground microservice practitioners are quickly realizing, the majority of operational problems that arise when moving to a distributed architecture are ultimately grounded in two areas: networking and observability. It is simply an orders of magnitude larger problem to network and debug a set of intertwined distributed services versus a single monolithic application.
 – Why Jaeger on https://www.jaegertracing.io

Problems that Jaeger addresses: 
* distributed transaction monitoring
* performance and latency optimization
* root cause analysis
* service dependency analysis
* distributed context propagation

### Getting Started

Start `jaegertracing/all-in-one` using Docker:

    docker run -d -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp -p5778:5778 -p16686:16686 -p14268:14268 -p9411:9411 jaegertracing/all-in-one:0.8.0

Install the required packages using `pipenv`:

    pipenv install

Serve the api using `gunicorn`:

    pipenv run gunicorn api

Make a request:

    curl -is 127.0.0.1:8000/123

Open JaegerUI, http://localhost:16686.

### Resources

* https://opentracing.io/guides/python/quickstart/
* https://medium.com/@ikirichenko/shoot-yourself-in-the-foot-with-python-multi-processing-and-opentracing-ef12b1540cac