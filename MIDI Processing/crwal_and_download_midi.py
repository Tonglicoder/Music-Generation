#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:40:04 2018

@author: tong
"""

import requests
from bs4 import BeautifulSoup
import urllib
import re
import urllib.request
import os
import string

def download_midi(music):
    if ("/" in music["track_name"]) or ("/" in music["artist_name"]):
        print ("error")
        print (music["track_name"])
        print (music["artist_name"])
    else:
        music_href = music["url"]
        tmp_list = music_href.split("-")
        url = "https://freemidi.org/"
        download_url = url + "getter-"+ tmp_list[1]
        html_page_url= url + "download-"+ tmp_list[1]
        headers = {'Referer': html_page_url,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        print (download_url)
        directory="newoutput/"+music["artist_name"]
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_name="newoutput/"+music["artist_name"]+"/"+music["artist_name"]+"$$$$$"+music["track_name"]+".midi"
        downloaded_midi = requests.get(download_url, headers=headers, allow_redirects=False)
        with open(file_name, 'wb') as ex:
            ex.write(downloaded_midi.content)
    return



def crawl_download_url(index):
    url = "https://freemidi.org/"
    crawl_url="https://freemidi.org/artists-"+index
    
    #use BeautifulSoup to crawl on the url:https://freemidi.org/artists-a(b/c/../z)
    result = requests.get(crawl_url)    
    c = result.content    
    soup = BeautifulSoup(c)    
    
    #find all the "div" in the class:genre-link-text, put these links in the list named samples
    samples = soup.find_all("div",class_="genre-link-text")   
    print (len(samples))
    #
    #extract detail information from samples list and put in the list named href_list       
    href_list = []    
    for s in samples:
        a = s.a
        href_list.append(a["href"])    
    print (len(href_list))    
    


    #iterate over href_list(this is the list of all artists in the upper level webpage)    
    for href in href_list:
        artist_name = re.findall(r"^artist-\d+-(.+?)$",href)
        print (artist_name)
        
        #use BeautifulSoup to crawl all the songs of a specific artist and invoke download_midi to download this song
        result = requests.get(url+href)
        c = result.content
        soup = BeautifulSoup(c)        
        for div in soup.find_all("div",class_="artist-song-cell"):
            music = {"url":div.find("a", {"itemprop": "url"})["href"],"track_name":div.find("a", {"itemprop": "url"}).text.strip().replace(" ","_"), "artist_name":artist_name[0]}        
            try:
                download_midi(music)   
            except:
                print ("error in download")
                print (music["track_name"])
                print (music["artist_name"])
    return 



#Generate a list, from a to z
alphabet=string.ascii_lowercase[:26]

#Iterate over the a-z list, invoke the crawl function 
for letter in alphabet:
    index=letter
    crawl_download_url(index)
