import tushare as ts
import yfinance as yf
from pandas_datareader import data as pdr

import base
import configure
import model

yf.pdr_override()
pro = ts.pro_api(token=configure.tu_share_token, timeout=30)


def getStockDailyHistory(symbol: str, start: str, end: str, adj: str) -> model.Response:
    """"""
    base.logger.info("load symbol=%s, start=%s,end=%s", symbol, start, end)
    rsp = model.Response()
    rsp.status = 200
    rsp.msg = "OK"

    # noinspection PyBroadException
    try:
        df = pdr.get_data_yahoo(symbol, start, end)
        if len(df.index) == 0:
            """"""
            return rsp
        print("-----------------------------------------:%s" % type(df))
        for row in df.iterrows():
            """"""
            st = model.StockPrice()
            st.day = row[0]
            st.open = row[1][0]
            st.high = row[1][1]
            st.low = row[1][2]
            st.close = row[1][3]
            st.vol = row[1][4]
            rsp.data.append(st)
        return rsp
    except Exception as ex:
        base.logger.warn("exceptions:%s", ex)
        rsp.status = 500
        rsp.msg = "Exception"
        return rsp


def getCnDaily(symbol: str, start: str, end: str) -> model.SingleDataRsp:
    rsp = model.SingleDataRsp()
    rsp.status = 200
    rsp.msg = "OK"
    try:
        hq_data = pro.daily(ts_code=symbol, start_date=start, end_date=end)
        total = len(hq_data)
        daily_items = model.TjDailyItems()
        daily_items.tsCode = symbol
        for row in range(0, total):
            """"""
            daily = model.TjCnDailyInfo()
            daily.symbol = hq_data.loc[row, 'ts_code']
            daily.tradeDate = hq_data.loc[row, 'trade_date']
            daily.open = hq_data.loc[row, 'open']
            daily.close = hq_data.loc[row, 'close']
            daily.preClose = hq_data.loc[row, 'pre_close']
            daily.high = hq_data.loc[row, 'high']
            daily.low = hq_data.loc[row, 'low']
            daily.change = hq_data.loc[row, 'change']
            daily.pctChg = hq_data.loc[row, 'pct_chg']
            daily.amount = hq_data.loc[row, 'amount']
            daily.vol = hq_data.loc[row, 'vol']
            daily_items.dtoList.insert(0, daily)
        """"""
        rsp.data = daily_items
        return rsp
    except Exception as ex:
        base.logger.warn("exceptions:%s", ex)
        rsp.status = 500
        rsp.msg = "Exception"
        return rsp


def tradeCal(exchange: str, start_date: str, end_date: str) -> model.Response:
    """"""
    rsp = model.Response()
    rsp.status = 200
    rsp.msg = "OK"
    try:
        data_item = pro.query('trade_cal', exchange=exchange, start_date=start_date, end_date=end_date)
        total = len(data_item)
        for row in range(0, total):
            """"""
            td = model.TjTradeDate()
            td.exchange = exchange
            td.cal_date = data_item.loc[row, 'cal_date']
            td.is_open = int(data_item.loc[row, 'is_open'])
            td.pretrade_date = data_item.loc[row, 'pretrade_date']
            rsp.data.append(td)
        """"""
        print("total:", total)
        return rsp
    except Exception as ex:
        base.logger.warn("exceptions:%s", ex)
        rsp.status = 500
        rsp.msg = "Exception"
        return rsp


def getCnBasic(page_number: int) -> model.Response:
    """"""
    rsp = model.SingleDataRsp()
    rsp.status = 200
    rsp.msg = "OK"
    data = model.TjCnBasicPage()
    data.pageSize = 10000
    rsp.data = data
    field_list = 'ts_code,name,area,industry,fullname,enname,cnspell,market,exchange,list_status,list_date,' \
                 'delist_date,is_hs '
    try:
        basic_data = pro.query('stock_basic', exchange='', list_status='L', fields=field_list)
        total = len(basic_data)
        data.pageSize = total + 100
        for row in range(0, total):
            """"""
            bd = model.TjCnBasicInfo()
            bd.symbol = basic_data.loc[row, 'ts_code']
            bd.name = basic_data.loc[row, 'name']
            bd.area = basic_data.loc[row, 'area']
            bd.industry = basic_data.loc[row, 'industry']
            bd.fullname = basic_data.loc[row, 'fullname']
            bd.enname = basic_data.loc[row, 'enname']
            bd.cnspell = basic_data.loc[row, 'cnspell']
            bd.market = basic_data.loc[row, 'market']
            bd.exchange = basic_data.loc[row, 'exchange']
            bd.status = basic_data.loc[row, 'list_status']
            bd.list_date = basic_data.loc[row, 'list_date']
            bd.delist_date = basic_data.loc[row, 'delist_date']
            bd.is_hs = basic_data.loc[row, 'is_hs']
            data.items.append(bd)
    except Exception as ex:
        base.logger.warn("exceptions:%s", ex)
        rsp.status = 500
        rsp.msg = "Exception"
        return rsp
