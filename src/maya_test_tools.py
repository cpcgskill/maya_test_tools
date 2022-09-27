# -*-coding:utf-8 -*-
u"""
:创建时间: 2022/5/11 19:43
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

import os.path
import sys
import subprocess

from maya.cmds import file, about


def new_file():
    file(f=True, new=True)


def open_file(f):
    try:
        file(f, open=True, force=True, typ="mayaAscii", options="v=0;", ignoreVersion=True)
    except RuntimeError as rx:
        sys.stderr.write('读取文件出错: \n')
        for i in rx.args:
            sys.stderr.write(i.encode('utf-8').decode('utf-8'))
            sys.stderr.write('\n')


def open_maya_gui():
    test_file_path = "C:\\Users\\PC\\Documents\\maya\\projects\\default\\scenes\\test.ma"
    file(rename=test_file_path)
    file(save=True, type='mayaAscii')
    maya_executable = os.sep.join([os.path.dirname(sys.executable), 'maya.exe'])
    subprocess.call([maya_executable, test_file_path])


def question_open_maya_gui():
    if 'RIG_TEST_NO_QUESTION' in os.environ:
        if os.environ.get('RIG_TEST_NO_QUESTION').upper() in ('Y', 'YES', 'ON'):
            open_maya_gui()
            return
    if sys.version_info.major < 3:
        new_input = raw_input
    else:
        new_input = input
    if new_input('whether to open the maya user interface ? (YES|Y) or (NO|N): ').upper() in ('Y', "YES"):
        open_maya_gui()
        return
