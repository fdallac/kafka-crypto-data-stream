echo Preparing system
echo off
rmdir /q /s C:\Tools\kafka\zk-data
rmdir /q /s C:\Tools\kafka\kafka-logs
timeout 1
echo Starting Zookeeper
start cmd /k C:\Tools\kafka\bin\windows\zookeeper-server-start.bat C:\Tools\kafka\config\zookeeper.properties
timeout 5
echo Starting Kafka Server
start cmd /k C:\Tools\kafka\bin\windows\kafka-server-start.bat C:\Tools\kafka\config\server.properties
timeout 15
start cmd /k C:/Users/Filippo/Anaconda3/python.exe c:/Users/Filippo/Desktop/ESILV/NOSql/_finalProject/realTimeDataCollector.py /k
start cmd /k C:/Users/Filippo/Anaconda3/python.exe c:/Users/Filippo/Desktop/ESILV/NOSql/_finalProject/realTimeMA.py /k
start cmd /k C:/Users/Filippo/Anaconda3/python.exe c:/Users/Filippo/Desktop/ESILV/NOSql/_finalProject/realTimeInterface.py /k

