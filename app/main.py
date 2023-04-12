import sys
from dataclasses import dataclass

# import sqlparse - available if you need it!

def handleCmd(dbpath, cmd):
    if cmd == ".dbinfo":
        db_info = {}
        with open(dbpath, "rb") as dbfile:
            dbfile.seek(16)
            db_info["database page size"] = int.from_bytes(dbfile.read(2), byteorder="big")
            
            dbfile.seek(103)
            db_info["number of tables"] = int.from_bytes(dbfile.read(2), byteorder="big")

            for info, val in db_info.items():
                print(f"{info}: {val}")

    else:
        sys.stderr.write(f"Invalid command: {command}\n")


if __name__ == "__main__":
    db_path = sys.argv[1]
    cmd = sys.argv[2]

    handleCmd(db_path, cmd)
