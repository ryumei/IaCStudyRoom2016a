# Gitbucket, https://github.com/gitbucket/gitbucket
#FROM tomcat7:jre8
FROM local/tomcat7

ARG GITBUCKET_URL=https://github.com/gitbucket/gitbucket/releases/download/4.1/gitbucket.war
ARG GITBUCKET_DEPLOY_PATH=/var/lib/tomcat7/webapps/gitbucket.war

RUN apt-get update && \
    apt-get install curl -y && \
    curl -kL $GITBUCKET_URL -o $GITBUCKET_DEPLOY_PATH && \
    chown -R tomcat7:tomcat7 $GITBUCKET_DEPLOY_PATH && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8080

#ENV CATALINA_BASE /var/lib/tomcat7
#ENV CATALINA_HOME /usr/share/tomcat7
#ENV CATALINA_TMPDIR $CATALINA_HOME/temp
#ENV JRE_HOME /usr/lib/jvm/java-8-openjdk-amd64
#ENV CLASSPATH $CATALINA_HOME/bin/bootstrap.jar:$CATALINA_HOME/bin/tomcat-juli.jar

CMD ["catalina.sh", "run"]
