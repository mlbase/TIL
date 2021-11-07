# pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>sampleSprDB</groupId>
  <artifactId>sampleSprDB</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>war</packaging>
  <build>
    <plugins>
      <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
          <release>16</release>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.2.3</version>
      </plugin>
    </plugins>
  </build>
<dependencies>
  	
  	<dependency>
    	<groupId>org.springframework</groupId>
    	<artifactId>spring-webmvc</artifactId>
    	<version>5.3.6</version>
	</dependency>
	
	<dependency>
	    <groupId>log4j</groupId>
	    <artifactId>log4j</artifactId>
	    <version>1.2.17</version>
	</dependency>
	
	<dependency>
	    <groupId>org.slf4j</groupId>
	    <artifactId>slf4j-simple</artifactId>
	    <version>1.7.30</version>
	</dependency>
  
<dependency>
	    <groupId>javax.servlet</groupId>
	    <artifactId>javax.servlet-api</artifactId>
	    <version>3.1.0</version>
	    <scope>provided</scope>
	</dependency>
	<dependency>
		<groupId>javax.servlet.jsp</groupId>
		<artifactId>jsp-api</artifactId>
		<version>2.1</version>
		<scope>provided</scope>
	</dependency>
	<dependency>
		<groupId>javax.servlet</groupId>
		<artifactId>jstl</artifactId>
		<version>1.2</version>
	</dependency>
	
	<!-- 런타임에 동적으로 자바 클래스의 프록시(대리(인))를 생성해주는 기능을 제공한다 -->
	<dependency>
	    <groupId>cglib</groupId>		
	    <artifactId>cglib</artifactId>
	    <version>3.3.0</version>
	</dependency>
	<dependency>
	    <groupId>commons-digester</groupId>
	    <artifactId>commons-digester</artifactId>
	    <version>1.8</version>
	</dependency>
	
	<dependency>
  		<groupId>commons-logging</groupId>
  		<artifactId>commons-logging</artifactId>
  		<version>1.1.3</version>
  	</dependency>
  	
  	<!-- Ajax 사용 설정[jackson] -->
  	<dependency>
  		<groupId>org.codehaus.jackson</groupId>	
  		<artifactId>jackson-core-asl</artifactId>
  		<version>1.9.12</version>
  	</dependency>
  	<dependency>
  		<groupId>org.codehaus.jackson</groupId>
  		<artifactId>jackson-mapper-asl</artifactId>
  		<version>1.9.12</version>
  	</dependency>
  	
  	<!-- 의존성을 추가 --> 
  	<dependency>
  		<groupId>javax.inject</groupId>
  		<artifactId>javax.inject</artifactId>
  		<version>1</version>
  	</dependency>
  	
  	<!-- JCL(자카르타 커먼스 로깅)을 사용 --> 	
  	<dependency>
  		<groupId>org.slf4j</groupId>
  		<artifactId>jcl-over-slf4j</artifactId>
  		<version>1.7.30</version>
  	</dependency>

	<!-- XML 파싱 -->
  	<dependency>
	    <groupId>jdom</groupId>
	    <artifactId>jdom</artifactId>
	    <version>1.0</version>
	</dependency>
	
	<!-- 마이 바티스 스프링 사용시 -->
  	<dependency>
	    <groupId>org.mybatis</groupId>
	    <artifactId>mybatis-spring</artifactId>
	    <version>2.0.3</version>
	</dependency>
	
  	<dependency>
	    <groupId>org.mybatis</groupId>
	    <artifactId>mybatis</artifactId>
	    <version>3.5.3</version>
	</dependency>
	
	<!-- 마이 SQL 사용시 -->	
  	<dependency>
	    <groupId>mysql</groupId>
	    <artifactId>mysql-connector-java</artifactId>
	    <version>8.0.18</version>
	</dependency>
	
	<!-- XML 파싱 -->
  	<dependency>
	    <groupId>org.jdom</groupId>
	    <artifactId>jdom</artifactId>
	    <version>2.0.1</version>
	</dependency>

	<!-- SLF4J API를 사용하도록 -->
  	<dependency>
  		<groupId>org.slf4j</groupId>
  		<artifactId>slf4j-api</artifactId>
  		<version>1.7.30</version>
  	</dependency>

	<!-- log4j -->
  	<!-- <dependency>
  		<groupId>ant</groupId>
  		<artifactId>ant-apache-log4j</artifactId>
  		<version>1.9.4</version>
  	</dependency> -->
  	
  	<dependency>
	    <groupId>commons-dbcp</groupId>
	    <artifactId>commons-dbcp</artifactId>
	    <version>1.4</version>
	</dependency>
  	
  	<!-- Map을 Bean객체로 바꾸어주는 클래스 -->
  	<dependency>
  		<groupId>commons-beanutils</groupId>
  		<artifactId>commons-beanutils-core</artifactId>
  		<version>1.8.2</version>
  	</dependency>
  	
  	<!-- DBCP : DB Connection Poll 사용 --> 
  	<dependency>
  		<groupId>com.kenai.nbpwr</groupId>
  		<artifactId>org-apache-commons-dbcp</artifactId>
  		<version>1.2.2-201002241055</version>
  		<type>nbm</type>
  	</dependency>
  	
  	<!-- IO 기능 개발을 지원하는 유틸리티 라이브러리  다운안됨 -->
  	<dependency>
  		<groupId>org.apache.commons</groupId>
  		<artifactId>commons-io</artifactId>
  		<version>1.3.2</version>
  	</dependency>
  	
  	<dependency>
  		<groupId>org.apache.commons</groupId>
  		<artifactId>commons-lang3</artifactId>
  		<version>3.9</version>
  	</dependency>
  	
  	<dependency>
  		<groupId>org.apache.commons</groupId>
  		<artifactId>commons-pool2</artifactId>
  		<version>2.8.0</version>
  	</dependency>
  	<dependency>
  		<groupId>org.slf4j</groupId>
  		<artifactId>slf4j-log4j12</artifactId>
  		<version>1.7.30</version>
  	</dependency>
  	
  	<!-- spring -->
	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-aop</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-beans</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-context</artifactId>
  		<version>5.3.6</version>
  	</dependency>  	
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-context-support</artifactId>
  		<version>5.3.6</version>
  	</dependency>  	
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-core</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-expression</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-jdbc</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-orm</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-test</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-tx</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	<dependency>
  		<groupId>org.springframework</groupId>
  		<artifactId>spring-web</artifactId>
  		<version>5.3.6</version>
  	</dependency>
  	
  	<!-- Java용 json 라이브러리(XML/YAM/CSV) data-processing 툴 -->
  	<dependency>
	    <groupId>com.fasterxml.jackson.core</groupId>
	    <artifactId>jackson-core</artifactId>
	    <version>2.12.1</version>
	</dependency>
	
	<dependency>
	    <groupId>com.fasterxml.jackson.core</groupId>
	    <artifactId>jackson-databind</artifactId>
	    <version>2.12.1</version>
	</dependency>
		
	
	
	<dependency>
	    <groupId>org.aspectj</groupId>
	    <artifactId>aspectjweaver</artifactId>
	    <version>1.9.4</version>
	</dependency>
	
	<dependency>
	    <groupId>org.aspectj</groupId>
	    <artifactId>aspectjrt</artifactId>
	    <version>1.9.4</version>
	</dependency>
	
	<!-- oracle -->
	<dependency>
	    <groupId>com.oracle.database.jdbc</groupId>
	    <artifactId>ojdbc6</artifactId>
	    <version>11.2.0.4</version>
	</dependency>
		
	<dependency>
	    <groupId>org.json</groupId>
	    <artifactId>json</artifactId>
	    <version>20190722</version>
	</dependency>	
  
