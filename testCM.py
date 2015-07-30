# −*− coding: UTF−8 −*−
"""
CryptoMobile: library to provide python bindings to mobile cryptographic
reference implementation. 
Copyright (C) 2013 Benoit Michau, ANSSI

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
########################################################
# CryptoMobile python toolkit
#
# Interfaces C implementation of reference mobile cryptographic algorithms 
# to python primitives
# WARNING: mobile crypto algorithms specifications are freely available on the web, 
# but generally require license to be used in field equipments
#
# C source code from 3GPP / ETSI / GSMA / NIST web pages:
# - Kasumi (UEA1, UIA1)
# - SNOW3G (UEA2, UIA2, EEA1, EIA1)
# - ZUC (EEA3, EIA3)
# - AES (EEA2, EIA2) - from pycrypto
#######################################################

from time import time
from CM import AES_3GPP
import binascii
###
# Kasumi, F8, F9: testsets from 3GPP TS 35.203 Rel.10
###

###
# EEA2, EIA2: testsets from 3GPP TS 33.401
###

def aes_EEA2_testset_1():
    aes3gpp = AES_3GPP()
    key     = '\xd3\xc5\xd5\x922\x7f\xb1\x1c@5\xc6h\n\xf8\xc6\xd1'
    count   = 0x398a59b4 
    bearer  = 0x15
    direct  = 1
    data    = '\x98\x1b\xa6\x82L\x1b\xfb\x1a\xb4\x85G )\xb7\x1d\x80\x8c\xe3>,\xc3\xc0\xb5\xfc\x1f=\xe8\xa6\xdcf\xb1\xf0'
    bitlen  = 253
    output  = '\xe9\xfe\xd8\xa6=\x15S\x04\xd7\x1d\xf2\x0b\xf3\xe8"\x14\xb2\x0e\xd7\xda\xd2\xf23\xdc<"\xd7\xbd\xee\xed\x8ex'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EEA2_testset_2():
    aes3gpp = AES_3GPP()
    key     = '+\xd6E\x9f\x82\xc4@\xe0\x95,I\x10H\x05\xffH'
    count   = 0xc675a64b 
    bearer  = 0xc
    direct  = 1
    data    = '~\xc6\x12rt;\xf1aG&Djl8\xce\xd1f\xf6\xcav\xebT0\x04B\x864l\xef\x13\x0f\x92\x92+\x03E\r:\x99u\xe5\xbd.\xa0\xebU\xad\x8e\x1b\x19\x9e>\xc41` \xe9\xa1\xb2\x85\xe7bySY\xb7\xbd\xfd9\xbe\xf4\xb2HE\x83\xd5\xaf\xe0\x82\xae\xe68\xbf_\xd5\xa6\x06\x199\x01\xa0\x8fJ\xb4\x1a\xab\x9b\x13H\x80'
    bitlen  = 798
    output  = 'Ya`SS\xc6K\xdc\xa1[\x19^(\x85S\xa9\x10c%\x06\xd6 \n\xa7\x90\xc4\xc8\x06\xc9\x99\x04\xcf$E\xccP\xbb\x1c\xf1h\xa4\x96ssN\x08\x1bW\xe3$\xceRY\xc0\xe7\x8dL\xd9{\x87\tvP<\tC\xf2\xcbZ\xe8\xf0R\xc7\xb7\xd3\x92#\x95\x87\xb8\x95`\x86\xbc\xab\x18\x83`B\xe2\xe6\xceBC*\x17\x10\\S\xd0'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EEA2_testset_3():
    aes3gpp = AES_3GPP()
    key     = '\n\x8bk\xd8\xd9\xb0\x8b\x08\xd6N2\xd1\x81ww\xfb'
    count   = 0x544d49cd
    bearer  = 0x4
    direct  = 0
    data    = '\xfd@\xa4\x1d7\n\x1fetP\x95h}G\xba\x1d6\xd24\x9e#\xf6D9,\x8e\xa9\xc4\x9d@\xc12q\xaf\xf2d\xd0\xf2H\x00'
    bitlen  = 310
    output  = 'uu\r7\xb4\xbb\xa2\xa4\xde\xdb4#[\xd6\x8cfE\xac\xda\xac\xa4\x818\xa3\xb0\xc4q\xe2\xa7\x04\x1aWd#\xd2\x92r\x87\xf0'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EEA2_testset_4():
    aes3gpp = AES_3GPP()
    key     = '\xaa\x1f\x95\xae\xa53\xbc\xb3.\xb6;\xf5-\x8f\x83\x1a'
    count   = 0x72d8c671
    bearer  = 0x10
    direct  = 1
    data    = '\xfb\x1b\x96\xc5\xc8\xba\xdf\xb2\xe8\xe8\xed\xfd\xe7\x8eW\xf2\xad\x81\xe7A\x03\xfcC\nSM\xcc7\xaf\xce\xc7\x0e\x15\x17\xbb\x06\xf2r\x19\xda\xe4\x90"\xdd\xc4z\x06\x8d\xe4\xc9Ij\x95\x1ak\t\xed\xbd\xc8d\xc7\xad\xbdt\n\xc5\x0c\x02/0\x82\xba\xfd"\xd7\x81\x97\xc5\xd5\x08\xb9w\xbc\xa1?2\xe6R\xe7K\xa7(W`w\xceb\x8cS^\x87\xdc`w\xba\x07\xd2\x90hY\x0c\x8c\xb5\xf1\x08\x8e\x08,\xfa\x0e\xc9a0-i\xcf=D'
    bitlen  = 1022
    output  = '\xdf\xb4@\xac\xb3w5I\xef\xc0F(\xae\xb8\xd8\x15bu#\x0b\xdci\r\x94\xb0\r\x8d\x95\xf2\x8cKV0\x7f`\xf4\xcaU\xeb\xa6a\xeb\xbar\xac\x80\x8f\xa8\xc4\x9e&x\x8e\xd0J]`l\xb4\x18\xdet\x87\x8b\x9a"\xf8\xef)Y\x0b\xc4\xebW\xc9\xfa\xf7\xc4\x15$\xa8\x85\xb8\x97\x9cB?/\x8f\x8e\x05\x92\xa9\x87\x92\x01\xbe\x7f\xf9wz\x16*\xb8\x10\xfe\xb3$\xbat\xc4\xc1V\xe0M9\tr\te:\xc3>Z_-\x88d'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EEA2_testset_5():
    aes3gpp = AES_3GPP()
    key     = '\x96\x18\xaeF\x89\x1f\x86W\x8e\xeb\xe9\x0e\xf7\xa1 .'
    count   = 0xc675a64b 
    bearer  = 0xc
    direct  = 1
    data    = '\x8d\xaa\x17\xb1\xae\x05\x05)\xc6\x82\x7f(\xc0\xefj\x12B\xe9?\x8b1O\xb1\x8aw\xf7\x90\xae\x04\x9f\xed\xd6\x12&\x7f\xec\xae\xfcE\x01t\xd7m\x9f\x9a\xa7uZ0\xcd\x90\xa9\xa5\x87K\xf4\x8e\xafp\xee\xa3\xa6*%\n\x8bk\xd8\xd9\xb0\x8b\x08\xd6N2\xd1\x81ww\xfbTMI\xcdIr\x0e!\x9d\xbf\x8b\xbe\xd39\x04\xe1\xfd@\xa4\x1d7\n\x1fetP\x95h}G\xba\x1d6\xd24\x9e#\xf6D9,\x8e\xa9\xc4\x9d@\xc12q\xaf\xf2d\xd0\xf2HA\xd6F_\t\x96\xff\x84\xe6_\xc5\x17\xc5>\xfc3c\xc3\x84\x92\xa8'
    bitlen  = 1245
    output  = '\x91\x9c\x8c3\xd6g\x89p=\x05\xa0\xd7\xce\x82\xa2\xae\xacN\xe7l\x0fM\xa0P3^\x8a\x84\xe7\x89{\xa5\xdf/6\xbdQ>=\x0c\x85x\xc7\xa0\xfc\xf0C\xe0:\xa3\xa3\x9f\xba\xad}\x15\xbe\x07O\xaa]\x90)\xf7\x1f\xb4W\xb6G\x83G\x14\xb0\xe1\x8f\x11\x7f\xca\x10gyE\tl\x8c_2k\xa8\xd6\t^\xb2\x9c>6\xcf$]\x16"\xaa\xfe\x92\x1fuf\xc4\xf5\xd6D\xf2\xf1\xfc\x0e\xc6\x84\xdd\xb2\x13Itv"\xe2\t)]\'\xff?\x95b3q\xd4\x9b\x14|\n\xf4\x86\x17\x1f"\xcd\x04\xb1\xcb\xeb&X">i8'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EEA2_testset_6():
    aes3gpp = AES_3GPP()
    key     = 'T\xf4\xe2\xe0L\x83xn\xec\x8f\xb5\xab\xe8\xe3ef'
    count   = 0xaca4f50f
    bearer  = 0xb
    direct  = 0
    data    = "@\x98\x1b\xa6\x82L\x1b\xfbB\x86\xb2\x99x=\xafD,\t\x9fz\xb0\xf5\x8d\\\x8eF\xb1\x04\xf0\x8f\x01\xb4\x1a\xb4\x85G )\xb7\x1d6\xbd\x1a=\x90\xdc:A\xb4mQg*\xc4\xc9f:+\xe0c\xdaK\xc8\xd2\x80\x8c\xe3>,\xcc\xbf\xc64\xe1\xb2Y\x06\x08v\xa0\xfb\xb5\xa47\xeb\xcc\x8d1\xc1\x9eDT1\x87E\xe3\xfa\x16\xbb\x11\xad\xae$\x88y\xfeR\xdb%C\xe5<\xf4E\xd3\xd8(\xce\x0b\xf5\xc5`Y=\x97'\x8aYv-\xd0\xc2\xc9\xcdh\xd4Ijy%\x08a@\x14\xb1;j\xa5\x11(\xc1\x8c\xd6\xa9\x0b\x87\x97\x8c/\xf1\xca\xbe}\x9f\x89\x8aA\x1b\xfd\xb8Oh\xf6r{\x14\x99\xcd\xd3\r\xf0D:\xb4\xa6fS3\x0b\xcb\xa1\x10^L\xec\x03Ls\xe6\x05\xb41\x0e\xaa\xad\xcf\xd5\xb0\xca'\xff\xd8\x9d\x14M\xf4y'YB|\x9c\xc1\xf8\xcd\x8c\x87 #d\xb8\xa6\x87\x95L\xb0Z\x8dN-\x99\xe7=\xb1`\xde\xb1\x80\xad\x08A\xe9gA\xa5\xd5\x9f\xe4\x18\x9f\x15B\x00&\xfeL\xd1!\x04\x93/\xb3\x8fsS@C\x8a\xaf~\xcao\xd5\xcf\xd3\xa1\x95\xceZ\xbee'*\xf6\x07\xad\xa1\xbee\xa6\xb4\xc9\xc0i24\t,M\x01\x8f\x17V\xc6\xdb\x9d\xc8\xa6\xd8\x0b\x88\x818akh\x12b\xf9T\xd0\xe7q\x17Hx\r\x92)\x1d\x86)\x99r\xdbt\x1c\xfaO7\xb8\xb5l\xdb\x18\xa7\xca\x82\x18\xe8nKKqjM\x047\x1f\xbe\xc2b\xfcZ\xd0\xb3\x81\x9b\x18{\x97\xe5[\x1aM|\x19\xee$\xc8\xb4\xd7r<\xfe\xdf\x04[\x8a\xca\xe4\x86\x95\x17\xd8\x0ePa]\x905\xd5\xd9\xc5\xa4\n\xf6\x02(\x0bT%\x97\xb0\xcb\x18a\x9e\xeb5\x92WY\xd1\x95\xe1\x00\xe8\xe4\xaa\x0c8\xa3\xc2\xab\xe0\xf3\xd8\xff\x04\xf3\xc3<)Pi\xc26\x94\xb5\xbb\xea\xcd\xd5B\xe2\x8e\x8a\x94\xed\xb9\x11\x9fA-\x05K\xe1\xfar\x00\xb0\x90\x00"
    bitlen  = 3861
    output  = '\\\xb7,n\xdc\x87\x8f\x15f\xe1\x02S\xaf\xc3d\xc9\xfaT\r\x91M\xb9L\xbe\xe2u\xd0\x91|\xa6\xaf\rw\xac\xb4\xef;\xbe\x1ar+.\xf5\xbd\x1dK\x8e*\xa5\x02N\xc18\x8a \x1e{\xcey \xae\xc6\x15\x89_v:Ud\xdc\xc4\xc4\x82\xa2\xee\x1d\x8b\xfe\xccD\x98\xec\xa8?\xbbu\xf9\xabS\x0e\r\xaf\xbe\xde/\xa5\x89[\x82\x99\x1bbw\xc5)\xe0\xf2R\x9d\x7fy`k\xe9g\x06)m\xed\xfa\x9dt\x12\xb6\x16\x95\x8c\xb5c\xc6x\xc0(%\xc3\r\n\xeew\xc4\xc1F\xd2vT\x12B\x1a\x80\x8d\x13\xce\xc8\x19iLu\xadW.\x9b\x97=\x94\x8b\x81\xa93|;*\x17\x19."\xc2\x06\x9f~\xd1\x16*\xf4L\xde\xa8\x17`6e\xe8\x07\xce@\xc8\xe0\xdd\x9dc\x94\xdcn1\x15?\xe1\x95\\G\xaf\xb5\x1f&\x17\xee\x0c^;\x8e\xf1\xadut\xed4>\xdc\'C\xcc\x94\xc9\x90\xe1\xf1\xfd&BS\xc1x\xde\xa79\xc0\xbe\xfe\xeb\xcd\x9f\x9bv\xd4\x9c\x10\x15\xc9\xfe\xcfP\xe5;\x8bR\x04\xdb\xcd>\xed\x868U\xda\xbc\xdc\xc9K1\xe3\x18\x02\x15h\x85\\\x8b\x9eR\xa9\x81\x95z\x11(\'\xf9x\xba\x96\x0f\x14G\x91\x1b1{U\x11\xfb\xcc\x7f\xb1:\xc1S\xdbt%\x11\x17\xe4\x86\x1e\xb9\xe8;\xff\xff\xc4\xebwUW\x908\xe5y$\xb1\xf7\x8b>\x1a\xd9\x0b\xab*\x07\x87\x1br\xdb^\xef\x96\xc34\x04If\xdb\x0c7\xca\xfd\x1a\x89\xe5dj5\x80\xebde\xf1!\xdc\xe9\xcb\x88\xd8[\x96\xcf#\xcc\xcc\xd4(\x07g\xbe\xe8\xee\xb2=\x86RF\x1d\xb6I1\x03\x00;\xaf\x89\xf5\xe1\x82a\xeaC\xc8J\x92\xeb\xff\xff\xe4\x90\x9d\xc4lQ\x92\xf8%\xf7p`\x0b\x96\x02\xc5W\xb5\xf8\xb41\xa7\x9dE\x97}\xd9\xc4\x1b\x86=\xa9\xe1B\xe9\x00 \xcf\xd0t\xd6\x92{z\xb3\xb6r]\x1ao?\x98\xb9\xc9\xda\xa8\x98*\xff\x06x('
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_1():
    aes3gpp = AES_3GPP()
    key     = '+\xd6E\x9f\x82\xc5\xb3\x00\x95,I\x10H\x81\xffH'
    count   = 0x38a6f056
    bearer  = 0x18
    direct  = 0
    data    = '324bc98@'
    bitlen  = 58
    output  = '\x11\x8cn\xb8'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_2():
    aes3gpp = AES_3GPP()
    key     = '\xd3\xc5\xd5\x922\x7f\xb1\x1c@5\xc6h\n\xf8\xc6\xd1'
    count   = 0x398a59b4 
    bearer  = 0x1a
    direct  = 1
    data    = 'HE\x83\xd5\xaf\xe0\x82\xae'
    bitlen  = 64
    output  = '\xb97\x87\xe6'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_3():
    aes3gpp = AES_3GPP()
    key     = '~^\x94C\x1e\x11\xd78(\xd79\xccl\xedEs'
    count   = 0x36af6144 
    bearer  = 0x18
    direct  = 1
    data    = '\xb3\xd3\xc9\x17\nN\x162\xf6\x0f\x86\x10\x13\xd2-\x84\xb7&\xb6\xa2x\xd8\x02\xd1\xee\xaf\x13!\xbaY)\xdc'
    bitlen  = 254
    output  = '\x1f`\xb0\x1d'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_4():
    aes3gpp = AES_3GPP()
    key     = '\xd3A\x9b\xe8!\x08z\xcd\x02\x12:\x92H\x033Y'
    count   = 0xc7590ea9
    bearer  = 0x17
    direct  = 0
    data    = '\xbb\xb0W\x03\x88\tIk\xcf\xf8mo\xbc\x8c\xe5\xb15\xa0k\x16`T\xf2\xd5e\xbe\x8a\xceu\xdc\x85\x1e\x0b\xcd\xd8\xf0qA\xc4\x95\x87/\xb5\xd8\xc0\xc6j\x8bm\xa5Vf>NF\x12\x05\xd8E\x80\xbe\xe5\xbc~'
    bitlen  = 511
    output  = 'hF\xa2\xf0'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_5():
    aes3gpp = AES_3GPP()
    key     = '\x83\xfd#\xa2D\xa7L\xf3X\xda0\x19\xf1r&5'
    count   = 0x36af6144
    bearer  = 0xf
    direct  = 1
    data    = '5\xc6\x87\x16c<f\xfbu\x0c&he\xd5<\x11\xea\x05\xb1\xe9\xfaI\xc89\x8dH\xe1\xef\xa5\x90\x9d9G\x90(7\xf5\xae\x96\xd5\xa0[\xc8\xd6\x1c\xa8\xdb\xef\x1b\x13\xa4\xb4\xab\xfeO\xb1\x00`E\xb6t\xbbTr\x93\x04\xc3\x82\xbeS\xa5\xaf\x05Uav\xf6\xea\xa2\xef\x1d\x05\xe4\xb0\x83\x18\x1e\xe6t\xcd\xa5\xa4\x85\xf7Mz'
    bitlen  = 768
    output  = '\xe6W\xe1\x82'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_6():
    aes3gpp = AES_3GPP()
    key     = 'h2\xa6\\\xffDsb\x1e\xbd\xd4\xba&\xa9!\xfe'
    count   = 0x36af6144
    bearer  = 0x18
    direct  = 0
    data    = '\xd3\xc589bh qwefv 287cb@\x98\x1b\xa6\x82L\x1b\xfb\x1a\xb4\x85G )\xb7\x1d\x80\x8c\xe3>,\xc3\xc0\xb5\xfc\x1f=\xe8\xa6\xdc'
    bitlen  = 383
    output  = '\xf0f\x8c\x1e'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_7():
    aes3gpp = AES_3GPP()
    key     = ']\n\x80\xd8\x13J\xe1\x96w\x82Kg\x1e\x83\x8a\xf4'
    count   = 0x7827fab2 
    bearer  = 0x5
    direct  = 1
    data    = "p\xde\xdf-\xc4,\\\xbd:\x96\xf8\xa0\xb1\x14\x18\xb3`\x8dW3`J,\xd3j\xab\xc7\x0c\xe3\x19;\xb5\x15;\xe2\xd3\xc0m\xfd\xb2\xd1n\x9c5qX\xbejA\xd6\xb8a\xe4\x91\xdb?\xbf\xebQ\x8e\xfc\xf0H\xd7\xd5\x89Ss\x0f\xf3\x0c\x9e\xc4p\xff\xcdf=\xc3B\x01\xc3j\xdd\xc0\x11\x1c5\xb3\x8a\xfe\xe7\xcf\xdbX.71\xf8\xb4\xba\xa8\xd1\xa8\x9c\x06\xe8\x11\x99\xa9qb'\xbe4N\xfc\xb46\xdd\xd0\xf0\x96\xc0d\xc3\xb5\xe2\xc3\x99\x99?\xc7s\x94\xf9\xe0\x97 \xa8\x11\x85\x0e\xf2;.\xe0]\x9eas`\x9d\x86\xe1\xc0\xc1\x8e\xa5\x1a\x01*\x00\xbbA;\x9c\xb8\x18\x8ap<\xd6\xba\xe3\x1c\xc6{4\xb1\xb0\x00\x19\xe6\xa2\xb2\xa6\x90\xf0&q\xfe|\x9e\xf8\xde\xc0\tNS7cG\x8dX\xd2\xc5\xf5\xb8'\xa0\x14\x8cYH\xa9i1\xac\xf8OFZd\xe6,\xe7@\x07\xe9\x91\xe3~\xa8#\xfa\x0f\xb2\x19#\xb7\x99\x05\xb73\xb61\xe6\xc7\xd6\x86\n81\xac5\x1a\x9cs\x0cR\xffr\xd9\xd3\x08\xee\xdb\xab!\xfd\xe1C\xa0\xea\x17\xe2>\xdc\x1ft\xcb\xb3c\x8a 3\xaa\xa1Td\xea\xa738]\xbb\xebo\xd75\t\xb8W\xe6\xa4\x19\xdc\xa1\xd8\x90z\xf9w\xfb\xacM\xfa5\xec"
    bitlen  = 2558
    output  = '\xf4\xcc\x8f\xa3'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_8():
    aes3gpp = AES_3GPP()
    key     = '\xb3\x12\x0f\xfd\xb2\xcfj\xf4\xe7>\xaf.\xf4\xeb\xeci'
    count   = 0x296f393c 
    bearer  = 0xb
    direct  = 1
    data = '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\xe0\x95\x80E\xf3\xa0\xbb\xa4\xe3\x96\x83F\xf0\xa3\xb8\xa7\xc0*\x01\x8a\xe6@vR&\xb9\x87\xc9\x13\xe6\xcb\xf0\x83W\x00\x16\xcf\x83\xef\xbca\xc0\x82Q>!V\x1aB|\x00\x9d(\xc2\x98\xef\xac\xe7\x8e\xd6\xd5l-E\x05\xad\x03.\x9c\x04\xdc`\xe7:\x81im\xa6e\xc6\xc4\x86\x03\xa5{E\xab3"\x15\x85\xe6\x8e\xe3\x16\x91\x87\xfb\x029R\x862\xddel\x80~\xa3$\x8b{F\xd0\x02\xb2\xb5\xc7E\x8e\xb8[\x9c\xe9Xy\xe04\x08Y\x05^;\n\xbb\xc3\xea\xce\x87\x19\xca\xa8\x02e\xc9r\x05\xd5\xdcK\xcc\x90/\xe1\x83\x96)\xedq2\x8a\x0f\x04I\xf5\x88U~h\x98\x86\x0e\x04*\xec\xd8K$\x04\xc2\x12\xc9"-\xa5\xbf\x8a\x89\xefg\x97\x87\x0c\xf5\x07q\xa6\x0ff\xa2\xeeb\x856W\xad\xdf\x04\xcd\xde\x07\xfaAN\x11\xf1+M\x81\xb9\xb4\xe8\xacS\x8e\xa3\x06fh\x8d\x88\x1fl4\x84!\x99/1\xb9O\x88\x06\xed\x8f\xcc\xffL\x91#\xb8\x96BRz\xd6\x13\xb1\t\xbfu\x16t\x85\xf1&\x8b\xf8\x84\xb4\xcd#\xd2\x9a\t4\x92W\x03\xd64\t\x8fwg\xf1\xbet\x91\xe7\x08\xa8\xbb\x94\x9a8sp\x8a\xefJ6#\x9eP\xcc\x08#\\\xd5\xedk\xbeW\x86h\xa1{X\xc1\x17\x1d\x0b\x90\xe8\x13\xa9\xe4\xf5\x8a\x89\xd7\x19\xb1\x10B\xd66\x0b\x1b\x0fR\xde\xb70\xa5\x8dX\xfa\xf4c\x15\x95K\n\x87&\x91GYw\xdc\x88\xc0\xd73\xfe\xffT`\n\x0c\xc1\xd00\n\xaa\xeb\x94W,n\x95\xb0\x1a\xe9\r\xe0O\x1d\xceG\xf8~\x8f\xa7\xbe\xbfw\xe1\xdb\xc2\rk\xa8\\\xb9\x14=Q\x8b(]\xfa\x04\xb6\x98\xbf\x0c\xf7\x81\x9f \xfaz(\x8e\xb0p=\x99\\Y\x94\x0c|f\xdeW\xa9\xb7\x0f\x827\x9bp\xe2\x03\x1eE\x0f\xcf\xd2\x18\x13&\xfc\xd2\x8d\x88#\xba\xaa\x80\xdfn\x0fD5Ydu9\xfd\x89\x07\xc0\xff\xd9\xd7\x9c\x13\x0e\xd8\x1c\x9a\xfd\x9b~\x84\x8c\x9f\xed8D=]8\x0eS\xfb\xdb\x8a\xc8\xc3\xd3\xf0hv\x05O\x12$a\x10}\xe9/\xea\t\xc6\xf6\x92:\x18\x8dS\xaf\xe5J\x10\xf6\x0en\x9dZ\x03\xd9\x96\xb5\xfb\xc8 \xf8\xa67\x11j\'\xad\x04\xb4D\xa0\x93-\xd6\x0f\xbd\x12g\x1c\x11\xe1\xc0\xecs\xe7\x89\x87\x9f\xaa=B\xc6M \xcd\x12Rt*7h\xc2Z\x90\x15\x85\x88\x8e\xce\xe1\xe6\x12\xd9\x93k@;\x07u\x94\x9af\xcd\xfd\x99\xa2\x9b\x13E\xba\xa8\xd9\xd5@\x0c\x91\x02K\n`sc\xb0\x13\xce]\xe9\xae\x86\x9d;\x8d\x95\xb0W\x0b<-9\x14"\xd3$P\xcb\xcf\xae\x96e"\x86\xe9m\xec\x12\x14\xa94e\'\x98\n\x81\x92\xea\xc1\xc3\x9a:\xafo\x155\x1d\xa6\xbevM\xf8\x97r\xec\x04\x07\xd0nD\x15\xbe\xfa\xe7\xc9%\x80\xdf\x9b\xf5\x07I|\x8f)\x95\x16\rN!\x8d\xaa\xcb\x02\x94J\xbf\x834\x0c\xe8\xbe\x16\x86\xa9`\xfa\xf9\x0e-\x90\xc5\\\xc6G[\xab\xc3\x17\x1a\x80\xa3c\x17IT\x95]q\x01\xda\xb1j\xe8\x17\x91g\xe2\x14D\xb4C\xa9\xea\xaa|\x91\xde6\xd1\x18\xc3\x9d8\x9f\x8d\xd4F\x9a\x84l\x9a&+\xf7\xfa\x18Hzy\xe8\xde\x11i\x9e\x0b\x8f\xdfU|\xb4\x87\x19\xd4S\xbaq0V\x10\x9b\x93\xa2\x18\xc8\x96u\xac\x19_\xb4\xfb\x06c\x9b7\x97\x14IU\xb3\xc92}\x1a\xec\x00=B\xec\xd0\xea\x98\xab\xf1\x9f\xfbJ\xf3V\x1ag\xe7|5\xbf\x15\xc5\x9c$\x12\xda\x88\x1d\xb0+\x1b\xfb\xce\xbf\xacQR\xbc\x99\xbc?\x1d\x15\xf7q\x00\x1bp)\xfe\xdb\x02\x8f\x8b\x85+\xc4@~\xb8?\x89\x1c\x9c\xa73%O\xdd\x1e\x9e\xdbV\x91\x9c\xe9\xfe\xa2\x1c\x17@rR\x1c\x181\x9aT\xb5\xd4\xef\xbe\xbd\xdf\x1d\x8bi\xb1\xcb\xf2_H\x9f\xcc\x98\x13rT|\xf4\x1d\x00\x8e\xf0\xbc\xa1\x92o\x93Ks^\t\x0b;%\x1e\xb3:6\xf8.\xd9\xb2\x9c\xf4\xcb\x94A\x88\xfa\x0e\x1e8\xddw\x8f}\x1c\x9d\x98{(\xd12\xdf\xb9s\x1f\xa4\xf4\xb4\x16\x93[\xe4\x9d\xe3\x05\x16\xaf5xX\x1f/\x13\xf5a\xc0f3a\x94\x1e\xab$\x9aK\xc1#\xf8\xd1\\\xd7\x11\xa9V\xa1\xbf \xfen\xb7\x8a\xea#s6\x1d\xa0Bly\xa50\xc3\xbb\x1d\xe0\xc9\x97"\xef\x1f\xde9\xac+\x00\xa0\xa8\xee|\x80\n\x08\xbc"d\xf8\x9fN\xff\xe6\'\xac/\x051\xfbUOm!\xd7LY\np\xad\xfa\xa3\x90\xbd\xfb\xb3\xd6\x8eF!\\\xab\x18}#h\xd5\xa7\x1f^\xbe\xc0\x81\xcd; \xc0\x82\xdb\xe4\xcd/\xac\xa2\x87sy]k\x0c\x10 Ke\x9a\x93\x9e\xf2\x9b\xbe\x10\x88$6$B\x99\'\xa7\xebWm\xd3\xa0\x0e\xa5\xe0\x1a\xf5\xd4u\x83\xb2\',\x0c\x16\x1a\x80e!\xa1o\xf9\xb0\xa7"\xc0\xcf&\xb0%\xd5\x83n"X\xa4\xf7\xd4w:\xc8\x01\xe4&;\xc2\x94\xf4=\xef\x7f\xa8p?:A\x97F5%\x88vR\xb0\xb2\xa4\xa2\xa7\xcf\x87\xf0\t\x14\x87\x1e%\x03\x91\x13\xc7\xe1a\x8d\xa3@d\xb5zC\xc4c$\x9f\xb8\xd0^\x0f&\xf4\xa6\xd8Ir\xe7\xa9\x05H$\x14_\x91)\\\xdb\xe3\x9ao\x92\x0f\xac\xc6Yq+F\xa5K\xa2\x95\xbb\xe6\xa9\x01T\xe9\x1b3\x98Z+\xcdB\n\xd5\xc6~\xc9\xad\x8e\xb7\xachd\xdb\'*Qk\xc9L(9\xb0\xa8\x16\x9ak\xf5\x8e\x1a\x0c*\xda\x8c\x88;{\xf4\x97\xa4\x91q&\x8e\xd1]\xdd)i8N\x7f\xf4\xbfJ\xab.\xc9\xec\xc6R\x9c\xf6)\xe2\xdf\x0f\x08\xa7ze\xaf\xa1*\xa9\xb5\x05\xdf\x8b(~\xf6\xcc\x91I=\x1c\xaa9\x07n(\xef\x1e\xa0(\xf5\x11\x8d\xe6\x1a\xe0+\xb6\xae\xfc3C\xa0P)/\x19\x9f@\x18W\xb2\xbe\xad^n\xe2\xa1\xf1\x91\x02/\x92x\x01o\x04w\x91\xa9\xd1\x8d\xa7\xd2\xa6\xd2\x7f.\x0eQ\xc2\xf6\xea0\xe8\xacI\xa0`OL\x13T.\x85\xb6\x83\x81\xb9\xfd\xcf\xa0\xceK-4\x13T\x85-6\x02E\xc56\xb6\x12\xafq\xf3\xe7|\x90\x95\xae-\xbd\xe5\x04\xb2es=\xab\xfe\x10\xa2\x0f\xc7\xd6\xd3,!\xcc\xc7+\x8b4D\xaef=e\x92-\x17\xf8,\xaa+\x86\\\xd8\x89\x13\xd2\x91\xa6X\x99\x02n\xa12\x849r<\x19\x8c6\xb0\xc3\xc8\xd0\x85\xbf\xaf\x8a2\x0f\xde3KJI\x19\xb4L+\x95\xf6\xe8\xec\xf73\x93\xf7\xf0\xd2\xa4\x0e`\xb1\xd4\x06Rk\x02-\xdc3\x18\x10\xb1\xa5\xf7\xc3G\xbdS\xed\x1f\x10]j\r0\xab\xa4w\xe1x\x88\x9a\xb2\xecU\xd5X\xde\xab&0 C6\x96+M\xb5\xb6c\xb6\x90+\x89\xe8[1\xbcj\xf5\x0f\xc5\n\xcc\xb3\xfb\x9bW\xb6c)p17\x8d\xb4x\x96\xd7\xfb\xafl`\n\xdd,g\xf96\xdb\x03y\x86\xdb\x85n\xb4\x9c\xf2\xdb?}\xa6\xd26P\xe48\xf1\x88@A\xb0\x13\x11\x9eL*\xe5\xaf7\xcc\xcd\xfbhf\x078\xb5\x8b<Y\xd1\xc0$\x847G*\xba\x1f5\xca\x1f\xb9\x0c\xd7\x14\xaa\x9fcU4\xf4\x9e|[\xba\x81\xc2\xb6\xb3o\xde\xe2\x1c\xa2~4\x7fy=,\xe9D\xed\xb2<\x8c\x9b\x91K\xe1\x035\xe3P\xfe\xb5\x07\x03\x94\xb7\xa4\xa1\\\x0c\xa1 (5h\xb7\xbf\xc2T\xfe\x83\x8b\x13z!G\xce|\x11::MeI\x9d\x9e\x86\xb8}\xbc\xc7\xf0;\xbd::\xb1\xaa$>\xce[\xa9\xbc\xf2_\x82\x83l\xfeG;-\x83\xe7\xa7 \x1c\xd0\xb9jrE\x1e\x86?l;\xa6d\xa6\xd0s\xd1\xf7\xb5\xed\x99\x08e\xd9x\xbd8\x15\xd0`\x94\xfc\x9a*\xbaR!\xc2-Z\xb9\x968\x9e7!\xe3\xaf_\x05\xbe\xdd\xc2\x87^\r\xfa\xeb9\x02\x1e\xe2zA\x18|\xbbE\xef@\xc3\xe7;\xc09\x89\xf9\xa3\r\x12\xc5K\xa7\xd2\x14\x1d\xa8\xa8uI>ewn\xf3_\x97\xde\xbc"\x86\xccJ\xf9\xb4b>\xee\x90/\x84\x0cR\xf1\xb8\xade\x899\xae\xf7\x1f?r\xb9\xec\x1d\xe2\x15\x88\xbd5HN\xa4D64?\xf9^\xadj\xb1\xd8\xaf\xb1\xb2\xa3\x03\xdf\x1bq\xe5<J\xeak.>\x93r\xbe\r\x1b\xc9\x97\x98\xb0\xce<\xc1\r*YmV]\xba\x82\xf8\x8c\xe4\xcf\xf3\xb3=]$\xe9\xc0\x83\x11$\xbf\x1a\xd5Ky%2\x98=\xd6\xc3\xa8\xb7\xd0'
    bitlen  = 16448
    output  = '\xeb\xd5\xcc\xb0'
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_9():
    aes3gpp = AES_3GPP()
    key     = '5ead1f52e92ced3add9486d1b066c693'.decode('hex')
    count   = 0x00
    bearer  = 0x00
    direct  = 0
    data = '0010101010'.decode('hex')
    bitlen  = 40
    output  = 'c76c5132'.decode('hex')
    return aes3gpp.EIA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_10():
    aes3gpp = AES_3GPP()
    key     = '941c08ca34df130ee7644ef803b90eda'.decode('hex')
    count   = 0x00
    bearer  = 0x00
    direct  = 0
    data = '10101010c76c5132'.decode('hex')
    bitlen  = 64
    output  = 'ad1d7e855d13fbd6'.decode('hex')
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_11():
    aes3gpp = AES_3GPP()
    key     = '941c08ca34df130ee7644ef803b90eda'.decode('hex')
    count   = 0x00
    bearer  = 0x00
    direct  = 0
    data = 'ad1d7e855d13fbd6'.decode('hex')
    bitlen  = 64
    output  = '10101010c76c5132'.decode('hex')
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_11():
    aes3gpp = AES_3GPP()
    key     = 'a24fd61d0b627b91f7451be11df4d40e'.decode('hex')
    count   = 0x1C3
    bearer  = 0x00
    direct  = 1
    data = '45e0003c4cce00003d014091ac144077ac1456e2'.decode('hex')
    bitlen  = 160
    output  = 'ee1cae4f34904f46515bc173562021c64afe08fc'.decode('hex')
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen) == output

def aes_EIA2_testset_12():
    aes3gpp = AES_3GPP()
    key     = 'a24fd61d0b627b91f7451be11df4d40e'.decode('hex')
    count   = 0x1C3
    bearer  = 0x00
    direct  = 1
    data = 'ee1cae4f34904f46515bc173562021c64afe08fc'.decode('hex')
    bitlen  = 160
    #output  = '45e0003c4cce00003d014091ac144077ac1456e2'.decode('hex')
    output  = '45e0003c4cce00003d014091ac144077ac1456e2'
    return aes3gpp.EEA2(key, count, bearer, direct, data, bitlen).encode('hex') == output

def aes_testsets():

    return aes_EEA2_testset_1() & aes_EEA2_testset_2() & \
            aes_EEA2_testset_3() & aes_EEA2_testset_4() & \
            aes_EEA2_testset_5() & aes_EEA2_testset_6() & \
            aes_EIA2_testset_1() & aes_EIA2_testset_2() & \
            aes_EIA2_testset_3() & aes_EIA2_testset_4() & \
            aes_EIA2_testset_5() & aes_EIA2_testset_6() & \
            aes_EIA2_testset_7() & aes_EIA2_testset_8() & \
            aes_EIA2_testset_9()& aes_EIA2_testset_10() & \
            aes_EIA2_testset_11()& aes_EIA2_testset_12()

###
###
def testall():
    return aes_testsets()

def testperf():
    a = None
    T0 = time()
    for i in range(1000):
        a = testall()
    print('1000 full testsets in %.3f seconds' % (time()-T0, ))



# print len(bytearray.fromhex('5ead1f52e92ced3add9486d1b066c693'))
#
# print len('5ead1f52e92ced3add9486d1b066c693'.decode('hex'))
# print ('941c08ca34df130ee7644ef803b90eda'.decode('hex'))
#
# import binasciiz
#print len(binascii.b2a_base64(binascii.unhexlify('5ead1f52e92ced3add9486d1b066c693')))
# print binascii.b2a_base64(binascii.unhexlify('941c08ca34df130ee7644ef803b90eda'))


print(aes_testsets())
