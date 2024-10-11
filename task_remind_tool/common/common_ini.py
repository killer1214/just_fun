import os
from configparser import ConfigParser
from pathlib import Path

class Base():
    def __init__(self):
        self.now_path = os.getcwd()
        self.ini = Path(self.now_path, "config/config.ini")

    def trans_time_number(self, time_str, key):
        return int(time_str.split(key)[0].strip())

    def trans_time(self, time_source: str):
        """解析不规范的时间字段, 识别优先级: min, hour, second

        :param time_source: 时间,如 '10mins', '15hours'
        :type time_source: str
        :raises TypeError: 提示配置有误
        :return: 返回秒数,用于sleep函数使用
        :rtype: tuple
        """
        if 'm' in time_source:
            return self.trans_time_number(time_source, "m") * 60
        elif 'h' in time_source:
            return self.trans_time_number(time_source, "h") * 3600
        elif 's' in time_source:
            return self.trans_time_number(time_source, "s")
        else:
            raise TypeError(f"config.ini配置信息错误, 请检查{time_source}")
    
    def catch_ini_info(self, ini_path, section):
        """解析配置文件,返回可迭代section

        :param ini_path: 配置文件路径
        :type ini_path: file_path
        """
        conf = ConfigParser()
        conf.read(ini_path)
        return conf[section]
    
    def test(self):
        # self.catch_ini_info(self.ini)
        print(self.trans_time("10 mi"))


if __name__ == "__main__":
    b = Base()
    b.test()
    