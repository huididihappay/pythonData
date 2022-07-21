# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

'''
create table stocktake_bill
(
    id                bigint auto_increment
        primary key,
    create_time       datetime    default CURRENT_TIMESTAMP not null comment '创建时间',
    created_by        varchar(64) default 'system'          null comment '创建人',
    deleted           tinyint(1)  default 0                 not null comment '是否被删除（0、否  1、是）',
    last_modified_by  varchar(64) default 'system'          null comment '最后修改人',
    update_time       datetime    default CURRENT_TIMESTAMP not null comment '最后修改时间',
    warehouse_code    varchar(64) default 'ce'              not null comment '仓库编码',
    can_cancel        bit         default b'1'              null comment '是否可以取消（默认 true）',
    customer_code     varchar(64)                           null comment '货主编码',
    priority          tinyint(1)  default 0                 null comment '优先级',
    status            tinyint(1)  default 1                 not null comment '盘点单状态',
    stocktake_bill_id varchar(64)                           not null comment '盘点单 id',
    constraint stocktake_bill_uindex
        unique (stocktake_bill_id, warehouse_code)
)
'''


class StockTake(Base):
    __tablename__ = 'stocktake_bill'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deleted = Column(Integer)
    warehouse_code = Column(String(64))
    update_time = Column(DateTime)
    priority = Column(Integer)
    status = Column(Integer)
    stocktake_bill_id = Column(String)
    create_time = Column(String)

    def __init__(self, warehouse_code, customer_code,
                 stocktake_bill_id, priority
                 ):
        self.warehouse_code = warehouse_code

        self.create_time = datetime.datetime.now()
        self.warehouse_code = warehouse_code
        self.stocktake_bill_id = stocktake_bill_id
        self.priority = priority
        self.deleted = 0
        self.status = 1
        self.update_time = datetime.datetime.now()


"""
create table stocktake_bill_detail
(
    id                       bigint auto_increment
        primary key,
    create_time              datetime    default CURRENT_TIMESTAMP not null comment '创建时间',
    created_by               varchar(64) default 'system'          null comment '创建人',
    deleted                  tinyint(1)  default 0                 not null comment '是否被删除（0、否  1、是）',
    last_modified_by         varchar(64) default 'system'          null comment '最后修改人',
    update_time              datetime    default CURRENT_TIMESTAMP not null comment '最后修改时间',
    warehouse_code           varchar(64) default 'ce'              not null comment '仓库编码',
    batch_no                 varchar(64)                           null comment '批次编码, 如有必填',
    expiry_date              date                                  not null comment '有效日期',
    item_id                  varchar(64)                           not null comment 'sku 编码 == bar_code',
    item_name                varchar(256)                          null comment '商品名称',
    normal_flag              tinyint(1)  default 0                 null comment '产品形态: 0正品/1残品',
    operator                 varchar(64)                           null comment '盘点操作员',
    stocktake_bill_detail_id varchar(64)                           not null comment '盘点单明细 id',
    stocktake_bill_id        varchar(64)                           not null comment '盘点单 id',
    stocktaking_quantity     int         default 0                 null comment '盘点数量，实际盘点时填入',
    constraint stocktake_bill_detail_uindex
        unique (stocktake_bill_detail_id, stocktake_bill_id, warehouse_code)
)
"""


class StockTakeDetail(Base):
    __tablename__ = 'stocktake_bill_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deleted = Column(Integer)
    warehouse_code = Column(String(64))

    batch_no = Column(String)
    expiry_date = Column(Date)
    item_id = Column(String)
    item_name = Column(String)
    normal_flag = Column(Boolean)

    stocktake_bill_detail_id = Column(String)
    stocktake_bill_id = Column(String)

    stocktaking_quantity = Column(Integer)

    def __init__(self, warehouse_code, customer_code,
                 stocktake_bill_id, stocktake_bill_detail_id,
                 item_id, item_name, batch_no, expiry_date
                 ):
        self.warehouse_code = warehouse_code
        self.customer_code = customer_code
        self.item_id = item_id
        self.item_name = item_name
        self.batch_no = batch_no
        self.expiry_date = expiry_date
        self.stocktake_bill_id = stocktake_bill_id
        self.stocktake_bill_detail_id = stocktake_bill_detail_id

        self.create_time = datetime.datetime.now()
        self.deleted = 0
        self.pick_quantity = 0
        self.allocated_quantity = 0
        self.normal_flag = 0
        self.stocktaking_quantity = 0
