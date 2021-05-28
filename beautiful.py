import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import ssl
from datetime import datetime
import argparse
from tkinter import *


def check_tag1(naver_ID):
    context = ssl._create_unverified_context()
    # CHECK TAG 1
    # check how many pages
    new_url = f'https://blog.naver.com/PostListByTagName.nhn?blogId={naver_ID}&logType=0&cpage=1&tagName=%EC%98%A4%EB%8A%98%EC%9D%BC%EA%B8%B0'
    html = urllib.request.urlopen(new_url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(class_='paging')
    str_pages = str(pages)
    page_num = str_pages.count('goPage')
    p_tag = soup.find_all('p', class_='tit')
    tag1_list = []
    for title in p_tag:
        tag1_list.append([title.a['href'], title.input['value']])
    for i in range(2, page_num+1):
        new_url = f'https://blog.naver.com/PostListByTagName.nhn?blogId={naver_ID}&logType=0&cpage={i}&tagName=%EC%98%A4%EB%8A%98%EC%9D%BC%EA%B8%B0'
        html = urllib.request.urlopen(new_url, context=context).read()
        soup = BeautifulSoup(html, 'html.parser')
        new_p_tag = soup.find_all('p', class_='tit')
        for title in new_p_tag:
            tag1_list.append([title.a['href'], title.input['value']])
    return tag1_list


def check_tag2(naver_ID):
    context = ssl._create_unverified_context()
    # CHECK TAG 2
    # check how many pages
    new_url = f'https://blog.naver.com/PostListByTagName.nhn?blogId={naver_ID}&logType=0&cpage=1&tagName=%EB%B8%94%EC%B1%8C'
    html = urllib.request.urlopen(new_url, context=context).read()
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(class_='paging')
    str_pages = str(pages)
    page_num = str_pages.count('goPage')
    p_tag = soup.find_all('p', class_='tit')
    tag2_list = []
    for title in p_tag:
        tag2_list.append([title.a['href'], title.input['value']])
    for i in range(2, page_num+1):
        new_url = f'https://blog.naver.com/PostListByTagName.nhn?blogId={naver_ID}&logType=0&cpage={i}&tagName=%EB%B8%94%EC%B1%8C'
        html = urllib.request.urlopen(new_url, context=context).read()
        soup = BeautifulSoup(html, 'html.parser')
        new_p_tag = soup.find_all('p', class_='tit')
        for title in new_p_tag:
            tag2_list.append([title.a['href'], title.input['value']])
    return tag2_list


def main(naver_ID):
    list1 = check_tag1(naver_ID)
    list2 = check_tag2(naver_ID)
    success = []
    for i in list1:
        if i in list2:
            success.append(i)

    dates = ['May 24', 'May 25', 'May 26', 'May 27', 'May 28', 'May 29', 'May 30', 'May 31', 'Jun 01', 'Jun 02', 'Jun 03']

    today = datetime.today().strftime("%m%d")
    today = str(today)
    if today[:2] == '05':
        today = 'May '+today[-2:]
    elif today[:2] == '06':
        today = 'Jun '+today[-2:]

    print()
    print()
    print('============================')
    print(f" {naver_ID}'s Blog Challenge")
    print('----------------------------')
    for date in dates:
        done = 'Not Yet'
        for ele in success:
            if date in ele[1]:
                done = 'Done'
                break
            else:
                pass
        if date == today:
            print(date, done, '<---- Today')
        else:
            print(date, done)
    print('============================')
    print()
    print()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Blog Challenge Checker')
    # parser.add_argument('--naver_ID', type=str, default='cori95')
    #
    # args = parser.parse_args()
    # naver_ID = args.naver_ID

    # test = Tk()
    # test.title('Naver Blog Challenge Checker')
    # test.geometry('300x500+100+100')
    # test.resizable(False, False)
    #
    # label = Label(test, text='Insert your Naver ID')
    # label.pack()
    #
    # textExample = Text(test, height=1, width=10)
    # textExample.pack()
    # btnRead = Button(test, height=1, width=10, text="check", command=getTextInput)
    # btnRead.pack()

    while True:
        naver_ID = input('Insert Your Naver ID : ')
        main(naver_ID)

    # test.mainloop()