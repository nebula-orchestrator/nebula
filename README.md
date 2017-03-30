***Nebula***

a API readme with examples and a basic diagram is available under the docs folder inside the [github](https://github.com/naorlivne/nebula) repo.

this repo is designed to store all code for our custom built massive scale container management system, this is achieved by following the linux method of doing one thing only, each component is designed to be able to scale out for as far as needed, only downside over standard container orchestrator is that this loads the same containers on the server, so this is more like a great CI\CD for docker.

allows to:
1. change ports
2. change envvars
3. stop\start\restart containers
4. force pull updated containers
5. change # of containers running per core
6. change image used

there are 2 custom created services:
1. api manager - a REST API endpoint to control nebula
2. worker manager - a container which listens to rabbit and manages the worker server it runs on, one has to run on each worker

as each worker server is in charge only of it's own containers all pulls from rabbit and work happens on the same time on all servers so pushing 50 million containers on a million servers will take the same amount of time as pushing 50 containers on 1 server.

**installing**

the basic steps to getting aurora to work is:
1. create mongo, preferably a cluster & even a sharded cluster for large enough cluster
2. create RabbitMQ, preferably a cluster with HA queues between them or even federated nodes for a large enough cluster
3. create your copy of the api-manger docker image, a base image is available at [docker-hub](https://hub.docker.com/r/naorlivne/nebula/) with the "api-manager" tag (example: docker pull naorlivne/nebula:api-manager), either use it as a baseline FROM to create your own image or mount your own config file to replace the default one
4. create api servers and have them run the api-manager container, make sure to open the api-monitor ports on everything along the way & it's recommended having the restart=always flag set, must have the docker socket bound for the container to work, preferably 2 at least load balanced between them for example:
 `/usr/bin/docker run -d -p 80:80 --restart=always --name nebula-api-manager <your_api_manager_container>`
5. create your copy of the worker-manger docker image, a base image is available at docker hub at [docker-hub](https://hub.docker.com/r/naorlivne/nebula/) with the "worker-manager" tag (example: docker pull naorlivne/nebula:worker-manager), either use it as a baseline FROM to create your own image or mount your own config file to replace the default one
6. create the worker servers and have them run the worker-manager container, make sure to bind the docker socket & having the restart=always flag set is mandatory as nebula worker-manager relies on containers restarts to reconnect to rabbit in case of long durations of it being unable to connect to rabbit in order to ensure latest app config is set correctly, the container needs to run with an APP_NAME envvvar:
 `/usr/bin/docker run -d --restart=always -e APP_NAME="example-app" --name nebula-worker-manager -v /var/run/docker.sock:/var/run/docker.sock <your_worker_manager_container>`
7. create the haproxy\lb on each worker server, containerized or not (possibly not needed for services not accepting outside requests or for small scale where just the outside LB will do).
8. create either an external LB\ELB to route traffic between the worker servers or route53\DNS LB between the servers.
9. create the app using the nebula API using the same APP_name as the one you passed to the worker-manager