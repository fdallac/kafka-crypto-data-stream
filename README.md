# Data streaming of (crypto) currencies dynamics with Apache Kafka
In this project we developed a financial data streaming, processing and visualization on crypto currencies. The core of the project is the streaming system Apache Kafka, that allows the blocks to communicate rapidly a great amount of data.\
At the moment the data processing is limited to the computation of technical indicator like moving average, but in the future it could be implemented some Machine Learning prediction technique (with Apache Spark), and a storage for the data like Cassandra.\
All the implementions could be part of a bigger project of automatic trading.

# Components
- config.py: stores configuration parameters for an easy setup of the app
- kafkaHelper.py: stores the method to use Apache Kafka in python
- realTimeDataCollector.py: uses asynchronously kafka producers to call Coinbase API and get financial data, then sends records on Kafka framework, to be used by consumers. Each cryptocurrency has a dedicated topic in the stream.
- realTimeInterface.py: consumes financial records and plot them on Bokeh server.
- ???.py: consumers row financial data from realTimeDataCollector, computes technical indicators (moving average) and produces them to be plotted by realTimeDataInterface
- starter.bat: bat file to start the app in windows OS, needs to be configurated with the folder of Apache Kafka, Anaconda and this files on your own PC

# Software structure
![structure](https://user-images.githubusercontent.com/57987109/72688379-de154580-3b06-11ea-92e2-84166473d357.png)

# Preview
![Interface](https://i.ibb.co/BnN5wMW/preview.png)


