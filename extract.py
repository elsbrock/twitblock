#!/usr/bin/env python

import re
import argparse

import PyPDF2

def run():
    parser = argparse.ArgumentParser(description='Extracts usernames from the Twitter '
                                     + 'advertister list.')
    parser.add_argument('inputfile', type=str, help='Advertister List PDF',
                        default='twitter_advertiser_list.pdf')
    args = parser.parse_args()

    with open(args.inputfile, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()

        for pages in range(num_pages):
            user_page = pdf_reader.getPage(pages).extractText()
            for username in re.findall(r'(@[^@]+)', user_page):
                print(username)

if __name__ == '__main__':
    run()
