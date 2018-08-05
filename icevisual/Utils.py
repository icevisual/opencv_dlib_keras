import hashlib
import os
import time
import socket
import random
import hmac
import base64
import re
import sys
from hashlib import sha1
from datetime import datetime
from subprocess import Popen, PIPE


class Utils:

    @staticmethod
    def random_str(length = 8):
        collection = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        result_string = ""
        for x in range(length):
            result_string += collection[random.randint(0,len(collection) - 1)]
        return result_string

    @staticmethod
    def get_ip_address_sk():
        return socket.gethostbyname(socket.gethostname())
        # ret = Popen('ipconfig', stdout=PIPE).stdout.read()
        # print(str(ret,encoding="GBK"))
        # return re.search(r'\d+\.\d+\.\d+\.\d+', str(ret, encoding="GBK")).group(0)

    @staticmethod
    def get_ip_address():
        ret = Popen('ipconfig', stdout=PIPE).stdout.read()
        print(str(ret,encoding="GBK"))
        return re.search(r'\d+\.\d+\.\d+\.\d+', str(ret, encoding="GBK")).group(0)

    @staticmethod
    def int2_bytes_list(int_val, target_len=4):
        res_list = [] * target_len
        for i in range(target_len):
            res_list.append((int_val >> (8 * (target_len - 1 - i))) & 0xff)
        return res_list

    @staticmethod
    def bytes_list_2_int(bytes_list, bytes_length=4):
        res_int_val = 0
        for i in range(bytes_length):
            res_int_val |= (bytes_list[i] << (8 * (bytes_length - 1 - i)))
        return res_int_val

    @staticmethod
    def bytes_list_2_hex_str(bytes_list):
        return ''.join(format(x, "02x") for x in bytes_list)

    @staticmethod
    def calculate_md5(bytes_array, format="str"):
        hl = hashlib.md5()
        hl.update(bytes_array)
        md5_value = hl.hexdigest()
        if format == "str":
            return md5_value
        elif format == "bytes":
            return bytes.fromhex(md5_value)
        elif format == "byteslist":
            return list(bytes.fromhex(md5_value))
        return md5_value

    @staticmethod
    def hmacsha1(msg, secret):
        my_sign = hmac.new(secret, msg, sha1).digest()
        my_sign = base64.b64encode(my_sign)
        return my_sign

    @staticmethod
    def load_key_value_config_file(config_file):
        kv_map = {}
        if os.path.exists(config_file):
            config_list = []
            with open(config_file, "r") as fp:
                config_list = fp.readlines()
            if len(config_list) > 0:
                re.compile(r"/[\s\=]/")
                for str in config_list:
                    line = str.strip().lower()
                    if len(line) > 0:
                        line_kv = re.split(r"[\s=]+", line)
                        kv_map[line_kv[0]] = line_kv[1]
        return kv_map

    @staticmethod
    def get_file_md5(filename):
        if not os.path.isfile(filename):
            return
        my_hash = hashlib.md5()
        f = open(filename, 'rb')
        while True:
            b = f.read(8096)
            if not b:
                break
            my_hash.update(b)
        f.close()
        return my_hash.hexdigest()

    @staticmethod
    def timestamp_2_time(timestamp):
        time_struct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)

    @staticmethod
    def format_time_with_millisecond(format_str="%Y-%m-%d %H:%M:%S.fff"):
        t = time.time()
        segms = str(t).split('.')
        ms = '{0:0<10}'.format(segms[1])
        ms = ms[:3]
        tp = int(segms[0])
        localTime = time.localtime(tp)
        strTime = time.strftime(format_str, localTime)
        return strTime.replace('fff', ms)

    @staticmethod
    def filename_width_ms(format_str="%Y-%m-%d-%H-%M-%S-fff"):
        return Utils.format_time_with_millisecond(format_str)

    @staticmethod
    def timestamp_string():
        return str(time.time()).replace('.', '')


class Marker(object):

    mark_tag_dict = {}

    def mark(self, tag):
        self.mark_tag_dict[tag] = time.time()

    def distance(self, tag1, tag2):
        if tag1 in self.mark_tag_dict and tag2 in self.mark_tag_dict:
            print("[%s ~ %s][dis]: %f" % (tag1, tag2, self.mark_tag_dict[tag2] - self.mark_tag_dict[tag1]))
        else:
            print("Tag Not Found")



if __name__ == "__main__":

    print(Utils.format_time_with_millisecond())
    print(Utils.filename_width_ms())
    sys.exit(0)
    print(datetime.now())
    print(Utils.hmacsha1(bytes("GID_CABINET_HANGZHOU", encoding="utf-8"), bytes("AomDHWs4NFvDWezetTpv6dwgSCuTdC", encoding="utf-8")))
    print(Utils.random_str(123))
    print(Utils.int2_bytes_list(9622))
    print(Utils.bytes_list_2_int([0, 0, 0, 10]))
    print(Utils.get_file_md5("..//a.bin"))
    print(Utils.get_ip_address_sk())
    t1 = b""
    print(len(t1))
