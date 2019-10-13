import xlrd
import xlwt
import tushare as ts
#Tushare是一个免费、开源的python财经数据接口包。主要实现对股票等金融数据从数据采集、清洗加工 到 数据存储的过程
#TaLib是一个Python金融指数处理库。包含了很多技术分析里的常用参数指标，例如MA、SMA、WMA、MACD、ATR等。
#token码
#c4b9012e9af4f0da32da8be5b8801c2cc9d1f69d32fb5291af77fa04

print(ts.__version__)
pro = ts.pro_api('c4b9012e9af4f0da32da8be5b8801c2cc9d1f69d32fb5291af77fa04')

#stockdata=ts.get_hist_data('sz',start='2019-09-01',end='2019-09-10')
##########获取交易数据参数
# code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
# start：开始日期，格式YYYY-MM-DD
# end：结束日期，格式YYYY-MM-DD
# ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
#print(stockdata)
##########################获取历史交易数据结果
# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5日均价
# ma10：10日均价
# ma20:20日均价
# v_ma5:5日均量
# v_ma10:10日均量
# v_ma20:20日均量
# turnover:换手率
#####################按行业取得股票
def getstockindustry():
    cfield=ts.get_industry_classified()
    print(cfield)
    cfield.to_excel('d:/pythontest/行业.xlsx')
# pandas将数据保存为MicroSoft Excel文件格式。
#
# 常用参数说明：
#
# excel_writer: 文件路径或者ExcelWriter对象
# sheet_name:sheet名称，默认为Sheet1
# sep : 文件内容分隔符，默认为,逗号
# na_rep: 在遇到NaN值时保存为某字符，默认为’‘空字符
# float_format: float类型的格式
# columns: 需要保存的列，默认为None
# header: 是否保存columns名，默认为True
# index: 是否保存index，默认为True
# encoding: 文件编码格式
# startrow: 在数据的头部留出startrow行空行
# startcol :在数据的左边留出startcol列空列
#####按概念取得股票名称
#ts.get_concept_classified()
# code：股票代码
# name：股票名称
# c_name：概念名称
############按地域取得股票名称
#ts.get_area_classified()
##########沪深300成份及权重
#ts.get_hs300s()
# code :股票代码
# name :股票名称
# date :日期
# weight:权重
#############上证50成份股
#ts.get_sz50s()
############中证500成份股
#ts.get_zz500s()
def getstockdata():
    myworkbook=xlrd.open_workbook('d:/pythontest/行业.xlsx','rb')
    mysheet=myworkbook.sheet_by_name('stock')
    for i in range(1,2740):
        try:
            stockcode=mysheet.cell_value(i,1)
            stockdata=ts.get_hist_data(stockcode,start='2017-01-01',end='2019-09-11')
            filename='d:/pythontest/stock/'+stockcode+'.xlsx'
            stockdata.to_excel(filename)
        except:
            continue

# 分配预案¶
# 参数说明：
# year : 预案公布的年份，默认为2014
# top :取最新n条数据，默认取最近公布的25条
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
# 返回值说明：
# code:股票代码
# name:股票名称
# year:分配年份
# report_date:公布日期
# divi:分红金额（每10股）
# shares:转增和送股数（每10股
def stockfh():
    df = ts.profit_data(year=2016,top=1000)
    df.to_excel('d:/pythontest/stock/股票2016分红.xlsx')
    df = ts.profit_data(year=2017,top=1000)
    df.to_excel('d:/pythontest/stock/股票2017分红.xlsx')
    df = ts.profit_data(year=2018,top=1000)
    df.to_excel('d:/pythontest/stock/股票2018分红.xlsx')
    df = ts.profit_data(year=2019,top=1000)
    df.to_excel('d:/pythontest/stock/股票2019分红.xlsx')
#stockfh()

# 业绩预告¶
# 参数说明：
# year:int 年度 e.g:2014
# quarter:int 季度 :1、2、3、4，只能输入这4个季度
# 结果返回的数据属性说明如下：
# code,代码
# name,名称
# type,业绩变动类型【预增、预亏等】
# report_date,发布日期
# pre_eps,上年同期每股收益
# range,业绩变动范围
stockvalue=ts.forecast_data(2014,2)

# 股票列表
# 获取沪深上市公司基本情况。属性包括：
# code,代码
# name,名称
# industry,所属行业
# area,地区
# pe,市盈率
# outstanding,流通股本(亿)
# totals,总股本(亿)
# totalAssets,总资产(万)
# liquidAssets,流动资产
# fixedAssets,固定资产
# reserved,公积金
# reservedPerShare,每股公积金
# esp,每股收益
# bvps,每股净资
# pb,市净率
# timeToMarket,上市日期
# undp,未分利润
# perundp, 每股未分配
# rev,收入同比(%)
# profit,利润同比(%)
# gpr,毛利率(%)
# npr,净利润率(%)
# holders,股东人数
def getstockbasic():
    stockbasic=ts.get_stock_basics()
    stockbasic.to_excel('d:/pythontest/stock/股票基本信息.xlsx')

################新版接口获取股票基本数据
# 输入参数
## 名称	类型	必选	描述
# is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
# list_status	str	N	上市状态： L上市 D退市 P暂停上市
# exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)
#返回结果
# # 名称	类型	描述
# ts_code	str	TS代码
# symbol	str	股票代码
# name	str	股票名称
# area	str	所在地域
# industry	str	所属行业
# fullname	str	股票全称
# enname	str	英文全称
# market	str	市场类型 （主板/中小板/创业板）
# exchange	str	交易所代码
# curr_type	str	交易货币
# list_status	str	上市状态： L上市 D退市 P暂停上市
# list_date	str	上市日期
# delist_date	str	退市日期
# is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
# data = pro.stock_basic(list_status='L')
# print(data)
###########
# 接口：trade_cal
# 描述：获取各大交易所交易日历数据,默认提取的是上交所
#
# 输入参数
#
# 名称	类型	必选	描述
# exchange	str	N	交易所 SSE上交所 SZSE深交所
# start_date	str	N	开始日期
# end_date	str	N	结束日期
# is_open	str	N	是否交易 '0'休市 '1'交易
# 输出参数
#
# 名称	类型	默认显示	描述
# exchange	str	Y	交易所 SSE上交所 SZSE深交所
# cal_date	str	Y	日历日期
# is_open	str	Y	是否交易 0休市 1交易
# pretrade_date	str	N	上一个交易日
# 接口示例
# pro.trade_cal(exchange='', start_date='20180101', end_date='20181231')