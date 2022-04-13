# Flowshutter
# Copyright (C) 2021  Hugo Chiang

# Flowshutter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Flowshutter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with flowshutter.  If not, see <https://www.gnu.org/licenses/>.
import hashlib, json, os, sys

sha1 = hashlib.sha1()
files = os.listdir("src/")

try:
    files.remove("sha.json")
except ValueError:
    pass

# print(files)
jtext = {"files":[]}

for f in files:
    with open("src/"+f,"rb") as hf:
        for byte_block in iter(lambda: hf.read(4096),b""):
            sha1.update(byte_block)
        # print(f,sha1.hexdigest()) # for debug
        jtext["files"].append({"name":f,"sha1":sha1.hexdigest()})

jdata = json.dumps(jtext,indent = 4, separators=(',', ': '))

jdir = ""
# print(len(sys.argv)) # for debug
if len(sys.argv) > 1:
    if sys.argv[1] == "check":
        jdir = "check_sha.json"
else:
    jdir = "src/sha.json"
    
print("SHA1 of all files generated!")
jfile = open(jdir,"w")
jfile.write(jdata)
jfile.close()
print("Update sha.json success!")
