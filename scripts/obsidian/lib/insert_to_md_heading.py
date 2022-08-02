import re, sys, os, unicodedata

def insert_to_heading(original_text, heading, insertion):
  
  find = re.compile(r'(?<=' + heading + r'\n)((\n.*?)+)(?=#+ |$)', flags = re.MULTILINE|re.DOTALL)
  found = re.findall(find, original_text)

  replace = f'\\1{insertion}'

  if re.findall(find, original_text) == []:
    new_content = original_text + heading + '\n\n' + insertion
  else:
    new_content = re.sub(find, replace, original_text)

  # print(unicodedata.normalize("NFC",new_content))
  return unicodedata.normalize("NFC",new_content)