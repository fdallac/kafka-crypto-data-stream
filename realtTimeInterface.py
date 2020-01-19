import numpy as np 
import pandas as pd 
import time

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Div
from bokeh.plotting import figure, curdoc
from bokeh.server.server import Server

from kafkaHelper import initConsumer, consumeRecord
from config import config, params

data_1 = pd.DataFrame(columns=['time', 'value'])
data_2 = pd.DataFrame(columns=['time', 'value'])
data_3 = pd.DataFrame(columns=['time', 'value'])

def updateDataFrames():
    # consume data from Kafka
    records_1 = consumeRecord(consumer_1)
    records_2 = consumeRecord(consumer_2)
    records_3 = consumeRecord(consumer_3)
    # debug \ message in prompt
    print('Consume records from all topics at time {0}'.format(time.time()))

    for r in records_1:
        data_1.loc[len(data_1)] = [int(r['timestamp']), float(r['amount'])]
    for r in records_2:
        data_2.loc[len(data_2)] = [int(r['timestamp']), float(r['amount'])]
    for r in records_3:
        data_3.loc[len(data_3)] = [int(r['timestamp']), float(r['amount'])]


# plot data sources
source_1 = ColumnDataSource(data=dict(x=[], y=[]))
source_2 = ColumnDataSource(data=dict(x=[], y=[]))
source_3 = ColumnDataSource(data=dict(x=[], y=[]))

def bkinterface(doc):

    # plot 1
    p_1 = figure(width=420, height=400, toolbar_location=None, title='Currency: {}'.format(params['currency_1']))
    p_1.yaxis.axis_label = params['ref_currency']
    p_1.border_fill_color = 'black'
    p_1.background_fill_color = 'black'
    p_1.outline_line_color = None
    p_1.grid.grid_line_color = None
    p_1.line('x', 'y', source=source_1, line_color='white', line_width=1.5)
    # plot 2
    p_2 = figure(width=420, height=400, toolbar_location=None, title='Currency: {}'.format(params['currency_2']))
    p_2.yaxis.axis_label = params['ref_currency']
    p_2.border_fill_color = 'black'
    p_2.background_fill_color = 'black'
    p_2.outline_line_color = None
    p_2.grid.grid_line_color = None
    p_2.line('x', 'y', source=source_2, line_color='white', line_width=1.5)
    # plot 3
    p_3 = figure(width=420, height=400, toolbar_location=None, title='Currency: {}'.format(params['currency_3']))
    p_3.yaxis.axis_label = params['ref_currency']
    p_3.border_fill_color = 'black'
    p_3.background_fill_color = 'black'
    p_3.outline_line_color = None
    p_3.grid.grid_line_color = None
    p_3.line('x', 'y', source=source_3, line_color='white', line_width=1.5)

    def callback():
        # call kafka consumers and update data
        updateDataFrames()
        # update charts values
        t_1_min = data_1['time'].min()
        source_1.data = dict(x=[int(d - t_1_min) for d in data_1['time']], y=data_1['value'])
        t_2_min = data_2['time'].min()
        source_2.data = dict(x=[int(d - t_2_min) for d in data_2['time']], y=data_2['value'])
        t_3_min = data_3['time'].min()
        source_3.data = dict(x=[int(d - t_3_min) for d in data_3['time']], y=data_3['value'])        

    # text divs
    header_text = Div(text='''<a style="font-size:30px"><b>Cryptocurrencies dynamics visualization</b></a><br>
        By: Filippo Dalla Chiara, Ibrahim Farajov (ESILV, 2020)''')
    bottom_text = Div(text='''Written in: Python<br>Using: Apache Kafka, Bokeh, Anaconda<br>Data source: Coinbase API''')

    # document layout
    doc.add_root(column(header_text, row(p_1, p_2, p_3), bottom_text))
    # document updating
    doc.add_periodic_callback(callback, 2500)

# run server
server = Server({'/': bkinterface})
server.start()

if __name__ == '__main__':
    print('Starting Apache Kafka consumer')
    consumer_1 = initConsumer(config['topic_1'])
    consumer_2 = initConsumer(config['topic_2'])
    consumer_3 = initConsumer(config['topic_3'])

    print('Opening Bokeh application on http://localhost:5006/')
    server.io_loop.add_callback(server.show, '/')
    server.io_loop.start()






