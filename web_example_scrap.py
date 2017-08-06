import bs4 as bs
import urllib.request as ulreq

def main(vocab_input):
    dest_url = r"http://youdao.com/w/" + vocab_input + r"#keyfrom=dict2.top"
    sauce = ulreq.urlopen(dest_url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    with open(r"webpage", "w") as file:
        file.write(str(soup))
if __name__ == "__main__":
    main("abandon")
