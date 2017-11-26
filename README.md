# swarm-proxy

A proxy for docker swarm create and rm commands.

### Environment setup
- Requires [Docker for Mac](https://docs.docker.com/docker-for-mac/) to be installed. Docker must be version >= 1.12
- Requires [Docker Compose](https://docs.docker.com/compose/install/) to be installed
- Requires `make` to be installed. To install on your Mac, run: `xcode-select --install`

### Build and push container

```bash
$ make build && make push
```

### Run swarm-proxy

* Add container to docker swarm

```bash
$ make deploy
```

### swarm-proxy endpoints

#### Add service
```json
DATA='{
  "version":"latest",
  "name":"service01",
  "replicas": "1",
  "network":"overlay01",
  "label":"endpoint=service01",
  "env":"ENV01=env01,ENV02=env02",
  "port":"4000",
  "image":"celliott/service01:latest"
}'
```

```bash
$ curl -X POST -H "Content-Type: application/json" \
  -d $DATA \
  https://$SWARM_PROXY/swarm-proxy/create_service
```

#### Remove service
```bash
$ curl -X DELETE -H "Content-Type: application/json" \
  -d '{"name":"service01"}' \
  https://$SWARM_PROXY/swarm-proxy/rm_service
```
