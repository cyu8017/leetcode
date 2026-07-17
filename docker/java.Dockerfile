FROM eclipse-temurin:21.0.4_7-jdk-jammy

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 unzip curl \
    && rm -rf /var/lib/apt/lists/*

# Kotlin compiler (pinned) for the kotlin runner's toolchain gate
RUN curl -fsSL -o /tmp/kotlin.zip https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip \
    && unzip -q /tmp/kotlin.zip -d /opt \
    && rm /tmp/kotlin.zip \
    && ln -s /opt/kotlinc/bin/kotlinc /usr/local/bin/kotlinc

# Scala compiler (pinned) for the scala runner's toolchain gate
RUN curl -fsSL -o /tmp/scala.tgz https://downloads.lightbend.com/scala/2.13.14/scala-2.13.14.tgz \
    && tar -xzf /tmp/scala.tgz -C /opt \
    && rm /tmp/scala.tgz \
    && ln -s /opt/scala-2.13.14/bin/scalac /usr/local/bin/scalac \
    && ln -s /opt/scala-2.13.14/bin/scala /usr/local/bin/scala

WORKDIR /workspace
