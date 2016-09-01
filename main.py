import re
import os


search_pattern = "(server)([\ \t]+)(\W+)([\ \t]+)(?P<ip>\d+\.\d+\.\d+\.\d+\.):(?P<port>\d+)([\ \t]+)(maxconn)([\ \t])(\d+)([\ \t]+)"
def extract():
    file = os.path.join(os.path.realpath("."), "files", "haproxy.cfg")
    with open(file, "r") as f:
        text = f.readlines()
    print("Found:\n")
    print(text)
    return text


def run():
    text = extract()
    print(type(text))
    print("Creating str of list")
    text = "".join(text)
    result = re.search("server", text)
    print(result)


run()
