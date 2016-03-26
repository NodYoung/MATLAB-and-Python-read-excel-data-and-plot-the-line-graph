import xlrd
import numpy as np
import pylab as pl

realdatafname = 'realpoint.xlsx'
trackingdatafname = 'trackingpoint.xlsx'
realdatabk = xlrd.open_workbook(realdatafname)  # 获取xls文件
trackingdatabk = xlrd.open_workbook(trackingdatafname)  # 获取xls文件
realdatash = realdatabk.sheet_by_name('Sheet1')  #通过名称获取bk中的sheet
trackingdatash = trackingdatabk.sheet_by_name('Sheet1')  #通过名称获取bk中的sheet

# nrows = realdatash.nrows  # 获取行数
# ncols = realdatash.ncols  # 获取列数
# print('nrows %d, ncols %d' % (nrows,ncols))
# cell_value = realdatash.cell_value(1, 1)  # 获取单元格（1，1）的值
# print(cell_value)

realdatax = np.array(realdatash.col_values(0))  # 获取第0列值的列表,并将其转换为array类型
realdatay = np.array(realdatash.col_values(1))
trackingdatax = np.array(trackingdatash.col_values(0))  # 获取第0列值的列表,并将其转换为array类型
trackingdatay = np.array(trackingdatash.col_values(1))
# print(realdatax)
errorx = np.absolute(trackingdatax - realdatax)
errory = np.absolute(trackingdatay - realdatay)
errordistant = np.sqrt(errorx * errorx + errory * errory)
pl.figure(1)
pl.xlabel('frames')
pl.ylabel('xerror(pixel)')
pl.title('The error of x direction')
pl.plot(errorx)  # use pylab to plot x and y
pl.figure(2)
pl.xlabel('frames')
pl.ylabel('yerror(pixel)')
pl.title('The error of y direction')
pl.plot(errory)  # use pylab to plot x and y
pl.figure(3)
pl.xlabel('frames')
pl.ylabel('xerror(pixel)')
pl.title('The error of x direction')
pl.plot(errordistant)  # use pylab to plot x and y
pl.show()   # show the plot on the screen
