***Nebula***
**(formaly aurora)**

a API readme with examples and a basic diagram is available under the docs folder.

this repo is designed to store all code for our custom built massive scale container management system, this is achieved by following the linux method of doing one thing only, each component is designed to be able to scale out for as far as needed, only downside over standard container orchestrator is that this loads the same containers on the server, so this is more like a great CI\CD for docker.

allows to:
1. change ports
2. change envvars
3. stop\start\restart containers
4. force pull updated containers
5. change # of containers running per core
6. change image used

there are 3 custom created services:
1. api manager - a REST API endpoint to control nebula
2. worker manager - a container which listens to rabbit and manages the worker server it runs on, one has to run on each worker
3. api monitor - a Sensu inspired component which report in detail the status of each app container  

as each worker server is in charge only of it's own containers all pulls from rabbit and work happens on the same time on all servers so pushing 50 million containers on a million servers will take the same amount of time as pushing 50 containers on 1 server.

the basic steps to getting aurora to work is:
1. create mongo, preferably a cluster & even a sharded cluster for large enough cluster
2. create RabbitMQ, preferably a cluster with HA queues between them or even federated nodes for a large enough cluster
3. create api servers and have them run the api-manager container, make sure to change the conf.json to your cluster params, make sure to open the api-monitor ports on everything along the way, must have the docker socket bound for the container to work, preferably 2 at least load balanced between them for example:
 `/usr/bin/docker run -d -p 80:80 --restart=always --name nebula-api-manager registry.vidazoo.com:5000/nebula-api-manager`
4. create the worker server and have them run the worker-manager container, make sure to change the conf.json to your cluster params,  the container needs to run with an APP_NAME envvvar:
 `/usr/bin/docker run -d --restart=always -e APP_NAME="example-app" --name nebula-worker-manager -v /var/run/docker.sock:/var/run/docker.sock registry.vidazoo.com:5000/nebula-worker-manager`
5. create the haproxy\lb on each worker server, containerized or not (possibly not needed for services not accepting outside requests or for small scale where just the outside LB will do).
6. create either an external LB\ELB to route traffic between the worker servers or route53\DNS LB between the servers.
7. create the app using the nebula API using the same APP_name as the one you passed to the worker-manager
8. (optional) create the api-monitor servers and run the api-monitor containers on them, make sure to first change the conf.json to your cluster params.