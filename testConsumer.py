# main consumer
import util.consumer as con
import time

# start consumer 
c = con.initConsumer('test')


for t in range(10):
    print('Reading #{}'.format(t))
    con.consumeAndPrintRecords(c)
    time.sleep(6)
