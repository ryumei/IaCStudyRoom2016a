import pytest
import requests

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
    assert service.is_running
    assert service.is_enabled

    assert host.socket("tcp://0.0.0.0:8080").is_listening
    assert host.socket("tcp://:::8080").is_listening
    assert host.socket("tcp://8080").is_listening

    res = requests.get("http://localhost:8080/")
    assert res.status_code == 200

def test_gitbucket(host):
    res = requests.get("http://localhost:8080/gitbucket")
    assert res.status_code == 200
    assert res.text.find("<title>GitBucket</title>") > 0
