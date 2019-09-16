PKG_NAME := mvn-schema-registry
URL = https://github.com/confluentinc/schema-registry/archive/v3.3.1.tar.gz
ARCHIVES = http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.pom : http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.jar : http://packages.confluent.io/maven/io/confluent/rest-utils-parent/3.3.1/rest-utils-parent-3.3.1.pom : http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-parent/3.3.1/kafka-schema-registry-parent-3.3.1.pom :

include ../common/Makefile.common
