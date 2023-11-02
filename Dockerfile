## FROM maven:3.8.2-jdk-8 # for Java 8
#FROM maven:3.8.5-openjdk-17
#
#WORKDIR /demo-app
#COPY . .
#RUN mvn clean install
#
#CMD mvn spring-boot:run


# Use the specified Maven version with OpenJDK 17
FROM maven:3.8.5-openjdk-17

# Set the working directory in the Docker image
WORKDIR /demo-app

# First, copy the pom.xml file. This layer will be cached until the pom.xml file changes.
COPY pom.xml .

# Download dependencies as a separate step so the Docker cache can reuse them.
# This will only re-run if the pom.xml file changes.
RUN mvn dependency:go-offline --batch-mode

# Then, copy the rest of the application's source files
COPY src src

# Now build the application using the cached layers for dependencies.
# This will only re-run if the source files change.
RUN mvn clean install

# When the container starts, run the application.
CMD ["mvn", "spring-boot:run"]
