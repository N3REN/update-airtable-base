!pip install pyairtable

from pyairtable import Table
import requests
import re

# replace AIRTABLE_API_KEY with access token
api_key = "patbZGTBTOLdG363Z.933c2984692a078d881a04b21726b5823e48a86b9f5d882fd56708acea2e50d3"

# import table and view records
# replace BASE_ID and TABLE_ID with base ID and table ID
table = Table(api_key, 'app8QwIyfrBK17Fjo', 'tblGgLV5tEeU8hMDB')
table.all()

# get the html content of link in each record
# search for a match using regex patterns
# return the capture group where match exists
# if no match is found, return a placeholder
def doc(url):

  #open with GET method
  get_html = requests.get(url)
    
  #http_respone 200 means OK status
  if get_html.status_code==200:
      text = get_html.text

      pattern = r"Subtitle\:\s*(.+)\s*\\nSEO"
      matches = re.search(pattern, text, re.MULTILINE)

      pattern2 = r"Subtitle\:\s*(.+)\s+[\\\\u000b]*SEO"
      matches2 = re.search(pattern2, text, re.MULTILINE)
			
      pattern3 = r"Subtitle\:\s*(.+)\s\s"
      matches3 = re.search(pattern3, text, re.MULTILINE)

      pattern4 = r"Subtitle\:\s*(.+)\s*\\u000bSEO"
      matches4 = re.search(pattern4, text, re.MULTILINE)

      pattern5 = r"Subtitle\:\s*(.+)\s*\\nWritten"
      matches5 = re.search(pattern5, text, re.MULTILINE)

      pattern6 = r"Subtitle\:\s*(.+)\s*\\u000bWritten"
      matches6 = re.search(pattern6, text, re.MULTILINE)

      pattern7 = r"Subtitle\:\s*(.+)\\n\\n"
      matches7 = re.search(pattern7, text, re.MULTILINE)
    
			
      if matches:
          for groupNum in range(0, len(matches.groups())):
              groupNum = groupNum + 1
              return matches.group(groupNum)

      elif matches2:
          for groupNum in range(0, len(matches2.groups())):
              groupNum = groupNum + 1
              return matches2.group(groupNum)

      elif matches3:
          for groupNum in range(0, len(matches3.groups())):
              groupNum = groupNum + 1
              return matches3.group(groupNum)

      elif matches4:
          for groupNum in range(0, len(matches4.groups())):
              groupNum = groupNum + 1
              return matches4.group(groupNum)

      elif matches5:
          for groupNum in range(0, len(matches5.groups())):
              groupNum = groupNum + 1
              return matches5.group(groupNum)

      elif matches6:
          for groupNum in range(0, len(matches6.groups())):
              groupNum = groupNum + 1
              return matches6.group(groupNum)

      elif matches7:
          for groupNum in range(0, len(matches7.groups())):
              groupNum = groupNum + 1
              return matches7.group(groupNum)			
      else:
          return "<subtitle>"

  else:
      return "No document found"


subtitle_list = []

# add content of match or placeholder to dict and append to a list
for record in table.all():
  doc_url = record['fields']['Story Preview Link']
  subtitle_list.append({'id': record['id'], 'fields': {'Subtitle': doc(doc_url)}})
print(subtitle_list)

# update table in Airtable
table.batch_update(subtitle_list)
