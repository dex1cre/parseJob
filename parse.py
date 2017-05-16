from bs4 import BeautifulSoup as bfs
import urllib.request
import config

def get_html(url):
    html = urllib.request.urlopen(url)
    return html.read()

def parse(html, ht=""):
    sp = bfs(html, "html5lib")
    lst = sp.find('ul', class_="content-list_tasks")
    li = lst.findAll('li', class_="content-list__item")

    data = []
    k = 0
    for i in li:
        k += 1
        print("Get task number --> ", k)
        try:
            a = i.find('div', class_="task__title").find('a')

            title = a.text
            if ht == "" or ht not in  title:
                print("Not to result")
                continue
            a_href = a.attrs["href"]
            tags_b = i.find('ul', class_='tags tags_short').findAll('li', class_="tags__item")
            tags = []
            for j in tags_b:
                tag = j.find('a', class_="tags__item_link").text
                tags.append(tag)
        except:
            print("Error to parse")
        else:

            #Выполняем дополнительный запрос для получения описания задания
            sp2 = bfs(get_html(config.url + str(a_href)), "html5lib")
            description = sp2.find('div', class_='task__description').text
            for i in ["<br>", "<p>", "</p>", "<li>", "</li>"]:
                description = description.replace(i, "")
            data.append([title, description, tags, a_href])
    return data


def main():
    print(parse(get_html(config.url)))

if __name__ == "__main__":
    main()
