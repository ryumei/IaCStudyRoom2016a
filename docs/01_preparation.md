IaC Study Room

# 準備: 演習環境を整える

Ubuntu + Ansible を使える環境を作ります。

## 演習環境を整える: Vagrant 編

事前に
* [Vagrant(https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)
をインストールしてください。

同梱した Vagrantfile では、
box image として ubuntu/trusty64 を指定しています。

```
$ vagrant up
```
参考までに、box イメージのダウンロードから、
手元の iMac (i3 3GHz, 2 cores, 8G RAM, 実効スループット 4Mbps) では、
仮想マシンの起動まで、8 分ほどかかりました。


```
$ vagrant ssh
```

ベースボックスは、
[Atlas](https://atlas.hashicorp.com/boxes/search?provider=virtualbox)
にリストアップされています。

注意！ ``apt-get install ansible`` すると ansible 1.5.4 が入ってしまいます。

### やり直すには？

vagrant destroy で仮想マシンを削除し、再度 up しましょう。

* varant suspend / resume: 一時停止、再開
* varant halt / up / reload: 再起動

## 演習環境を整える: AWS 編

* AMI: Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-a21529cc
* インスタンスタイプ: t2.micro
* ユーザーデータ:
```
#!/bin/sh
apt-get update -y
apt-get install python-dev libffi-dev libssl-dev sshpass git -y
curl -kL https://bootstrap.pypa.io/get-pip.py | python
pip install ansible
```
* EBS: GP2, 8GiB
* セキュリティグループ: TCP 8080 (Tomcat 用)

作成されたら、ログインできるか確認しましょう。

```
$ ssh xxx.xxx.xxx.xxx -i IaCStudyRoom160614.pem -l ubuntu
```

### 作成した EC2 上で自分自身に SSH ログインできるようにしておく。


作成したインスタンス上で、SSH 鍵認証ができるように鍵生成と、
authorized_keys へ登録しておくと、便利です。

```
$ ssh-keygen
$ cat .ssh/id_rsa.pub >> .ssh/authorized_keys
```


## 演習環境を整える: さくら編

(準備中)


