#!/usr/bin/env python3

# Required parameters: text
# @raycast.schemaVersion 1
# @raycast.title Obsidian Capture Idea
# @raycast.mode silent

# Optional parameters:
# @raycast.packageName obsidian-capture-idea
# @raycast.icon ./assets/obsidian.png
# @raycast.argument1 { "type": "text", "placeholder": "entry" }

# Documentation:
# @raycast.author chaosarium
# @raycast.authorURL https://github.com/chaosarium

import sys, os, datetime
query = sys.argv[1]

# set vault path
OBSIDIAN_VAULT_PATH = "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Zettelkasten"
# file to manipulate within vault
FILE_PATH = "000 System/080 Inboxes/Ideas Inbox.md"
# format appended text
insertion = f"""

%%captured {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}%%
{query}

---"""

abs_path = os.path.expanduser(os.path.join(OBSIDIAN_VAULT_PATH, FILE_PATH))

try: 
  file = open(abs_path, "a")
  file.write(insertion)
  file.close()
  print('success')
  sys.exit(0)
except Exception as e:
  print(e)
  sys.exit(1)