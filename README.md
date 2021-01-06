Code comparison
===============

https://stackoverflow.com/questions/1119722/base-62-conversion

    How would you convert an integer to base 62.

## result

```
code   BG Wo Se ko LS mj we 
size   2  1  2  2  2  2  2
speed  1  3  2  4  4  2  3
memory 1  1  1  2  2  1  1
```

smaller is better.
BG looks the best code at all.

## BASE64 string

BASE64 string is taken from wikipedia like below:

```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

## Modifications

```
base62BG.py
    replace BASE62 into wikipedia's one.

base62Wo.py
    integer //= length
    s/base_decode/decode/
    s/base_encode/encode/

base62Se.py
    s/base_decode/decode/
    s/base_encode/encode/

base62ko.py
    replace BASE62 into wikipedia's one.
    s/toBase10/decode/
    s/toBase62/encode/

base62LS.py
    replace BASE62 into wikipedia's one.

base62mj.py
    replace BASE62 into wikipedia's one.
    s/encode_base62/encode/
    s/decode_base62/decode/

base62we.py
    dec //= 62, range()
    s/base62_encode_i/encode/
    s/base62_decode_i/decode/

base62py.py
```

## encoded string

- classifying

```
code a b c d e f g 
type 1 2 1 3 4 1 1
```

- original data

```
% hexdump rand128.dmp
0000000 08 cc 06 dc b4 5e 2f e1 25 95 db 59 0c 28 1e 03
0000010 e1 76 d6 fa d9 9e 80 2e 4f cf ac a1 53 41 a8 e6
0000020 ab 06 68 7c 89 27 ac ba 32 ad 92 dd 11 33 30 b0
0000030 f9 6e bd 09 38 0e 84 0a 81 e9 62 e9 c2 69 7c 99
0000040 25 4c bc 9b d5 de 0c 3b 73 35 2b 46 7e 76 88 14
0000050 2b 4b c2 c4 0f f1 72 cc cb 38 c1 3d 67 1b 4f 08
0000060 3c 82 8b 46 67 d0 74 12 4a ae 20 21 a6 2f 48 fa
0000070 ca 7a 34 ae 80 3c 5f 88 36 48 01 b6 78 ac 3a c1
```

- encoded string

```
type 1:
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOzZ

type 2:
zc1JOQny@x9pnrmgME7wfxtJrWSpW0bA@fHa5jgqzCGMpEv8ADHbEOHpbt4jcMIfBKLgAU3EgawuByWs9Fv9ABjbOrRtUceTcRaQp_tEwkaQL2N0@NsIPbec4ZpNJf23O2yQpDQ7giiGUw8qoLifHauziKw3Nvy3p80rpUH3H1

type 3:
1xOr7wDYzom64oKqymuo4aYCsqW2sKYyYKuaS0UCG48wGWCuIyAUQ0S0S00Y6OQcOcqUuEAUkWk28K0eOS8wA0ggGiMSWI60Ii8AcmmyU8UWyygWowMUoMue6g4u60cOOIcsMIcGigCcqymYaeQIM2O4kqQU6I8S4AaOsSyaWYSZ

type 4:
ZzOH8MP6YvCj3t28LHePClMQqYenKBkoRZAz7IZoJJOVhQbemGaHEIwYc1dymUJfsMlEhR5xSmV4Yo4BPUvGWL8WxkOI1RuiuZjO3qtK7FzrpGK2Tmkqz38KBlOtcQM3tqo4zPYpIgJJfkFaoZMT1zyZIhhjxLf1osRzYDw7rOx1
```

## making data

```
% ./eval.py -M
executing. ./eval.py -c BG -i data/rand128.dmp -o data/rand128en-BG.txt
executing. ./eval.py -c BG -i data/rand256.dmp -o data/rand256en-BG.txt
executing. ./eval.py -c BG -i data/rand512.dmp -o data/rand512en-BG.txt
executing. ./eval.py -c BG -i data/rand1024.dmp -o data/rand1024en-BG.txt
executing. ./eval.py -c Wo -i data/rand128.dmp -o data/rand128en-Wo.txt
executing. ./eval.py -c Wo -i data/rand256.dmp -o data/rand256en-Wo.txt
executing. ./eval.py -c Wo -i data/rand512.dmp -o data/rand512en-Wo.txt
executing. ./eval.py -c Wo -i data/rand1024.dmp -o data/rand1024en-Wo.txt
executing. ./eval.py -c Se -i data/rand128.dmp -o data/rand128en-Se.txt
executing. ./eval.py -c Se -i data/rand256.dmp -o data/rand256en-Se.txt
executing. ./eval.py -c Se -i data/rand512.dmp -o data/rand512en-Se.txt
executing. ./eval.py -c Se -i data/rand1024.dmp -o data/rand1024en-Se.txt
executing. ./eval.py -c ko -i data/rand128.dmp -o data/rand128en-ko.txt
executing. ./eval.py -c ko -i data/rand256.dmp -o data/rand256en-ko.txt
OverflowError: integer division result too large for a float

