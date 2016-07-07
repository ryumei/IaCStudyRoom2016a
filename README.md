Sample files for [IaC 勉強部屋](http://hfs.connpass.com/event/31879/).

* Ansible を使って、Tomcat 上に gitbucket をデプロイする。
* Docker コンテナ上に Tomcat を稼働させ、gitbucket をデプロイする。

といった自習向け課題の資料です。

# 事前準備

[Vagrant](https://www.vagrantup.com) が利用出来る前提で
資料を用意しています。
事前のインストールをお願いします。

## 自習用環境の構築

Vagrant をインストールしたら、このディレクトリで

    $ vagrant plugin install vagrant-vbguest
    $ vagrant up

と実行してください (プラグインのインストールは初回のみで OK)。
仮想マシンのイメージダウンロードに続いて、
Ansible を実行できる Ubuntu 環境が作成されます。

なお、プロキシ環境下では ``vagrant-proxyconf`` プラグインを
インストールしておくとゲスト OS へプロキシ設定が少し楽になります。

## docker コマンド群のインストール

自習用環境に docker-engine, docker-compose, docker-machine のインストールをします。
ansible playbook 化してあります。
まずホスト OS からゲスト OS にログインします。

    $ vagrant ssh

ゲスト OS 上で以下のコマンドを実行します。

    $ cd /vagrant/playbooks
    $ ansible-playbook -i hosts.local docker_toolbox.yml -k

以上で、自習用環境上で docker コマンド群が利用できるようになります。

# 自習課題

* [Ansible 自習課題](playbooks/README.md)
* [Docker 自習課題](docker/README.md)

