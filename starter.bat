echo Preparing system
echo off
rmdir /q /s C:\%ZOOKEEPER_LOGS_FOLDER%
rmdir /q /s C:\%KAFKA_LOGS_FOLDER%
timeout 1
echo Starting Zookeeper
start cmd /k C:\%KAFKA_FOLDER%\bin\windows\zookeeper-server-start.bat C:\%KAFKA_FOLDER%\config\zookeeper.properties
timeout 5
echo Starting Kafka Server
start cmd /k C:\%KAFKA_FOLDER%\\bin\windows\kafka-server-start.bat C:\%KAFKA_FOLDER%\\config\server.properties
timeout 15
start cmd /k C:/%ANACONDA_FOLDER%/Anaconda3/python.exe c:/%THIS_APP_FOLDER%/realTimeDataCollector.py /k
start cmd /k C:/%ANACONDA_FOLDER%/Anaconda3/python.exe c:/%THIS_APP_FOLDER%/realtTimeInterface.py /k
