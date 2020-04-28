#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djsite2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入Django. 你确定已经安装并且"
            "设置好你的 PYTHONPATH 环境变量? 你是不是忘了 "
            "激活一个相关的虚拟环境?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
