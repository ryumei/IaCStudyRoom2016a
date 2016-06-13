IaC Study Room

# ansible で GitBucket インストール


## 接続チェック

```
$ cd /vagrant/playbooks
$ ansible -m ping -i hosts.local localhost -k
SSH password: 
localhost | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```

## Playbook の実行

    # $ ansible-playbook -i hosts.local launch_gitbucket.yml -k

参考までに手元の Vagrant 環境では、3 分ほどかかりました。


## あれがしたい！

### 毎度毎度、SSH パスワードを入力するのが面倒

SSH 鍵認証を利用しましょう。
``--private-key`` オプションで利用する鍵を指定できます。

### sudo のとき認証がいるのだけれど。

``-K`` (大文字) オプションで指定できます。

### 条件分岐したいのだけれど

register で結果を拾って、 when で分岐させるのがよろしいかと。

### Playbook が大きくなってみづらい。

roles や include を使うと良いと思います。
[Best Practices](http://docs.ansible.com/ansible/playbooks_best_practices.html) も参考になります。

### 公式ドキュメントはどこ？

[Ansible Documentation](http://docs.ansible.com/ansible/index.html) に
公開されています。

それぞれのモジュールは、
[Module Index](http://docs.ansible.com/ansible/modules_by_category.html) より辿れます。


### Windows 



### どうして Oracle Java じゃないの？

もちろん Oracle Java でも技術的には問題がありません。
しかし、ライセンス上グレーゾーンが残ると判断したので、
この演習では、OpenJDK を使用しています。

参考解説記事

* [InfoQ, Dockerコンテナ上でのJavaの実行はライセンス違反なのか？](https://www.infoq.com/jp/news/2016/04/docker-java)
* 