executing. ./eval.py -c ko -i data/rand512.dmp -o data/rand512en-ko.txt
OverflowError: integer division result too large for a float

executing. ./eval.py -c ko -i data/rand1024.dmp -o data/rand1024en-ko.txt
OverflowError: integer division result too large for a float

executing. ./eval.py -c LS -i data/rand128.dmp -o data/rand128en-LS.txt
executing. ./eval.py -c LS -i data/rand256.dmp -o data/rand256en-LS.txt
executing. ./eval.py -c LS -i data/rand512.dmp -o data/rand512en-LS.txt
executing. ./eval.py -c LS -i data/rand1024.dmp -o data/rand1024en-LS.txt
RecursionError: maximum recursion depth exceeded in comparison

executing. ./eval.py -c mj -i data/rand128.dmp -o data/rand128en-mj.txt
executing. ./eval.py -c mj -i data/rand256.dmp -o data/rand256en-mj.txt
executing. ./eval.py -c mj -i data/rand512.dmp -o data/rand512en-mj.txt
executing. ./eval.py -c mj -i data/rand1024.dmp -o data/rand1024en-mj.txt
executing. ./eval.py -c we -i data/rand128.dmp -o data/rand128en-we.txt
executing. ./eval.py -c we -i data/rand256.dmp -o data/rand256en-we.txt
executing. ./eval.py -c we -i data/rand512.dmp -o data/rand512en-we.txt
executing. ./eval.py -c we -i data/rand1024.dmp -o data/rand1024en-we.txt
executing. ./eval.py -c py -i data/rand128.dmp -o data/rand128en-py.txt
executing. ./eval.py -c py -i data/rand256.dmp -o data/rand256en-py.txt
executing. ./eval.py -c py -i data/rand512.dmp -o data/rand512en-py.txt
executing. ./eval.py -c py -i data/rand1024.dmp -o data/rand1024en-py.txt
```

## encoded data size

```
% ls -l data
total 128
-rw-r--r--  1 sakane  staff  1024 Jan  5 21:03 rand1024.dmp
-rw-r--r--  1 sakane  staff  1376 Jan  6 17:28 rand1024en-BG.txt
-rw-r--r--  1 sakane  staff  1376 Jan  6 17:29 rand1024en-Se.txt
-rw-r--r--  1 sakane  staff  1366 Jan  6 17:29 rand1024en-Wo.txt
-rw-r--r--  1 sakane  staff  1376 Jan  6 17:29 rand1024en-mj.txt
-rw-r--r--  1 sakane  staff  1376 Jan  6 17:29 rand1024en-py.txt
-rw-r--r--  1 sakane  staff  1376 Jan  6 17:29 rand1024en-we.txt
-rw-r--r--  1 sakane  staff   128 Jan  6 02:04 rand128.dmp
-rw-r--r--  1 sakane  staff   172 Jan  6 17:28 rand128en-BG.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-LS.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-Se.txt
-rw-r--r--  1 sakane  staff   170 Jan  6 17:28 rand128en-Wo.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-ko.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-mj.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-py.txt
-rw-r--r--  1 sakane  staff   172 Jan  6 17:29 rand128en-we.txt
-rw-r--r--  1 sakane  staff   256 Jan  6 01:52 rand256.dmp
-rw-r--r--  1 sakane  staff   344 Jan  6 17:28 rand256en-BG.txt
-rw-r--r--  1 sakane  staff   344 Jan  6 17:29 rand256en-LS.txt
-rw-r--r--  1 sakane  staff   344 Jan  6 17:29 rand256en-Se.txt
-rw-r--r--  1 sakane  staff   341 Jan  6 17:29 rand256en-Wo.txt
-rw-r--r--  1 sakane  staff   344 Jan  6 17:29 rand256en-mj.txt
-rw-r--r--  1 sakane  staff   344 Jan  6 17:29 rand256en-py.txt
-rw-r--r--  1 sakane  staff   344 Jan  6 17:29 rand256en-we.txt
-rw-r--r--  1 sakane  staff   512 Jan  6 01:52 rand512.dmp
-rw-r--r--  1 sakane  staff   688 Jan  6 17:28 rand512en-BG.txt
-rw-r--r--  1 sakane  staff   688 Jan  6 17:29 rand512en-LS.txt
-rw-r--r--  1 sakane  staff   688 Jan  6 17:29 rand512en-Se.txt
-rw-r--r--  1 sakane  staff   683 Jan  6 17:29 rand512en-Wo.txt
-rw-r--r--  1 sakane  staff   688 Jan  6 17:29 rand512en-mj.txt
-rw-r--r--  1 sakane  staff   688 Jan  6 17:29 rand512en-py.txt
-rw-r--r--  1 sakane  staff   688 Jan  6 17:29 rand512en-we.txt
```

## encoded data pattern

```
% for n in BG Wo Se ko LS mj we py ; do echo "\n" && fn=data/rand128en-${n}.txt && echo $fn && cat $fn ; done

