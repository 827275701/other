# -*- coding: utf-8 -*-

import xlrd, xlwt, xlutils

def read_excel(filename):
    '''
    ��ȡexcel�ļ�����
    :param filename:  ��Ҫ�򿪵��ļ�����
    :return:  �޷��� ֻ��ӡ
    '''
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name('Sheet1')
    rows = sheet.nrows
    # cols = sheet.ncols
    # for c in range(cols):
    #     c_values = sheet.col_values(c)
    #     print c_values
    for r in range(rows):
        r_values = sheet.row_values(r)
        print r_values

    # print (sheet.cell(1, 1))  #ָ��λ�ô�ӡ

def write_excel(filename, data):
    '''
    ��dataд��Excel�ļ�
    :param filename:  �ļ���
    :param data: ����һ���б��б��е�Ԫ��Ҳ��һ���б�ÿ��Ԫ�ش���һ��
    :return:�޷���
    '''
    book = xlwt.Workbook(encoding='utf-8')  #����һ������
    sheet = book.add_sheet('Sheet1')  #������������һ��sheet
    c = 0   #�ӵ�һ�п�ʼ
    for d in data:   #�����б�
        for index in range(len(d)):
            # �����б��ÿһ��Ԫ��д���ļ�
            sheet.write(c, index, d[index])  #sheet.write���ڼ��У� �ڼ��У� д������ݣ�
        c += 1 #��һ��
    book.save(filename) #���������һ���Դ浽�ļ������IO����



def main():
    data = []
    with open('title.txt', 'r') as f:

        for line in f:
            tem_list = line.split(' ', 2)
            data.append(tem_list)

    write_excel('aaa.xlsx', data)
    read_excel('aaa.xlsx')

if __name__ == '__main__':
    main()