# -*- coding: utf-8 -*- 
import os
import xdrlib,sys
import xlrd
import string,re
import test2


#reload(sys)
#sys.setdefaultencoding('utf8')

dot = '.'

#data = {}

def open_excel(file= '123.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
'''
def excel_table_byindex(file= '123.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list
'''
#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= '1.xls',colnameindex=0,by_name= 'Tablib Dataset'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    #usr_num = 0
    ent_num = 0
    tck_num = 0
    hhd_num = 0
    wik_num = 0
    sys_num = 0


    #print nrows
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(0,nrows-1):
        row = table.row_values(rownum)
        data = [[0 for x in range(4)]for x in range(nrows)]
        if row:
            operation = table.cell_value(rownum,1)
         	#print operation
            operation = operation.split(dot)
            #print operation[2]
            if operation[0] == "app" or "system":
                data[rownum][0]=operation[1]
                if data[rownum][0] == "music":
                    ent_num = ent_num+1
                    data[rownum][3] = "ent"
                if data[rownum][0] == "weather":
                    tck_num = tck_num+1
                    data[rownum][3] = "tck"
                if data[rownum][0] == "wiki":
                    wik_num = wik_num+1
                    data[rownum][3] = "wik"
                if data[rownum][0] == "chat":
                    sys_num = sys_num+1
                    data[rownum][3] = "sys"

            else:

                if operation[2] == "system":
                    data[rownum][0]=operation[3]
                    if data[rownum][0] == "command":
                        sys_num = sys_num+1
                        data[rownum][3] = "sys" 
                    if data[rownum][0] == "upgrade":
                        sys_num = sys_num+1
                        data[rownum][3] = "sys" 
                    if data[rownum][0] == "volume":
                        sys_num = sys_num+1
                        data[rownum][3] = "sys" 
                    if data[rownum][0] == "light":
                        hhd_num = hhd_num+1
                        data[rownum][3] = "hhd"
                        print 1 
                    if data[rownum][0] == "lightapp":
                        hhd_num = hhd_num+1
                        data[rownum][3] = "hhd"
                        print 1
                    if data[rownum][0] == "smarthome":
                        hhd_num = hhd_num+1
                        data[rownum][3] = "hhd" 
                        print 1
                    if data[rownum][0] == "functionguide":
                        sys_num = sys_num+1
                        data[rownum][3] = "sys"
                    if data[rownum][0] == "chat":
                        sys_num = sys_num+1
                        data[rownum][3] = "sys"

                else:
                    data[rownum][0]=operation[2]
                    if data[rownum][0] == "music1":
                        ent_num = ent_num+1
                        data[rownum][3] = "ent"
                    if data[rownum][0] == "flappybird":
                        ent_num = ent_num+1
                        data[rownum][3] = "ent"
                    if data[rownum][0] == "radio1":
                        ent_num = ent_num+1
                        data[rownum][3] = "ent"
                    if data[rownum][0] == "childstory":
                        ent_num = ent_num+1
                        data[rownum][3] = "ent"
                    if data[rownum][0] == "time1":
                        tck_num = tck_num+1
                        data[rownum][3] = "tck"
                    if data[rownum][0] == "weather1":
                        tck_num = tck_num+1
                        data[rownum][3] = "tck"
                    if data[rownum][0] == "alarm1":
                        tck_num = tck_num+1
                        data[rownum][3] = "tck"
                    if data[rownum][0] == "wikiqa":
                        wik_num = wik_num+1
                        data[rownum][3] = "wik"
                    if data[rownum][0] == "calendar1":
                        tck_num = tck_num +1
                        data[rownum][3] = "tck"

            #print data[rownum][0],data[rownum][3]
      




            time = table.cell_value(rownum,3)
            data[rownum][1]=time
            usr_id_temp = table.cell_value(rownum,4)
            data[rownum][2]=usr_id_temp



    return data,wik_num,tck_num,ent_num,sys_num,hhd_num,nrows

def get_users(data,nrows):
    length = len(usr_id)
    users_wed,usr_tue,usr_mon = [[0 for x in range(6)]for x in range(length)]
    for i in range(0,length-1):
        users_wed[i][0] = usr_id[i]
        users_tue[i][0] = usr_id[i]
        users_mon[i][0] = usr_id[i]


    for j in range(0,12234):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_wed[i][1]=users_wed[i][1]+1
                if data[j][3]=="tck":
                    users_wed[i][2]=users_wed[i][2]+1
                if data[j][3]=="hhd":
                    users_wed[i][3]=users_wed[i][3]+1
                if data[j][3]=="wik":
                    users_wed[i][4]=users_wed[i][4]+1
                if data[j][3]=="sys":
                    users_wed[i][5]=users_wed[i][5]+1
    for j in range(12235,27163):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_tue[i][1]=users_tue[i][1]+1
                if data[j][3]=="tck":
                    users_tue[i][2]=users_tue[i][2]+1
                if data[j][3]=="hhd":
                    users_tue[i][3]=users_tue[i][3]+1
                if data[j][3]=="wik":
                    users_tue[i][4]=users_tue[i][4]+1
                if data[j][3]=="sys":
                    users_tue[i][5]=users_tue[i][5]+1
    for j in range(27164,36296):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_mon[i][1]=users_mon[i][1]+1
                if data[j][3]=="tck":
                    users_mon[i][2]=users_mon[i][2]+1
                if data[j][3]=="hhd":
                    users_mon[i][3]=users_mon[i][3]+1
                if data[j][3]=="wik":
                    users_mon[i][4]=users_mon[i][4]+1
                if data[j][3]=="sys":
                    users_mon[i][5]=users_mon[i][5]+1

    return users



    




def main():
    (tables,wik_num,tck_num,ent_num,sys_num,hhd_num,nrows)=excel_table_byname()



    '''
    for row in tables:
		print row
    '''

if __name__=="__main__":
    main()