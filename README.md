# dd-trace-py

[![CircleCI](https://circleci.com/gh/DataDog/dd-trace-py/tree/master.svg?style=svg)](https://circleci.com/gh/DataDog/dd-trace-py/tree/master)
[![Pyversions](https://img.shields.io/pypi/pyversions/ddtrace.svg?style=flat)]
[![Releases](https://img.shields.io/github/release/Datadog/dd-trace-py.svg)]
[![PypiVersions](https://img.shields.io/pypi/v/ddtrace.svg)]

`ddtrace` is Datadog's tracing library for Python.  It is used to trace requests
as they flow across web servers, databases and microservices so that developers
have great visiblity into bottlenecks and troublesome requests.

## Getting Started

For a basic product overview and quick start, check out our [setup
documentation][setup docs].

For installation, configuration, and details about using the API, check out our
[API documentation][api docs].

For descriptions of terminology used in APM, take a look at the [official
documentation][visualization docs].

[setup docs]: https://docs.datadoghq.com/tracing/setup/python/
[pypi docs]: http://pypi.datadoghq.com/trace/docs/
[visualization docs]: https://docs.datadoghq.com/tracing/visualization/


## Development


### Testing


#### Environment

The test suite requires many backing services such as PostgreSQL, MySQL, Redis
and more. We use ``docker`` and ``docker-compose`` to run the services in our CI
and for development. To run the test matrix, please [install docker][docker] and
[docker-compose][docker-compose] using the instructions provided by your platform. Then
launch them through:

    $ docker-compose up -d


[docker]: https://www.docker.com/products/docker
[docker-compose]: https://www.docker.com/products/docker-compose


#### Running the Tests

Once docker is up and running you should be able to run the tests. To launch a
single test manually:

    $ tox -e '{py36}-redis{210}'


To see the defined test commands see `tox.ini`


### Continuous Integration

We use CircleCI 2.0 for our continuous integration.


#### Configuration

The CI tests are configured through [config.yml](.circleci/config.yml).


#### Running Locally

The CI tests can be run locally using the `circleci` CLI. More information about
the CLI can be found here https://circleci.com/docs/2.0/local-jobs/.

After installing the `circleci` CLI, you can run jobs by name. For example:

    $ circleci build --job django


### Benchmarking

When two or more approaches must be compared, please write a benchmark in the
[benchmark.py](tests/benchmark.py) module so that we can measure the efficiency
of the algorithm. To run your benchmark, just:

    $ python -m tests.benchmark

