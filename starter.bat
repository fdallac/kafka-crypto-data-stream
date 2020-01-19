set ZOOKEEPER_LOGS_PATH=...
set KAFKA_LOGS_PATH=...
set KAFKA_PATH=...
set ANACONDA_PATH=...
set THIS_PATH=...

echo Preparing system
echo off
rmdir /q /s %ZOOKEEPER_LOGS_PATH%
rmdir /q /s %KAFKA_LOGS_PATH%
timeout 1
echo Starting Zookeeper
start cmd /k %KAFKA_PATH%\bin\windows\zookeeper-server-start.bat %KAFKA_PATH%\config\zookeeper.properties
timeout 5
echo Starting Kafka Server
start cmd /k %KAFKA_PATH%\bin\windows\kafka-server-start.bat %KAFKA_PATH%\config\server.properties
timeout 15
start cmd /k %ANACONDA_PATH%/python.exe %THIS_PATH%/realTimeDataCollector.py /k
start cmd /k %ANACONDA_PATH%/python.exe %THIS_PATH%/realTimeMA.py /k
start cmd /k %ANACONDA_PATH%/python.exe %THIS_PATH%/realTimeInterface.py /k

