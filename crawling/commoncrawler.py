import requests
from warcio.archiveiterator import ArchiveIterator
import ast
import json
import io
from bs4 import BeautifulSoup
import sqlalchemy
from sqlalchemy import text
import os
import regex as re

# Example URL you want to search for


def common_crawler_url_search(url):
    # Send a GET request to the Common Crawl Index API
    index_url = f"http://index.commoncrawl.org/collinfo.json"
    response = requests.get(index_url)
    indexes = response.json()

    # Get the latest index (usually the last entry in the list)
    latest_index = indexes[0]["id"]

    # Use the latest index to search for the URL

    search_url = f"http://index.commoncrawl.org/{latest_index}-index?url={url}&output=json"
    search_response = requests.get(search_url)
    results = search_response.text
    results_list=results.split(",")
    data_dict={}
    for entry in results_list:
        try:
            entry=entry.replace("\"","").strip()
            key,value=entry.split(":")
            data_dict[key]=value
        except: 
            None
    #dictionary = json.loads(results)


    warc_filename = data_dict["filename"].strip()
    offset = int(data_dict["offset"].strip())
    length = int(data_dict["length"].strip())


    response = requests.get(f'https://data.commoncrawl.org/{warc_filename}',
                            headers={'Range': f'bytes={offset}-{offset + length - 1}'})
    return response

response=common_crawler_url_search("kiel.de")

def sanitize_input(string):
    new_string=re.sub("[!}{&#$%;']","",string)
    return new_string

def insert_response_to_sql_db(response):
    os.chdir(r"E:\stadt_interface")
    engine = sqlalchemy.create_engine('sqlite:///commoncrawler.db')
    connection=engine.connect()
    connection.execute(text("DROP TABLE html_table"))
    connection.execute(text("CREATE TABLE IF NOT EXISTS html_table (html TEXT) "))

    with io.BytesIO(response.content) as stream:
        for record in ArchiveIterator(stream):
            html = record.content_stream().read()
            pretty_html=BeautifulSoup(html, 'html.parser').prettify()
            #pretty_html=pretty_html.replace("DOCTYPE","")
            pretty_html=sanitize_input(pretty_html)
            pretty_html=str(pretty_html)
            connection.execute(text(f"INSERT INTO html_table (html) VALUES ('{pretty_html}');"))
    #connection.commit()
    connection.close()


insert_response_to_sql_db(response)