</dependencies>
 
<repositories>
  	<repository>
		<id>codelds</id>		
        <!-- ojdbc6 와 함께 추가 -->
		<url>https://code.lds.org/nexus/content/groups/main-repo</url>
	</repository>
</repositories>   
 
</project>
```

- *dependency injection* : jar파일을 직접 일일 이 추가하지 않고 pom.xml에 *maven*을 통해 입력하면 jar 파일이 자동으로 추가됨 (`dependency`태그를 참조할것)

- oracle, mybatis, selenium등 다양한 *dependency* 추가 가능



# web.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://xmlns.jcp.org/xml/ns/javaee" xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd" version="4.0">
  <display-name>sprSample1</display-name>
  <welcome-file-list>
    <welcome-file>index.html</welcome-file>
    <welcome-file>index.htm</welcome-file>
    <welcome-file>index.jsp</welcome-file>
    <welcome-file>default.html</welcome-file>
    <welcome-file>default.htm</welcome-file>
    <welcome-file>default.jsp</welcome-file>
  </welcome-file-list>
  
<servlet>
	<servlet-name>dispatcherServlet</servlet-name>
	<servlet-class>
		org.springframework.web.servlet.DispatcherServlet
	</servlet-class>
	
	<init-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>
			/WEB-INF/spring/servlet-context.xml
		</param-value>
	</init-param>
	
	<load-on-startup>1</load-on-startup>
	
</servlet>

<servlet-mapping>
	<servlet-name>dispatcherServlet</servlet-name>
	<!-- <url-pattern>/</url-pattern> -->
	<url-pattern>*.do</url-pattern>
</servlet-mapping>  
  
<!-- DB 관련 -->  
<context-param>
	<param-name>contextConfigLocation</param-name>
	<param-value>
		/WEB-INF/spring/applicationContext.xml
	</param-value>
</context-param>

<listener>
	<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
  
  
</web-app>
```





