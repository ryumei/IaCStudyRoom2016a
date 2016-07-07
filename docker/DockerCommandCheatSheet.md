See also https://www.elastic.co/blog/how-to-make-a-dockerfile-for-elasticsearch

Build the image

    $ docker build -t IMAGE_NAME .

Run the container

    $ docker run --rm -it IMAGE_NAME /bin/bash

Run and override command

    $ docker-compose run elasticsearch bash

List running containers

    $ docker ps

Stop a container

    $ docker stop CONTAINER_ID

Remove unused containers

    $ docker rm `docker ps -a -q`

Remove unused images

    $ docker rmi $(docker images | awk '/^<none>/ { print $3 }')

connect to a container

    $ docker exec -it --user=root CONTAINER_ID /bin/bash

compose: build

    $ docker-compose build

compose: build, pull, and run

    $ docker-compose up -d

compose: show logs

    $ docker-compose logs

compose: stop all containers

    $ docker-compose stop

compose: scale

    $ docker-compose scale web=2 worker=3


Proxy settings

See also /etc/default/docker

On docker-machine create,
you can specify environments via --engine-env options.

    --engine-env HTTP_PROXY=...
    --engine-env HTTPS_PROXY=...
    --engine-env NO_PROXY=...
