from pydantic import BaseModel
from typing import Union


class Response(BaseModel):
    status: int = 200
    msg: str = "OK"
    data: list = []


class SingleDataRsp(BaseModel):
    status: int = 200
    msg: str = "OK"
    data: object = None


class StockPrice(BaseModel):
    day: Union[str, None] = None
    open: Union[float, None] = None
    close: Union[float, None] = None
    high: Union[float, None] = None
    low: Union[float, None] = None
    vol: Union[float, None] = None
    amount: Union[float, None] = None
    amp: Union[float, None] = None
    change: Union[float, None] = None
    pct_chg: Union[float, None] = None
    turnover: Union[float, None] = None


class TjCnDailyInfo(BaseModel):
    symbol: Union[str, None] = None
    tradeDate: Union[str, None] = None
    open: Union[float, None] = None
    close: Union[float, None] = None
    preClose: Union[float, None] = None
    high: Union[float, None] = None
    low: Union[float, None] = None
    vol: Union[float, None] = None
    amount: Union[float, None] = None
    pctChg: Union[float, None] = None
    change: Union[float, None] = None


class TjCnBasicInfo(BaseModel):
    symbol: Union[str, None] = None
    name: Union[str, None] = None
    area: Union[str, None] = None
    industry: Union[str, None] = None
    fullname: Union[str, None] = None
    enname: Union[str, None] = None
    cnspell: Union[str, None] = None
    market: Union[str, None] = None
    exchange: Union[str, None] = None
    status: Union[str, None] = None
    list_date: Union[str, None] = None
    delist_date: Union[str, None] = None
    is_hs: Union[str, None] = None


class TjDailyItems(BaseModel):
    tsCode: Union[str, None] = None
    dtoList: list = []


class TjTradeDate(BaseModel):
    exchange: Union[str, None] = None
    cal_date: Union[str, None] = None
    is_open: Union[int, None] = None
    pretrade_date: Union[str, None] = None


class TjCnBasicPage(BaseModel):
    pageSize: Union[int, None] = None
    items: list = []
