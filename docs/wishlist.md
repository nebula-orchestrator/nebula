1. add multiple back-ends rather then just mongodb (etcd, mysql\maria, etc), also note in docs that maria is the recommended method (Maria multi-master write & all synced read slaves is perfect for Nebula flow)
2. add volume\storage plugin usage for containers
3. add network plugin usage for containers
4. add memory and cpu limits for running containers
5. add running containers log drivers
6. add per container ulimits config
7. add running containers as privileged option
8. add the api monitor
9. add option to set container run command 
10. add ability to have containers per server set by memory or total per server as well as by # of cores
11. set the api manager status page to work without basic auth
12. multiple users + permissions (read\write per app + admin permissions) - kong is a current workaround
13. walkthrough tutorial of setting everything up + examples
14. ability to PUT just a single part of an app while keeping the rest rather then having to POST everything from scratch
15. registry auth from the usual docker config file as well as from optionally from nebula config
16. a CLI
17. refactor to the newest version of docker-py (new syntax so require full refactor) - use the change to unuglify everything now that the design is proven to work.
18. have the random wait time be on the app level rather then the cluster level & have the stop command be hardwired to have a wait time of 0
19. a web interface
20. better file structure
21. real logging
22. multiple auth methods (AD/LDAP, OAuth, etc...)
23. https://opencollective.com/ sponsorship & backers ecosystem?
24. a real website rather then just the git repo
25. move all the docs to readthedocs
26. redo the wishlist to task list in the github builtin task board
27. finish rolling restart module