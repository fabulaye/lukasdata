import regex as re

def sanitize_input(string):
    new_string=re.sub("[!}{&#$%;']","",string)
    return new_string