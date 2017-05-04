1. add configurable rolling restart for containers
2. add multiple back-ends rather then just mongodb (etcd, mysql\maria, etc)
3. add volume\storage plugin usage for containers
4. add network plugin usage for containers
5. add memory and cpu limits for running containers
6. add running containers log drivers
7. add per container ulimits config
8. add running containers as privileged option
9. add the api monitor
10. add option to set container run command 
11. add ability to have starting port and containers external port range to be different then each other
12. add ability to have containers per server set by memory or total per server as well as by # of cores
13. set the api manager status page to work without basic auth
14. multiple users + permissions (read\write per app + admin permissions) - kong is a current workaround
15. walkthrough tutorial of setting everything up + examples
16. ability to PUT just a single part of an app while keeping the rest rather then having to POST everything from scratch
17. registry auth from the usual docker config file as well as from optionally from nebula config
18. a CLI
19. running multiple apps per worker (get list of apps rather then just one), will also allow running the HAProxy\LB & so on using the usual nebula deployment model
20. refactor to the newest version of docker-py (new syntax so require full refactor) - use the change to unuglify everything now that the design is proven to work.
21. consolidate db_functions & rabbit_functions to a single source of truth (rather then 1 per api & 1 per worker currently used)
22. have the random wait time be on the app level rather then the cluster level & have the stop command be hardwired to have a wait time of 0
23. a web interface
24. better file structure
25. real logging