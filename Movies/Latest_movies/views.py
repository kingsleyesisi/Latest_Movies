from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Ref: https://github.com/kingsleyesisi/Movie-Scraping

def home(request):        
    return render(request, 'index.html')