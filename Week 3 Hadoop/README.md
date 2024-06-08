# Running Hadoop

1. Make a working directory, somewhere

```
mkdir running-hadoop
cd running-hadoop
```

2. Clone the big-data-europe fork for commodity hardware

```
git clone https://github.com/wxw-matt/docker-hadoop.git
cd docker-hadoop
```

3. Test Docker 

I didn't have my Docker running and had to start it.

```
docker run hello-world
```

4. Change version - we need to use docker-compose-v2, but the docker-compose command will look for an unversioned file.

```
mv docker-compose.yml docker-compose-v1.yml
mv docker-compose-v3.yml docker-compose.yml
```

This will draw two warnings - you can fix the files or ignore both.


5. Bring the Hadoop containers up (took me 81.6s). I had previously pulled other hadoop images though so your time may vary.

```
docker-compose up -d
```

6. In a Hadoop cluster, we mostly work within the namenode. 

I used "docker ps" to list the nodes, then picked the one with name in it. For me:

```
docker ps
CONTAINER ID   IMAGE                                                    COMMAND                  CREATED         STATUS                            PORTS      NAMES
de4a8afd3940   wxwmatt/hadoop-historyserver:2.1.1-hadoop3.3.1-java8     "/entrypoint.sh /run…"   6 seconds ago   Up 4 seconds (health: starting)   8188/tcp   docker-hadoop-historyserver-1
a0e551086c0c   wxwmatt/hadoop-namenode:2.1.1-hadoop3.3.1-java8          "/entrypoint.sh /run…"   6 seconds ago   Up 4 seconds (health: starting)   9870/tcp   docker-hadoop-namenode-1
7b70e2a0bbb3   wxwmatt/hadoop-nodemanager:2.1.1-hadoop3.3.1-java8       "/entrypoint.sh /run…"   6 seconds ago   Up 5 seconds (health: starting)   8042/tcp   docker-hadoop-nodemanager-1
46e45d7b9f49   wxwmatt/hadoop-resourcemanager:2.1.1-hadoop3.3.1-java8   "/entrypoint.sh /run…"   6 seconds ago   Up 4 seconds                      8088/tcp   docker-hadoop-resourcemanager-1
a31b6cbaa2d8   wxwmatt/hadoop-datanode:2.1.1-hadoop3.3.1-java8          "/entrypoint.sh /run…"   6 seconds ago   Up 5 seconds (health: starting)   9864/tcp   docker-hadoop-datanode-1
```

So I used:

```
docker exec -it docker-hadoop-namenode-1 /bin/bash
```

### This is where me and Cameron ran into the problem with the Apple chips and could not finish. The node repeatedly kept crashing and restarting.
