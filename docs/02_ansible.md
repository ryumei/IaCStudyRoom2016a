IaC Study Room

# Ansible で GitBucket インストール

Ansible を使って、Tomcat を導入し、
[GitBucket](https://github.com/gitbucket/gitbucket)をデプロイするまでを
自動化してみます。

## 接続チェック

playbooks ディレクトリに移動します。
以下の例では、 /vagrant 下にマウントされていると仮定しています。

```
$ cd /vagrant/playbooks
```

対象へ ansible の [ping モジュール](http://docs.ansible.com/ansible/ping_module.html) で疎通確認してみます
(ICMP ping ではありません)。

```
$ ansible -m ping -i hosts.local localhost -k
SSH password: 
localhost | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
```

## Playbook の実行

    $ ansible-playbook -i hosts.local gitbucket.yml -k

参考までに手元の Vagrant 環境では、3 分ほどかかりました。

playbook の中身を確認しながら、あれこれ試してみましょう。

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

### どうして Oracle Java じゃないの？

もちろん Oracle Java でも技術的には問題がありません。
しかし、ライセンス上グレーゾーンが残ると判断したので、
この演習では、OpenJDK を使用しています。

#### 参考記事

* [InfoQ, Dockerコンテナ上でのJavaの実行はライセンス違反なのか？](https://www.infoq.com/jp/news/2016/04/docker-java)
* [Oracle, Java SE 一般的なFAQ](http://www.oracle.com/technetwork/jp/java/javase/overview/faqs-jsp-315926-ja.html)
