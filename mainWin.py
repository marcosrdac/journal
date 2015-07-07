#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import os


def main():
    columns = 80 #int(os.popen('stty size', 'r').read().split()[1])
    date = str(datetime.date.today())
    date = date.replace('-', '')
    listdir = os.listdir()
    if any(date in f for f in listdir):
        fileName = next(f for f in listdir if date in f)
        title = getTitle(fileName)
        print('Title:'.center(columns))
        print(title.center(columns))
        rename = input('Retitle (Y / [ENTER]): ')
        if any(rename == y for y in ['y', 'Y']):
            clear(5)
            newFileName = getFileName(date)
            os.rename(fileName, newFileName)
            fileName = newFileName
    else:
        fileName = getFileName(date)
        file = open(fileName, 'w')
        file.close()
    clear()
    cmd = 'notepad "%s"' % (fileName)
    os.system(cmd)
    clear()


def getFileName(date):
    name = input('Title: ')
    name = name.capitalize()
    if name == '':
        sep = ''
    else:
        sep = ' - '
    return(date + sep + name + '.jr')


def getTitle(fileName):
    li = len('YYYYMMDD - ')
    lf = -len('.jr')
    title = fileName[li:lf]
    return(title)


def clear(nl=80):
    print(nl * '\n')


if __name__ == '__main__':
    clear()
    main()
