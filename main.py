import plistlib
import os
import chardet

for filename in os.listdir("dic-src/"):
    if(filename[0] == "."):
        continue
    print(filename)
    f = open("dic-src/"+filename, "rb").read()
    encoding = chardet.detect(f)["encoding"]
    if encoding == None:
        print("ファイル: {}の文字コードがわかりませんでした。".format(filename))
        exit(1)
    f = f.decode(encoding)
    out = []
    for line in f.split("\n"):
        if len(line) == 0:
            continue
        if line[0] == ";": # 送りがなありはとりあえず無視
            continue
        line = line.split()
        yomi = line[0]
        henkan = "".join(line[1:]).lstrip("/").rstrip("/").split("/")
        for go in henkan:
            go = go.split(";")[0]
            out.append({
                "phrase": go,
                "shortcut": yomi
            })
    plistlib.dump(out, open("dic-dist/"+filename+".plist", "wb"))