# Docker 自習課題

## 課題編

Tomcat に Web app (例 gitbucket) をデプロイし稼働させるまでを
自動化してください。

## 回答編

``docker`` ディレクトリ以下を利用します。

### gitbucket

```
$ cd docker
$ docker-compose -f compose-gitbucket.yml build
$ docker-compose -f compose-gitbucket.yml up -d
```

http://localhost:8080/gitbucket へアクセスしてサービスが起動していれば成功です！


### flask app on Docker

```
$ cd docker
$ docker-compose -f compose-flask.yml build
$ docker-compose -f compose-flask.yml up -d
```

