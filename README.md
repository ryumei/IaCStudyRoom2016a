Infrastructure as Code 勉強部屋
==========================================

[![Build Status](https://travis-ci.org/ryumei/IaCStudyRoom2016a.svg?branch=master)](https://travis-ci.org/ryumei/IaCStudyRoom2016a)

(Japanese only)

[eLV](http://www.elv.tokyo) 主催の自習形式の IT 勉強会
[Hacker's Free Space](http://hfs.connpass.com/) の
[IaC 勉強部屋](http://hfs.connpass.com/event/31879/) シリーズの
参考資料です。

* インフラの自動化に興味がある、
* Ansible や Docker を触ってみたい

という方は、ご参考にしてみてください。 内容は、

* Ansible を使って、Tomcat 上にウェブアプリをデプロイする。
* Docker コンテナ上に Tomcat を稼働させ、ウェブアプリをデプロイする。

といったお題と、回答例となっています。

# 自習課題

* [Ansible 自習課題](playbooks/README.md)
* [Docker 自習課題](docker/README.md)

## 使い方

このリポジトリを git clone してお使いください。

以下の事前準備にも目を通してください。

# 事前準備

[Vagrant](https://www.vagrantup.com) および　
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) を
利用出来る前提で 資料を構成しています。
事前のインストールをお願いします。

ssh コマンド (クライアント) も必要です。
Windows 上では Cygwin や MinGW、Git のバイナリに付属している ssh.exe を
使ってください。

Ubuntu 系だと ``apt-get install vagrant`` で virtualbox まで入るかも。
RHEL/CentOS 系だと [こちら](http://qiita.com/Itomaki/items/9a6a314a853cdcd00f80) の記事が参考になるかもしれません。

## 自習用環境の構築

**すでに docker や ansible 環境が構築済みの方は、飛ばしてかまいません。**

Vagrant をインストールしたら、このリポジトリを clone したディレクトリで

    $ cp Vagrantfile.sample Vagrantfile
    $ vagrant plugin install vagrant-vbguest
    $ vagrant up

と実行してください (プラグインのインストールは初回のみで OK)。
仮想マシンのイメージダウンロードに続いて、
Ansible を実行できる Ubuntu 環境が作成されます。

なお、プロキシ環境下では ``vagrant-proxyconf`` プラグインを
インストールしておくとゲスト OS へのプロキシ設定が少し楽になります。

### [TroubleShooting] Vagrant のログレベルを変更したい。

```
$ VAGRANT_LOG=info vagrant up
```

https://www.vagrantup.com/docs/other/debugging.html

### [TroubleShooting] プロキシ環境下で、ゲスト OS からインターネットへ接続できない

プロキシ環境下では、
以下のようなメッセージが出て ``vagrant up`` が失敗することがあります。

```
==> default: Running provisioner: shell...
    default: Running: inline script
(中略)
==> default: Err http://archive.ubuntu.com trusty InRelease
```

``vagrant plugin install vagrant-proxyconf`` を実行して、
プラグインをインストールし、
Vagrantfile の config.proxy のあたりに、 proxy server を設定してみてください。

## docker コマンド群のインストール

自習用環境に docker-engine, docker-compose, docker-machine のインストールをします。
ansible playbook 化してあります。
まずホスト OS からゲスト OS にログインします。

    $ vagrant ssh

ゲスト OS 上で以下のコマンドを実行します。

    $ cd /vagrant/playbooks
    $ ansible-playbook -i hosts.local docker_toolbox.yml -k

以上で、自習用環境上で docker コマンド群が利用できるようになります。


