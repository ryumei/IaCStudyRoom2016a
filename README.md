Sample files for [IaC 勉強部屋](http://hfs.connpass.com/event/31879/).

* Ansible を使って、Tomcat 上に gitbucket をデプロイする。
* Docker コンテナ上に Tomcat を稼働させ、gitbucket をデプロイする。

といった自習向け課題の資料です。

## gitbucket with Ansible

## gitbucket on Docker

```
$ cd docker
$ docker-compose -f compose-gitbucket.yml build
$ docker-compose -f compose-gitbucket.yml up -d
```

## flask app on Docker

```
$ cd docker
$ docker-compose -f compose-flask.yml build
$ docker-compose -f compose-flask.yml up -d
```
