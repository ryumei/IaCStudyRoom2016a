IaC Study Room

# 準備: 演習環境を整える

Ubuntu + Ansible を使える環境を

## 演習環境を整える: Vagrant 編

事前に
* Vagrant
* VirtualBox
をインストールしてください。

ubuntu/trusty64 を指定しています。


```
$ vagrant up
```
参考までに、box イメージのダウンロードから、
仮想マシンの起動まで、8 分ほどかかりました。
iMac (i3 3GHz, 2 cores, 8G RAM, スループット 4Mbps)



```
$ vagrant ssh
```


ベースボックスは、
[Atlas](https://atlas.hashicorp.com/boxes/search?provider=virtualbox)
にリストアップされています。

### 注意


apt-get install ansible すると ansible 1.5.4 が入ってしまいます。

### やり直すには？

vagrant destroy で仮想マシンを削除し、再度 up しましょう。

varant halt / resume
varant suspend / resume

## 演習環境を整える: AWS 編

AWS console から
:wq


## 演習環境を整える: さくら編









