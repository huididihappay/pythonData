# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, Integer, Date, BigInteger, DateTime, VARCHAR, text, Index, \
    Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LocationInventoryRecord(Base):
    __tablename__ = 'location_inventory_modify_record'
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __init__(self):
        pass


class LocationInventory(Base):
    __tablename__ = 'location_inventory'
    __table_args__ = (
        Index('location_inventory_uindex', 'location_inventory_id', 'warehouse_code', unique=True),
        Index('location_inventory_index', 'tote_no', 'item_id', 'customer_code', 'expiry_date', 'warehouse_code'),
        {'comment': '库存信息数据表'}
    )

    id = Column(BigInteger, primary_key=True)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    created_by = Column(VARCHAR(64), server_default=text("'system'"), comment='创建人')
    deleted = Column(Integer, nullable=False, server_default=text("'0'"), comment='是否被删除（0、否  1、是）')
    last_modified_by = Column(VARCHAR(64), server_default=text("'system'"), comment='最后修改人')
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='最后修改时间')
    warehouse_code = Column(VARCHAR(64), nullable=False, server_default=text("'ce'"), comment='仓库编码')
    available_quantity = Column(Integer, server_default=text("'0'"),
                                comment='可用数量（availableQuantity=checkQty-frozenQuantity || availableQuantity=quantity-frozenQuantity）')
    bar_code = Column(VARCHAR(256), comment='商品条码, 多个以逗号分割')
    batch_no = Column(VARCHAR(64), comment='批次编码')
    check_diff_qty = Column(Integer, server_default=text("'0'"),
                            comment='盘点数量与库存数量的差值（checkDiffQty=checkQty-(availableQuantity+frozenQuantity)）')
    check_id = Column(VARCHAR(64), comment='盘点单号 id, 对应 stocktake_bill 表的 stocktake_bill_id')
    check_qty = Column(Integer, comment='盘点数量')
    check_time = Column(DateTime, comment='盘点时间')
    customer_code = Column(VARCHAR(64), comment='货主编码')
    customer_name = Column(VARCHAR(128), comment='货主名称')
    expiry_date = Column(Date, comment='有效日期')
    frozen_quantity = Column(Integer, server_default=text("'0'"), comment='冻结数量')
    item_id = Column(VARCHAR(64), comment='产品编号')
    item_name = Column(VARCHAR(256), comment='商品名称')
    location_inventory_id = Column(VARCHAR(64), nullable=False, comment='库存明细 id')
    location_no = Column(VARCHAR(64), comment='库位编号')
    normal_flag = Column(Boolean, server_default=text("'0'"), comment='正残标志（0、正常  1、残次）')
    produce_date = Column(Date, comment='生产日期')
    quantity = Column(Integer, server_default=text("'0'"), comment='总数量（quantity=checkQty）')
    tote_no = Column(VARCHAR(64), comment='料箱编号, 和 location_no 二选一; kiva用 location_no; 双边用 tote_no')
    warehouse_name = Column(VARCHAR(128), comment='仓库名称')

    # class LocationInventory(Base):
    #     __tablename__ = 'location_inventory'
    #
    #     id = Column(Integer, primary_key=True, autoincrement=True)
    #     deleted = Column(Integer)
    #     warehouse_code = Column(String(64))
    #     bar_code = Column(String(256))
    #     customer_code = Column(String(64))
    #     item_id = Column(String)
    #     item_name = Column(String)
    #     location_inventory_id = Column(String)
    #     tote_no = Column(String)
    #     quantity = Column(Integer)
    #     available_quantity = Column(Integer)
    #     batch_no = Column(String)
    #     frozen_quantity = Column(Integer)
    #     expiry_date = Column(Date)

    def __init__(self, warehouse_code, customer_code,
                 item_id, bar_code, item_name, expiry_date, batch_no,
                 tote_no,
                 quantity, available_quantity, frozen_quantity
                 ):
        self.warehouse_code = warehouse_code
        self.customer_code = customer_code
        self.item_id = item_id
        self.bar_code = bar_code
        self.item_name = item_name
        self.batch_no = batch_no
        self.create_time = datetime.datetime.now()

        self.tote_no = tote_no

        self.quantity = quantity
        self.frozen_quantity = frozen_quantity
        self.available_quantity = available_quantity
        self.expiry_date = expiry_date
        self.deleted = 0
        self.location_inventory_id = tote_no + "_" + item_id
