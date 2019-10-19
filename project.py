from flask import Flask, render_template, jsonify, request
import urllib.request
from bs4 import BeautifulSoup


url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EC%97%AC%ED%96%89'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_="sh_blog_title")

print(title)