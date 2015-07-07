#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import datetime


def main():
    '''
    This program creates a today's journal with a formated day's date and a
    given title. If that's already done (just now or today), it opens the file
    with a here-given software to be editted.
    '''

    # software for opening the text file
    software = 'vim'

    # number of columns in the opened terminal window
    #columns = int(os.popen('stty size', 'r').read().split()[1])

    # program start
    date = str(datetime.date.today())  # taking today's date
    date = date.replace('-', '')       # passing it to
    listdir = os.listdir()             # taking list of the current's dir

    # checking if there is already a file for today
    if any(date in file_name for file_name in listdir):
        # taking the file name and extracting it's title
        fileName = next(f for f in listdir if date in f)
        title = getTitle(fileName)

        # printing the title centralizedly
        print('Title: \"%s\"\n' % (title))

        # asking for a new title
        newTitle = input('New title or [ENTER]: ')

        # if the user wants a new title, rename the ruling file
        if newTitle != '':
            newFileName = getFileName(date, newTitle)
            os.rename(fileName, newFileName)
            fileName = newFileName

    # if it's the first program running time, ask for a title and create a new
    # document with the due file name; something like this:
    # "YYYYMMDD - Title"
    else:
        title = input('Title: ')
        fileName = getFileName(date, title)
        file = open(fileName, 'w')
        file.close()
    clear()

    # openning today's file with the above-chosen software
    os.system('%s "%s"' % (software, fileName))
    clear()


def getFileName(date, title):
    '''
    Returns a modeled file name for the date and name given
    '''
    title = title.capitalize()  # turning the name into a title

    # if name is not chosen, don't put a separator after the date
    sep = ''
    if title != '':
        sep = ' - '
    return(date + sep + title + '.jr')


def getTitle(fileName):
    '''
    Extracts the title from a given file name
    '''
    li = 11  # len('YYYYMMDD - ')
    lf = -3  # -len('.jr')
    title = fileName[li:lf]
    return(title)


def clear(nl=80):
    print(nl * '\n')


if __name__ == '__main__':
    clear()
    main()
