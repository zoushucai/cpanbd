import os
import re
from pathlib import Path
from typing import Any

from dotenv import find_dotenv, load_dotenv


def load_env():
    """加载 .env 配置(优先项目目录, 其次系统目录)"""

    # 在当前目录下查找 .env 文件,找到则返回路径, 否则返回空字符串
    dotenv_path: str = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path, override=True)
    else:
        # 尝试从系统默认目录加载
        system_env_path = Path.home() / ".env.panbd"
        if system_env_path.exists():
            load_dotenv(system_env_path, override=True)
        else:
            return


load_env()
HEADERS = {
    "User-Agent": "pan.baidu.com",
    "Content-Type": "application/json",
}
BASE_URL = "https://pan.baidu.com"
APPNAME = os.getenv("BAIDU_APPNAME", None)

assert APPNAME, "BAIDU_APPNAME 环境变量未设置"

TEMPLATE_PATTERN = re.compile(r"{{\s*([\w\.]+)\s*}}", re.IGNORECASE)
EMBEDDED_TEMPLATE_PATTERN = re.compile(r"{{{\s*([\w\.]+)\s*}}}", re.IGNORECASE)
TYPE_MAP = {
    "int": int,
    "float": float,
    "str": str,
    "number": float,
    "string": str,
    "bool": bool,
    "boolean": bool,
    "list": list,
    "dict": dict,
    "object": dict,
    "array": list,
    "any": Any,
    "none": type(None),
    "null": type(None),
}
DEFAULT_BY_TYPE = {
    "int": 0,
    "float": 0.0,
    "str": "",
    "string": "",
    "number": 0.0,
    "bool": False,
    "boolean": False,
    "list": [],
    "dict": {},
}
