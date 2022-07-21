# !/usr/bin/env python
# -*- coding: utf-8 -*-

from mysql_data import session,createAll
from models.stocktake import StockTakeDetail
from models.inventory import LocationInventory


def locationInventory():
    #获取所有的盘点单
    all_stock = session.query(StockTakeDetail).all()
    objs = []
    i = 0
    for stock in all_stock:
        i = i+1
        tote_no = "gu"+str(i)
        '''
          def __init__(self, warehouse_code, customer_code,
                 item_id, bar_code, item_name, expiry_date, batch_no,
                 tote_no,
                 quantity, available_quantity, frozen_quantity
                 ):
        '''
        o = LocationInventory(stock.warehouse_code,'ZNO1',stock.item_id,
                              "*",stock.item_name,stock.expiry_date,stock.batch_no,tote_no,stock.stocktaking_quantity,stock.stocktaking_quantity,0)
        objs.append(o)
    createAll(objs)

if __name__ == "__main__":
    locationInventory()
