import uvicorn
from fastapi import FastAPI

import base
import cnhistroy
import model

app = FastAPI()


@app.get("/adp/cn/stock-history")
async def getCnStockHistory(symbol: str, start: str, end: str, adj: str = "") -> model.Response:
    rsp = cnhistroy.getStockDailyHistory(symbol, start, end, adj)
    return rsp


@app.get("/api/hq/get-symbol")
async def getCnDaily(stock: str, start_date: str, end_date: str) -> model.SingleDataRsp:
    rsp = cnhistroy.getCnDaily(stock, start_date, end_date)
    return rsp


@app.get("/api/hq/get-cn-basic")
async def getCnBasic(page_num: int) -> model.SingleDataRsp:
    rsp = cnhistroy.getCnBasic(page_num)
    return rsp


@app.get("/api/hq/trade-cal")
async def tradeCal(start_date: str, end_date: str) -> model.Response:
    rsp = cnhistroy.tradeCal('SSE', start_date, end_date)
    return rsp


if __name__ == "__main__":
    base.logger.info("server started")
    config = uvicorn.Config("main:app", host='127.0.0.1', port=19080, log_level="info")
    server = uvicorn.Server(config)
    server.run()
