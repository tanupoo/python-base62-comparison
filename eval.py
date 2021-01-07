#!/usr/bin/env python

from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter

code_name = [ "BG", "Wo", "Se", "ko", "LS", "mj", "we", "py" ]

eval_orig_data = [
        ("data/ff128.dmp", 20000),
        ("data/ff256.dmp", 10000),
        ("data/ff512.dmp", 5000),
        ("data/ff768.dmp", 3000),
        ("data/ff1024.dmp", 2000),
        ("data/ff1536.dmp", 1500),
        ("data/ff2048.dmp", 1000),
        ("data/rand1024.dmp", 2000),
        ]

eval_encoded_data = [
        ("data/ff128en-{}.txt", 10000),
        ("data/ff256en-{}.txt", 5000),
        ("data/ff512en-{}.txt", 2500),
        ("data/ff768en-{}.txt", 1500),
        ("data/ff1024en-{}.txt", 1000),
        ("data/ff1536en-{}.txt", 700),
        ("data/ff2048en-{}.txt", 500),
        ("data/rand1024en-{}.txt", 2000),
        ]

ap = ArgumentParser(
        description="evaluation script.",
        formatter_class=ArgumentDefaultsHelpFormatter)
ap.add_argument("-c", action="store", dest="code_name",
                choices=code_name,
                help="specify a code name for use.")
ap.add_argument("-i", action="store", dest="input_file",
                help="specify a file name containing the data to be encoded.")
ap.add_argument("-o", action="store", dest="output_file",
                help="specify a file name to store the output.")
ap.add_argument("-d", action="store_true", dest="decode_mode",
                help="invoke to run as the decode mode, instead of the encode mode.")
ap.add_argument("-E", action="store_true", dest="eval_mode",
                help="invoke to evaluate the code specified.")
ap.add_argument("-X", action="store_true", dest="eval_all_mode",
                help="invoke to evaluate all codes.")
ap.add_argument("-B", action="store_true", dest="base_check_mode",
                help="invoke to check if the decoded data will be "
                "same value to the input one.")
# the data set are made under data directory.
ap.add_argument("-M", action="store_true", dest="make_data_mode",
                help="invoke to make data set.")
opt = ap.parse_args()

if not (opt.make_data_mode or opt.eval_all_mode or opt.base_check_mode) and not opt.code_name:
    raise ValueError(f"ERROR: this mode requires a code name. either {code_name}")

if not (opt.eval_all_mode or opt.eval_mode or opt.make_data_mode or opt.base_check_mode) and not opt.input_file:
    raise ValueError("ERROR: this mode requires an input file.")

from subprocess import Popen, PIPE, DEVNULL
import shlex
def exec_command(cmd):
    print(f"executing. {cmd}")
    p = Popen(shlex.split(cmd),
                stdout=PIPE, stderr=PIPE, stdin=DEVNULL,
                universal_newlines=True)
    (stdout_data, stderr_data) = p.communicate()
    if stderr_data:
        print("ERROR:", stderr_data.split("\n")[-2])
    if stdout_data:
        print(stdout_data)

if opt.eval_all_mode:
    for cn in code_name:
        exec_command(f"./eval.py -c {cn} -E")
        exec_command(f"./eval.py -c {cn} -E -d")
    exit(0)

if opt.eval_mode:
    import timeit
    if opt.decode_mode:
        print(f"## Timeit: {opt.code_name} decoding")
        for fname_base,nb_try in eval_encoded_data:
            fname = fname_base.format(opt.code_name)
            result = timeit.timeit(
                setup=f'''
from base62{opt.code_name} import decode
buf = open("{fname}", "r").read()
                ''',
                stmt=f'''
d = decode(buf)
                ''',
                number=nb_try
            )
            print(fname, result)
    else:
        print(f"## Timeit: {opt.code_name} encoding")
        for fname,nb_try in eval_orig_data:
            result = timeit.timeit(
                setup=f'''
from base62{opt.code_name} import encode
buf = open("{fname}", "rb").read()
num = int.from_bytes(buf, "big")
                ''',
                stmt=f'''
e = encode(num)
                ''',
                number=nb_try
            )
            print(fname, result)
    exit(0)

if opt.make_data_mode:
    import os.path
    for cn in code_name:
        for fname,nb_try in eval_orig_data:
            bn,pn = os.path.splitext(fname)
            exec_command(f"./eval.py -c {cn} -i {fname} -o {bn}en-{cn}.txt")
    exit(0)

def base62_decode(mod, input_data, output_file=None):
    d = mod.decode(input_data)
    if output_file:
        dd = d
        result = []
        while dd > 0:
            dd, mod = divmod(dd, 256)
            result.append(mod)
        with open(output_file, "wb") as fd:
            fd.write(bytes(result[::-1]))
    else:
        print(d)
    return d

def base62_encode(mod, buf: bytes, output_file=None):
    num = int.from_bytes(buf, "big")
    e = mod.encode(num)
    if output_file:
        with open(output_file, "w") as fd:
            fd.write(e)
    else:
        print(e)
    return e

from importlib import import_module

if opt.base_check_mode:
    print("## Initial check (very short data).")
    for cn in code_name:
        print(f"### Code: {cn}")
        for test_msg in [ b"ab", b"abcd", bytes([0xff,0xff]), bytes([0,1]), bytes([0,0,1]) ]:
            num = int.from_bytes(test_msg, "big")
            print(f"- Original data: {test_msg}")
            mod = import_module(f"base62{cn}")
            e = mod.encode(num)
            print(f"    + Encoded string: {e}")
            d = mod.decode(e)
            print(f"    + Decoded number: {d}")
            print(f"    + Decoded == Original: {num == d}")
        print()
    exit(0)

mod = import_module(f"base62{opt.code_name}")
if opt.decode_mode:
    buf = open(opt.input_file, "r").read()
    base62_decode(mod, buf, opt.output_file)
else:
    buf = open(opt.input_file, "rb").read()
    base62_encode(mod, buf, opt.output_file)

