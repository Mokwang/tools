import os
import difflib
import argparse


def string_similar(s1, s2):
    """
    对比s1 和 s2相识度
    :param s1:
    :param s2:
    :return: 相识度百分比，float
    """
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def read_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        read = f.readlines()
    return read


def main(file_a, file_b):
    fa = read_file(file_a)
    fb = read_file(file_b)
    for line in fa:
        if line not in fb:
            print("%s>>>>\n%s" % (file_a, line))
    for line in fb:
        if line not in fa:
            print("%s>>>>\n%s" % (file_b, line))


if __name__ == "__main__":
    arg = argparse.ArgumentParser("file compare tools")
    arg.add_argument("-a", "--file_A", type=str, dest="fa", required=True, help="A file name")
    arg.add_argument("-b", "--file_B", type=str, dest="fb", required=True, help="B file name")
    opt = arg.parse_args()
    main(opt.fa, opt.fb)
