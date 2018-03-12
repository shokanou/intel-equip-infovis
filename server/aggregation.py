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
def excel_table_byname(file= '2.xls',colnameindex=0,by_name= 'Tablib Dataset'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    #usr_num = 0
    ent_num = 0
    tck_num = 0
    hhd_num = 0
    wik_num = 0
    sys_num = 0
    dtk_num = 0


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
                    if data[rownum][0] == "idontknow":
                        dtk_num = dtk_num+1
                        data[rownum][3] = "dtk"

            #print data[rownum][0],data[rownum][3]
      




            time = table.cell_value(rownum,3)
            data[rownum][1]=time
            usr_id_temp = table.cell_value(rownum,4)
            data[rownum][2]=usr_id_temp



    return data,wik_num,tck_num,ent_num,sys_num,hhd_num,dtk_num,nrows

def get_users(data,nrows):
    length = len(usr_id)
    users_tue,users_mon,users_sun,users_sat,users_fri,users_thu = [[0 for x in range(8)]for x in range(length)]
    for i in range(0,length-1):
        users_tue[i][0] = usr_id[i]
        users_mon[i][0] = usr_id[i]
        users_sun[i][0] = usr_id[i]
        users_sat[i][0] = usr_id[i]
        users_fri[i][0] = usr_id[i]
        users_thu[i][0] = usr_id[i]


    for j in range(0,4731):
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
                if data[j][3]=="dtk":
                    users_tue[i][6]=users_tue[i][6]+1
            users_tue[i][7]=users_tue[i][1]+users_tue[i][2]+users_tue[i][3]+users_tue[i][4]+users_tue[i][5]+users_tue[i][6]

    for j in range(4732,15157):
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
                if data[j][3]=="dtk":
                    users_mon[i][6]=users_mon[i][6]+1
            users_mon[i][7]=users_mon[i][1]+users_mon[i][2]+users_mon[i][3]+users_mon[i][4]+users_mon[i][5]+users_mon[i][6]

    for j in range(15158,28896):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_sun[i][1]=users_sun[i][1]+1
                if data[j][3]=="tck":
                    users_sun[i][2]=users_sun[i][2]+1
                if data[j][3]=="hhd":
                    users_sun[i][3]=users_sun[i][3]+1
                if data[j][3]=="wik":
                    users_sun[i][4]=users_sun[i][4]+1
                if data[j][3]=="sys":
                    users_sun[i][5]=users_sun[i][5]+1
                if data[j][3]=="dtk":
                    users_sun[i][6]=users_sun[i][6]+1
            users_sun[i][7]=users_sun[i][1]+users_sun[i][2]+users_sun[i][3]+users_sun[i][4]+users_sun[i][5]+users_sun[i][6]

    for j in range(28897,43865):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_sat[i][1]=users_sat[i][1]+1
                if data[j][3]=="tck":
                    users_sat[i][2]=users_sat[i][2]+1
                if data[j][3]=="hhd":
                    users_sat[i][3]=users_sat[i][3]+1
                if data[j][3]=="wik":
                    users_sat[i][4]=users_sat[i][4]+1
                if data[j][3]=="sys":
                    users_sat[i][5]=users_sat[i][5]+1
                if data[j][3]=="dtk":
                    users_sat[i][6]=users_sat[i][6]+1
            users_sat[i][7]=users_sat[i][1]+users_sat[i][2]+users_sat[i][3]+users_sat[i][4]+users_sat[i][5]+users_sat[i][6]

    for j in range(43866,52949):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_fri[i][1]=users_fri[i][1]+1
                if data[j][3]=="tck":
                    users_fri[i][2]=users_fri[i][2]+1
                if data[j][3]=="hhd":
                    users_fri[i][3]=users_fri[i][3]+1
                if data[j][3]=="wik":
                    users_fri[i][4]=users_fri[i][4]+1
                if data[j][3]=="sys":
                    users_fri[i][5]=users_fri[i][5]+1
                if data[j][3]=="dtk":
                    users_fri[i][6]=users_fri[i][6]+1
            users_fri[i][7]=users_fri[i][1]+users_fri[i][2]+users_fri[i][3]+users_fri[i][4]+users_fri[i][5]+users_fri[i][6]

    for j in range(52950,63610):
        for i in range(0,length-1):
            if users[i][0]==data[j][2]:
                if data[j][3]=="ent":
                    users_thu[i][1]=users_thu[i][1]+1
                if data[j][3]=="tck":
                    users_thu[i][2]=users_thu[i][2]+1
                if data[j][3]=="hhd":
                    users_thu[i][3]=users_thu[i][3]+1
                if data[j][3]=="wik":
                    users_thu[i][4]=users_thu[i][4]+1
                if data[j][3]=="sys":
                    users_thu[i][5]=users_thu[i][5]+1
                if data[j][3]=="dtk":
                    users_thu[i][6]=users_thu[i][6]+1

            users_thu[i][7]=users_thu[i][1]+users_thu[i][2]+users_thu[i][3]+users_thu[i][4]+users_thu[i][5]+users_thu[i][6]

    cat_tue,cat_mon,cat_sun,cat_sat,cat_fri,cat_thu=[[0 for x in range(7)]for x in range(length)]
    var = 0
    for k in range(0,len(users_tue)-1):
        if users_tue[k][7]!=0 :
            cat_tue[var][0]=users_tue[k][0]
            cat_tue[var][1]=users_tue[k][1]/users_tue[k][7]
            cat_tue[var][2]=users_tue[k][2]/users_tue[k][7]
            cat_tue[var][3]=users_tue[k][3]/users_tue[k][7]
            cat_tue[var][4]=users_tue[k][4]/users_tue[k][7]
            cat_tue[var][5]=users_tue[k][5]/users_tue[k][7]
            cat_tue[var][6]=users_tue[k][6]/users_tue[k][7]
            var = var+1

    var = 0
    for k in range(0,len(users_mon)-1):
        if users_mon[k][7]!=0 :
            cat_mon[var][0]=users_mon[k][0]
            cat_mon[var][1]=users_mon[k][1]/users_mon[k][7]
            cat_mon[var][2]=users_mon[k][2]/users_mon[k][7]
            cat_mon[var][3]=users_mon[k][3]/users_mon[k][7]
            cat_mon[var][4]=users_mon[k][4]/users_mon[k][7]
            cat_mon[var][5]=users_mon[k][5]/users_mon[k][7]
            cat_mon[var][6]=users_mon[k][6]/users_mon[k][7]
            var = var+1

    var = 0
    for k in range(0,len(users_sun)-1):
        if users_sun[k][7]!=0 :
            cat_sun[var][0]=users_sun[k][0]
            cat_sun[var][1]=users_sun[k][1]/users_sun[k][7]
            cat_sun[var][2]=users_sun[k][2]/users_sun[k][7]
            cat_sun[var][3]=users_sun[k][3]/users_sun[k][7]
            cat_sun[var][4]=users_sun[k][4]/users_sun[k][7]
            cat_sun[var][5]=users_sun[k][5]/users_sun[k][7]
            cat_sun[var][6]=users_sun[k][6]/users_sun[k][7]
            var = var+1

    var = 0
    for k in range(0,len(users_sat)-1):
        if users_sat[k][7]!=0 :
            cat_sat[var][0]=users_sat[k][0]
            cat_sat[var][1]=users_sat[k][1]/users_sat[k][7]
            cat_sat[var][2]=users_sat[k][2]/users_sat[k][7]
            cat_sat[var][3]=users_sat[k][3]/users_sat[k][7]
            cat_sat[var][4]=users_sat[k][4]/users_sat[k][7]
            cat_sat[var][5]=users_sat[k][5]/users_sat[k][7]
            cat_sat[var][6]=users_sat[k][6]/users_sat[k][7]
            var = var+1

    var = 0
    for k in range(0,len(users_fri)-1):
        if users_fri[k][7]!=0 :
            cat_fri[var][0]=users_fri[k][0]
            cat_fri[var][1]=users_fri[k][1]/users_fri[k][7]
            cat_fri[var][2]=users_fri[k][2]/users_fri[k][7]
            cat_fri[var][3]=users_fri[k][3]/users_fri[k][7]
            cat_fri[var][4]=users_fri[k][4]/users_fri[k][7]
            cat_fri[var][5]=users_fri[k][5]/users_fri[k][7]
            cat_fri[var][6]=users_fri[k][6]/users_fri[k][7]
            var = var+1

    var = 0
    for k in range(0,len(users_thu)-1):
        if users_thu[k][7]!=0 :
            cat_thu[var][0]=users_thu[k][0]
            cat_thu[var][1]=users_thu[k][1]/users_thu[k][7]
            cat_thu[var][2]=users_thu[k][2]/users_thu[k][7]
            cat_thu[var][3]=users_thu[k][3]/users_thu[k][7]
            cat_thu[var][4]=users_thu[k][4]/users_thu[k][7]
            cat_thu[var][5]=users_thu[k][5]/users_thu[k][7]
            cat_thu[var][6]=users_thu[k][6]/users_thu[k][7]
            var = var+1
            








    #return users_tue,users_mon,users_sun,users_sat,users_fri,users_thu
    return cat_tue,cat_mon,cat_sun,cat_sat,cat_fri,cat_thu


    




def main():
    (tables,wik_num,tck_num,ent_num,sys_num,hhd_num,dtk_num,nrows)=excel_table_byname()
    (cat_tue,cat_mon,cat_sun,cat_sat,cat_fri,cat_thu)=get_users(tables,nrows)


    '''
    for row in tables:
		print row
    '''

if __name__=="__main__":
    main()