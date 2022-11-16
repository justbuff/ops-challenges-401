#!/usr/bin/env python3

import hashlib

def hash_file(filename):
  h = hashlib.sha256()
  with open(filename, "rb") as file:
    chunk = 0
    while chunk != b"":
      chunk = file.read(1024)
      h.update(chunk)
  return h.hexdigest()

msg = hash_file("test.txt")
print(msg)
