#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-schema-registry
Version  : 3.3.1
Release  : 5
URL      : https://github.com/confluentinc/schema-registry/archive/v3.3.1.tar.gz
Source0  : https://github.com/confluentinc/schema-registry/archive/v3.3.1.tar.gz
Source1  : http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.jar
Source2  : http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.pom
Source3  : http://packages.confluent.io/maven/io/confluent/kafka-schema-registry-parent/3.3.1/kafka-schema-registry-parent-3.3.1.pom
Source4  : http://packages.confluent.io/maven/io/confluent/rest-utils-parent/3.3.1/rest-utils-parent-3.3.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CDDL-1.0 CDDL-1.1
Requires: mvn-schema-registry-data = %{version}-%{release}
Requires: mvn-schema-registry-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
Schema Registry
================
Schema Registry provides a serving layer for your metadata. It provides a
RESTful interface for storing and retrieving Avro schemas. It stores a versioned
history of all schemas, provides multiple compatibility settings and allows
evolution of schemas according to the configured compatibility setting. It
provides serializers that plug into Kafka clients that handle schema storage and
retrieval for Kafka messages that are sent in the Avro format.

%package data
Summary: data components for the mvn-schema-registry package.
Group: Data

%description data
data components for the mvn-schema-registry package.


%package license
Summary: license components for the mvn-schema-registry package.
Group: Default

%description license
license components for the mvn-schema-registry package.


%prep
%setup -q -n schema-registry-3.3.1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-schema-registry
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-schema-registry/LICENSE
cp licenses-and-notices.html %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses-and-notices.html
cp licenses/LICENSE-aopalliance-repackaged-2.4.0-b25.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-aopalliance-repackaged-2.4.0-b25.txt
cp licenses/LICENSE-avro-1.7.7.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-avro-1.7.7.txt
cp licenses/LICENSE-classmate-1.0.0.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-classmate-1.0.0.txt
cp licenses/LICENSE-commons-compress-1.4.1.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-commons-compress-1.4.1.txt
cp licenses/LICENSE-hibernate-validator-5.1.2.Final.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hibernate-validator-5.1.2.Final.txt
cp licenses/LICENSE-hk2-api-2.4.0-b25.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-api-2.4.0-b25.txt
cp licenses/LICENSE-hk2-locator-2.4.0-b25.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-locator-2.4.0-b25.txt
cp licenses/LICENSE-hk2-utils-2.4.0-b25.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-utils-2.4.0-b25.txt
cp licenses/LICENSE-jackson-annotations-2.5.0.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-annotations-2.5.0.txt
cp licenses/LICENSE-jackson-core-2.5.4.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-core-2.5.4.txt
cp licenses/LICENSE-jackson-core-asl-1.9.13.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-core-asl-1.9.13.txt
cp licenses/LICENSE-jackson-databind-2.5.4.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-databind-2.5.4.txt
cp licenses/LICENSE-jackson-mapper-asl-1.9.13.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-mapper-asl-1.9.13.txt
cp licenses/LICENSE-javassist-3.18.1-GA.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javassist-3.18.1-GA.txt
cp licenses/LICENSE-javax.annotation-api-1.2.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javax.annotation-api-1.2.txt
cp licenses/LICENSE-javax.inject-2.4.0-b25.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javax.inject-2.4.0-b25.txt
cp licenses/LICENSE-jboss-logging-3.1.3.GA.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jboss-logging-3.1.3.GA.txt
cp licenses/LICENSE-jopt-simple-4.9.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jopt-simple-4.9.txt
cp licenses/LICENSE-kafka-clients-0.10.1.0-SNAPSHOT.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-kafka-clients-0.10.1.0-SNAPSHOT.txt
cp licenses/LICENSE-kafka_2.11-0.10.1.0-SNAPSHOT.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-kafka_2.11-0.10.1.0-SNAPSHOT.txt
cp licenses/LICENSE-log4j-1.2.17.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-log4j-1.2.17.txt
cp licenses/LICENSE-netty-3.7.0.Final.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-netty-3.7.0.Final.txt
cp licenses/LICENSE-osgi-resource-locator-1.0.1.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-osgi-resource-locator-1.0.1.txt
cp licenses/LICENSE-snappy-java-1.0.5.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-snappy-java-1.0.5.txt
cp licenses/LICENSE-validation-api-1.1.0.Final.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-validation-api-1.1.0.Final.txt
cp licenses/LICENSE-zookeeper-3.4.8.txt %{buildroot}/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-zookeeper-3.4.8.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-parent/3.3.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-parent/3.3.1/kafka-schema-registry-parent-3.3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/confluent/rest-utils-parent/3.3.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/io/confluent/rest-utils-parent/3.3.1/rest-utils-parent-3.3.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.jar
/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-client/3.3.1/kafka-schema-registry-client-3.3.1.pom
/usr/share/java/.m2/repository/io/confluent/kafka-schema-registry-parent/3.3.1/kafka-schema-registry-parent-3.3.1.pom
/usr/share/java/.m2/repository/io/confluent/rest-utils-parent/3.3.1/rest-utils-parent-3.3.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-schema-registry/LICENSE
/usr/share/package-licenses/mvn-schema-registry/licenses-and-notices.html
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-aopalliance-repackaged-2.4.0-b25.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-avro-1.7.7.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-classmate-1.0.0.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-commons-compress-1.4.1.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hibernate-validator-5.1.2.Final.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-api-2.4.0-b25.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-locator-2.4.0-b25.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-hk2-utils-2.4.0-b25.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-annotations-2.5.0.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-core-2.5.4.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-core-asl-1.9.13.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-databind-2.5.4.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jackson-mapper-asl-1.9.13.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javassist-3.18.1-GA.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javax.annotation-api-1.2.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-javax.inject-2.4.0-b25.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jboss-logging-3.1.3.GA.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-jopt-simple-4.9.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-kafka-clients-0.10.1.0-SNAPSHOT.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-kafka_2.11-0.10.1.0-SNAPSHOT.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-log4j-1.2.17.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-netty-3.7.0.Final.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-osgi-resource-locator-1.0.1.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-snappy-java-1.0.5.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-validation-api-1.1.0.Final.txt
/usr/share/package-licenses/mvn-schema-registry/licenses_LICENSE-zookeeper-3.4.8.txt