data/rand128en-BG.txt
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOzZ

data/rand128en-Wo.txt
zc1JOQny@x9pnrmgME7wfxtJrWSpW0bA@fHa5jgqzCGMpEv8ADHbEOHpbt4jcMIfBKLgAU3EgawuByWs9Fv9ABjbOrRtUceTcRaQp_tEwkaQL2N0@NsIPbec4ZpNJf23O2yQpDQ7giiGUw8qoLifHauziKw3Nvy3p80rpUH3H1

data/rand128en-Se.txt
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOzZ

data/rand128en-ko.txt
1xOr7wDYzom64oKqymuo4aYCsqW2sKYyYKuaS0UCG48wGWCuIyAUQ0S0S00Y6OQcOcqUuEAUkWk28K0eOS8wA0ggGiMSWI60Ii8AcmmyU8UWyygWowMUoMue6g4u60cOOIcsMIcGigCcqymYaeQIM2O4kqQU6I8S4AaOsSyaWYSZ

data/rand128en-LS.txt
ZzOH8MP6YvCj3t28LHePClMQqYenKBkoRZAz7IZoJJOVhQbemGaHEIwYc1dymUJfsMlEhR5xSmV4Yo4BPUvGWL8WxkOI1RuiuZjO3qtK7FzrpGK2Tmkqz38KBlOtcQM3tqo4zPYpIgJJfkFaoZMT1zyZIhhjxLf1osRzYDw7rOx1

data/rand128en-mj.txt
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOzZ

data/rand128en-we.txt
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOzZ

