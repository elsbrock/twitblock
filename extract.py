#!/usr/bin/env python

import re
import PyPDF2
import argparse

parser = argparse.ArgumentParser(description='Extracts usernames from the Twitter advertister list.')
parser.add_argument('inputfile', type=str, help='Advertister List PDF', default='twitter_advertiser_list.pdf')
args = parser.parse_args()
print(args.inputfile)

with open(args.inputfile, 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numberOfPages = pdfReader.getNumPages()

    for pages in range(numberOfPages):
        userPage = pdfReader.getPage(pages).extractText();
        for username in re.findall(r'(@[^@]+)', userPage):
            print(username)