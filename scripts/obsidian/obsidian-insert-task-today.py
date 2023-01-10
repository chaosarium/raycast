#!/usr/bin/env python3

# NOTE: dateparser package required!!!

# Required parameters: text
# @raycast.schemaVersion 1
# @raycast.title Obsidian Due Today
# @raycast.mode silent

# Optional parameters:
# @raycast.icon ./assets/obsidian.png
# @raycast.argument1 { "type": "text", "placeholder": "task" }

# Documentation:
# @raycast.author chaosarium
# @raycast.authorURL https://github.com/chaosarium

import sys, os, datetime, dateparser
from lib.insert_to_md_heading import insert_to_heading
query = sys.argv[1]

# set vault path
OBSIDIAN_VAULT_PATH = "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Zettelkasten"
# file to manipulate within vault
FILE_PATH = f"050 Periodic/051 Daily/{datetime.datetime.now().strftime('%Y/%m-%B/%Y-%m-%d')}.md"
# format appended text
heading = '### Inbox'

when = 'today'

parsed_date = dateparser.parse(when, settings={'PREFER_DATES_FROM': 'future', 'PREFER_DAY_OF_MONTH': 'first'})
if parsed_date:
  insertion = f'''- [ ] #t #inbox {query} 📅 {parsed_date.strftime('%Y-%m-%d')}
'''
  
print(insertion)

abs_path = os.path.expanduser(os.path.join(OBSIDIAN_VAULT_PATH, FILE_PATH))

try: 
  file = open(abs_path, "r")
  original_text = file.read() 
  file.close()
  
  processed_text = insert_to_heading(original_text, heading, insertion)
  file = open(abs_path, "w")
  file.write(processed_text)
  file.close()
  
  if when and not parsed_date: 
    print('failed to parse date; due date ignored')
  else: 
    print('success')
  
  sys.exit(0)
except Exception as e:
  print(e)
  sys.exit(1)