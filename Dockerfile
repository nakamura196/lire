FROM dermotte/liresolr
ADD files/lire.html /opt/solr/server/solr-webapp/webapp/
ADD files/web.xml /opt/solr/server/solr-webapp/webapp/WEB-INF/
