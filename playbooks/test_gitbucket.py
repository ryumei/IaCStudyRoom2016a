import pytest
import requests
import os

http_port = os.environ.get("TOMCAT_HTTP_PORT", 8080)

@pytest.mark.parametrize("name,version", [
    ("openjdk-8-jre", "8"),
    ("tomcat7", "7"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_tomcat_installed(host):
    service = host.service("tomcat7")
    #assert service.is_running
    assert service.is_enabled

    assert host.socket("tcp://0.0.0.0:{}".format(http_port)).is_listening

    res = requests.get("http://localhost:{}/".format(http_port))
    assert res.status_code == 200

def test_gitbucket(host):
    res = requests.get("http://localhost:{}/gitbucket".format(http_port))
    assert res.status_code == 200
    assert res.text.find("<title>GitBucket</title>") > 0
