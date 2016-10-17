import tushare as ts 
import pandas as pd
import os

def save_all_stocks_info():
	"""
	It saves the list of stocks and related information. The output as following:
	        code    name c_name
	0     600051    xxxx   xxxx
	"""
	dir_path = os.getcwd()  
	file_path = dir_path +  '/../data/stock_industry_map.csv'

	df = ts.get_industry_classified()
	df.to_csv(file_path, encoding='utf-8')

	return df


def save_all_stocks_transaction_history():
	
	dir_path = os.getcwd()
	stock_info_path = dir_path + '/../data/stock_industry_map.csv'


	if os.path.exists(stock_info_path): 
		# if exists, directly read from the file, otherwise re-read from the tushare server
		df = pd.read_csv(stock_info_path, dtype=str)
	else:
		df = save_all_stocks_info()    

	print "successfully fetched all the stock info!"

	codes = df['code']	 # get the list of stock codes
	for c in codes:	
		print c
		# get all the transation history for each stock, and save it! 
		df_c = ts.get_hist_data(c) 
		file_path = dir_path + '/../data/stocks/' + str(c) + '.csv'
		df_c.to_csv(file_path)
		print "successfully get the transaction history for stock: " + str(c)


if __name__ == '__main__':
	#save_all_stocks_info()
	save_all_stocks_transaction_history()









