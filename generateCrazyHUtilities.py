# [
# 
# Script made by CrazyH2 (https://github.com/crazyh2)
# © Copyright 2024 CrazyH2. All rights reserved.
# 
# ]

import os, shutil, hashlib

def generate_file_md5(rootdir, filename, blocksize=2**20):
    m = hashlib.md5()
    with open( os.path.join(rootdir, filename) , "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

def main():
    shutil.make_archive("zipped.zip", 'zip', f"""{pathlib.Path(__file__).parent.resolve()}//main""")

    print("Hash:", generate_file_md5(pathlib.Path(__file__).parent.resolve(), "main"))

if __name__ == "__main__":
    main()
