#-*- coding: utf-8 -*-
import MySQLdb

class Analysis:
    def __init__(self, fileObj):
        self.info = {}
        self.info['파일명'] = fileObj.filename
        self.raw = ' '.join(map(self.streamToHex, fileObj.stream.read()))
    
    def streamToHex(self, x):
        return str(format(ord(x), '#04x'))[2:]

    # core
    def analysis(self):
        rInfo = self.ransomInfo()
        if rInfo != None:
            dInfo = self.decryptInfo(rInfo)
            self.info['랜섬웨어명'] = rInfo
            if dInfo == None:
                return
        if len(dInfo) > 1:
            i = 1
            for url, env in dInfo.items():
                self.info['복호화 도구 -',i] = url
                self.info['복호화 가능 환경 -',i] = env
                i += 1
        else :
            self.info['복호화 도구'] = list(dInfo.keys())[0]
            self.info['복호화 가능 환경'] = list(dInfo.values())[0]

    # Get Ransomware Name
    def ransomInfo(self):
        db = Database()
        db.cur.execute("select * from signatur3")
        # [0] signature  [1] Ransomware Name [2] Detection Range
        for row in cur.fetchall():
            src, dst = 0, 0
            rng = raw[2].split("-")
            src = int(rng[0])
            dst = int(rng[1])
            if row[0] in self.raw[:]:
                return row[1]
        db.close()
        return None

    def decryptInfo(self, name):
        db = Database()
        db.cur.execute("select * from decrypt3r where name")
        # [0] Ransomware Name [1] Decrypter URL [2] Decryptable OS
        result = cur.fetchall()
        tools = {}
        for row in result:
            tools[row[1]] = row[2]
        return info

    def get(self):
        return self.info


class Database:
    def __init__(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="#g0pher",
            db="rans0mwhere"
        )
        self.cur = self.db.cursor()
    def close():
        self.db.close()
        return