data/rand128en-py.txt
1xOr7wDYzRso1fLxjhhIZyz1TMZoaFkfJJgIpYPz4oqt3MQctOlBK83zqkmT2KGprzF7Ktq3OjZuiuR1IOkxW8LWGvUPB4oY4VmSx5RhElMsfJUmyd1cYwIEHaGmebQhVOJJoZI7zAZRokBKneYqQMlCPeHL82t3jCvY6PM8HOz
```

## Initial check (very short data).

```
% ./eval.py -B
## Initial check (very short data).
### Code: BG
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: Wo
- Original data: b'ab'
Encoded string: 65y
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1xoCdA
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: Se
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: ko
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: LS
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: asPZm1
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: mj
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
"""
Decoded number: 1
True
### Code: we
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
### Code: py
- Original data: b'ab'
Encoded string: 6U6
Decoded number: 24930
True
- Original data: b'abcd'
Encoded string: 1mZPsa
Decoded number: 1633837924
True
- Original data: b'\x00\x01'
Encoded string: 1
Decoded number: 1
True
- Original data: b'\x00\x00\x01'
Encoded string: 1
Decoded number: 1
True
```

## 

```
% ./eval.py -X
executing. ./eval.py -c BG -E
## Timeit: BG encoding
data/rand128.dmp 1.150345531
data/rand256.dmp 1.750482229
data/rand512.dmp 3.014687352
data/rand1024.dmp 4.446291773

executing. ./eval.py -c BG -E -d
## Timeit: BG decoding
data/rand128en-BG.txt 2.9281760770000003
data/rand256en-BG.txt 4.140904781
data/rand512en-BG.txt 8.14172112
data/rand1024en-BG.txt 16.374926721

executing. ./eval.py -c Wo -E
## Timeit: Wo encoding
data/rand128.dmp 1.7984873300000002
data/rand256.dmp 3.025364228
data/rand512.dmp 5.7248722
data/rand1024.dmp 8.793173094000002

executing. ./eval.py -c Wo -E -d
## Timeit: Wo decoding
data/rand128en-Wo.txt 2.3036571649999997
data/rand256en-Wo.txt 3.486529079
data/rand512en-Wo.txt 7.021175856
data/rand1024en-Wo.txt 15.293358747000001

executing. ./eval.py -c Se -E
## Timeit: Se encoding
data/rand128.dmp 1.351012378
data/rand256.dmp 1.95121599
data/rand512.dmp 3.3848083119999997
data/rand1024.dmp 4.881064842

executing. ./eval.py -c Se -E -d
## Timeit: Se decoding
data/rand128en-Se.txt 0.49796012100000003
data/rand256en-Se.txt 0.612176036
data/rand512en-Se.txt 0.9097908100000001
data/rand1024en-Se.txt 1.2493047170000002

executing. ./eval.py -c ko -E
OverflowError: integer division result too large for a float

## Timeit: ko encoding
data/rand128.dmp 2.362107742

executing. ./eval.py -c ko -E -d
FileNotFoundError: [Errno 2] No such file or directory: 'data/rand256en-ko.txt'

## Timeit: ko decoding
data/rand128en-ko.txt 0.977722909

executing. ./eval.py -c LS -E
RecursionError: maximum recursion depth exceeded in comparison

## Timeit: LS encoding
data/rand128.dmp 2.078450003
data/rand256.dmp 3.3803402879999997
data/rand512.dmp 6.386202400000001
FileNotFoundError: [Errno 2] No such file or directory: 'data/rand1024en-LS.txt'

## Timeit: LS decoding
data/rand128en-LS.txt 3.330581055
data/rand256en-LS.txt 4.7009656500000006
data/rand512en-LS.txt 9.015914672000001

executing. ./eval.py -c mj -E
## Timeit: mj encoding
data/rand128.dmp 1.367665948
data/rand256.dmp 1.9671295359999998
data/rand512.dmp 3.39414159
data/rand1024.dmp 4.886276939

executing. ./eval.py -c mj -E -d
## Timeit: mj decoding
data/rand128en-mj.txt 1.448302911
data/rand256en-mj.txt 1.6419888989999998
data/rand512en-mj.txt 2.1248602890000003
data/rand1024en-mj.txt 2.544945021

executing. ./eval.py -c we -E
## Timeit: we encoding
data/rand128.dmp 1.792983236
data/rand256.dmp 3.0632432489999997
data/rand512.dmp 5.759132660000001
data/rand1024.dmp 8.780794731

executing. ./eval.py -c we -E -d
## Timeit: we decoding
data/rand128en-we.txt 3.1107905579999997
data/rand256en-we.txt 4.364036964
data/rand512en-we.txt 8.051533847
data/rand1024en-we.txt 16.419350202000004

executing. ./eval.py -c py -E
## Timeit: py encoding
data/rand128.dmp 1.896242014
data/rand256.dmp 3.117141737
data/rand512.dmp 5.622818481
data/rand1024.dmp 8.572743477

executing. ./eval.py -c py -E -d
## Timeit: py decoding
data/rand128en-py.txt 3.243203345
data/rand256en-py.txt 4.5838909359999995
data/rand512en-py.txt 8.805824765
data/rand1024en-py.txt 16.776439615
```

## なぜやってみたのか？

base62 binary encoder/decoder を探していた。

上記は元が整数をbase62 encode/decode するというのテーマなので、
文字列やバイト列は扱えない。

文字列を扱うには bytes を int に変換してからエンコードする。
しかし、big number をbase62でエンコードしているので、
デコードした結果も big number になる。
デコードした後に元の bytes のサイズが失われるので戻すことができない。

結局、https://github.com/suminb/base62 は binaryもサポートしているので採用。

