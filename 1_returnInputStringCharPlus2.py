#!/usr/bin/env python
'''translate encoded string. char_of_alphabet -> char_of_alphabet_+2'''

from string import ascii_lowercase, maketrans, translate


input_text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def solution_1(text):
    #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = list(ascii_lowercase)

    input_chars = list(text)
    input_chars_translated = []

    for char in input_chars:
        print "char = %c" % char
        if char in ascii_lowercase:
            c_index = alphabet.index(char)
            print c_index
            input_chars_translated.append(alphabet[(alphabet.index(char) + 2) % (len(alphabet))])
        else:
            input_chars_translated.append(char)
        
    return ''.join(input_chars_translated)
    

def solution_2(text):
    intab = ascii_lowercase
    outtab = "%s%s" % (ascii_lowercase[2:], ascii_lowercase[:2])

    translation = maketrans(intab, outtab)
    return text.translate(translation)
    
    
print solution_2(input_text)