from urllib import request
import json

def get_zen_text():
    content = request.urlopen("https://zentexts.org/quip.json").read()

    return json.loads(content).get("quip")


def main():
    f = open("zentext.txt", "w+")

    seen = set() # holds zen texts already seen
    for i in range (2000):
        zentext = get_zen_text()

        if zentext not in seen: # not a duplicate
            line = zentext + "\n \n"
            print(line)
            f.write(line)
            seen.add(zentext)

    f.close()


if __name__ == "__main__":
    main()