- `welcome-file-list`태그 따로 url을 설정하지 않아도 열수 있는 파일(주로 index나 default를 설정한다.)
- `servlet`태그 : *model2*에서는 web.xml에서 controller로 바로 servlet-mapping을 해줬지만, spring에서는 *dispatcherservlet*을 통해 servlet-mapping을 해주기 때문에 `init-param`태그를 통해 dispatcherservlet으로 mapping해준다.
- `context-param`태그 : db설정에 관련된 xml파일을 mapping해준다.
- `listner`태그: db설정 xml파일에 쿼리문을 넘겨줄 클래스를 정해준다.



# servlet-context.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

	<!-- spring MVC annotation(주석문, 지시어)을 사용하기 위한 설정 -->
	<context:annotation-config/>

	<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="prefix" value="/WEB-INF/views/"></property>	<!-- views의 경로 -->
		<property name="suffix" value=".jsp"></property> <!-- 확장자명은 jsp -->
	</bean>
	<!-- InternalResourceViewResolver viewResolver = new InternalResourceViewResolver(); 
		 viewResolver.prefix = "/WEB-INF/views";
	-->
	
	<context:component-scan base-package="mul.cum.a"/>	


</beans>

```



- `<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">`  연결할 jsp파일 url경로 설정

- `<context:component-scan base-package="mul.cum.a"/>	` 사용할 java파일을 저장해놓은 default package





# applicationContext.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

	<!-- Database 설정 -->
	
	<!-- DB 초기화 파일의 위치 -->
	<bean id="propertyConfigurer" class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
		<property name="locations">
			<list>
				<value>classpath:properties/jdbc.properties</value>
			</list>
		</property>
	</bean>
	
	<!-- DBMS(DataBase Management System) -->	
	<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
		<property name="driverClassName" value="${jdbc.drvierClassName}"/>		
		<property name="url" value="${jdbc.url}"/>
		<property name="username" value="${jdbc.username}"/>
		<property name="password" value="${jdbc.password}"/>
		<property name="initialSize" value="${jdbc.initialSize}"/>
		<property name="maxActive" value="${jdbc.maxActive}"/>
		<property name="minIdle" value="${jdbc.initialSize}"/>
		<property name="maxWait" value="3000"/>
		<property name="poolPreparedStatements" value="true"/>
		<property name="maxOpenPreparedStatements" value="50"/>	
	</bean>

	<!-- mybatis setting -->
	<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
		<property name="dataSource" ref="dataSource"/>
		<property name="mapperLocations" value="classpath:sqls/*.xml"/>
	</bean>
		
	<!-- sqlSession 취득 -->
	<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
		<constructor-arg index="0" ref="sqlSessionFactory"/>
		<constructor-arg index="1" value="SIMPLE"/>		<!-- value="batch" -->
	</bean>
	
	<!-- jdbc 설정 -->
	<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
		<property name="dataSource" ref="dataSource"/>
	</bean>	
</beans>
```



- applicationContext.xml을 통해서 db연결 jdbc설정을 모두 세팅해줌







