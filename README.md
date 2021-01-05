Code comparison
===============

https://stackoverflow.com/questions/1119722/base-62-conversion

## result

a looks the best code at all.

```
code   a b c d e f g 
size   2 1 2 2 2 2 2
speed  1 3 2 4 4 2 3
memory 1 1 1 2 2 1 1
```

## BASE64 string

BASE64 string is taken from wikipedia like below:

```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
```

## file sample.txt

```
% hexdump sample.txt
0000000 31 32
```

## Measurement

```
0. Any modifications.
2. Encoded string of '12'. Command: python base62a.py sample.txt
3. Decoded number of #2. Command: python base62a.py sample.txt d
4. Check and encoded size. Command: python base62a.py rand128.dmp | wc -c
5. Check and encoded size. Command: python base62a.py rand256.dmp | wc -c
6. Check and encoded size. Command: python base62a.py rand1024.dmp | wc -c
7. Timeit. Command: python base62a.py

base62a.py
    0. BASE62文字列を修正
    2. 3H8
    3. 12594
    4. 173
    5. 345
    6. 1377
    7. 
        rand128.dmp 1.15060702
        rand256.dmp 1.7725877580000002
        rand512.dmp 3.0224366350000005
        rand1024.dmp 4.485375492

base62b.py
    0. integer //= length
    2. 34O
    3. 12594
    4. 171
    5. 342
    6. 1367
    7. 
        rand128.dmp 1.795423812
        rand256.dmp 3.064219188
        rand512.dmp 5.754633555
        rand1024.dmp 8.731376784999998

base62c.py
    0. 
    2. 3H8
    3. 12594
    4. 173
    5. 345
    6. 1377
    7.
        rand128.dmp 1.314013325
        rand256.dmp 1.93440177
        rand512.dmp 3.353189208
        rand1024.dmp 4.863234354

base62d.py
    0. BASE62文字列を修正
    2. 3H8
    3. 12594
    4. 173
    5. OverflowError: integer division result too large for a float
    6. OverflowError: integer division result too large for a float
    7.
        rand128.dmp 2.343731752
        rand256.dmp NA
        rand512.dmp NA
        rand1024.dmp NA

base62e.py
    0. BASE62文字列を修正
    2. 8H3
    3. 12594
    4. 173
    5. 345
    6. RecursionError: maximum recursion depth exceeded in comparison
    7.
        rand128.dmp 2.075309834
        rand256.dmp 3.3831268490000004
        rand512.dmp 6.310743282
        rand1024.dmp NA

base62f.py
    0. BASE62文字列を修正
    2. 3H8
    3. 12594
    4. 173
    5. 345
    6. 1377
    7.
        rand128.dmp 1.39898395
        rand256.dmp 1.9714964299999997
        rand512.dmp 3.416826287
        rand1024.dmp 4.903553506

base62g.py
    0. dec //= 62, range()
    2. 3H8
    3. 12594
    4. 173
    5. 345
    6. 1377
    7.
        rand128.dmp 1.841803575
        rand256.dmp 3.1044888090000002
        rand512.dmp 5.8235807930000005
        rand1024.dmp 8.923519868000001
```

## encoded string

### original data

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

### classifying

```
code a b c d e f g 
type 1 2 1 3 4 1 1
```

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

### command

```
python base62a.py rand128.dmp | tee a | wc -c
python base62b.py rand128.dmp | tee b | wc -c
python base62c.py rand128.dmp | tee c | wc -c
python base62d.py rand128.dmp | tee d | wc -c
python base62e.py rand128.dmp | tee e | wc -c
python base62f.py rand128.dmp | tee f | wc -c
python base62g.py rand128.dmp | tee g | wc -c
```

