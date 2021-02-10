from crawler.crawler import Crawler, normalize_link
import argparse


def main(args):
    """Main

    Funcion que procesa los argumentos de consola y dependiendo
    de si estan todos o falta alguno saca un menu por consola
    preguntando por los argumentos que faltan.

    Params: args, objeto parser.parse_args()
    """
    list_url = args.file
    seconds = args.sec
    max_downloads = args.mx
    recorrido = ""
    name = args.name
    if args.a:
        recorrido = "a"
    if args.p:
        recorrido = "p"
    opt = menu(seconds, max_downloads, recorrido)
    print("Starting Crawler:")
    print("")
    scan(list_url, opt[0], opt[1], opt[2], name)


def scan(list_url, seconds, max_downloads, recorrido, name):
    """Scan

    Funcion que crea un objeto Crawler y le manda
    escanear con el tipo de recorrido que se le ha
    mandado.

    Params:
        list_url, fichero con las urls
        seconds, int con el numero de segundos
        max_downloads, int con el numero de max_downloads
        recorrido, str con valor "a" para anchura o "p" para profundidad
        name, nombre del crawler
    """
    crw = Crawler(max_downloads, seconds, name)
    ax = parse_txt(list_url)
    links = []
    for i in ax:
        links.append(normalize_link(i, i))

    if recorrido == "p":
        for link in links:
            crw.scan_p(link, link)
    else:
        crw.scan_a(links, max_downloads, links[0], links[0])


def parse_txt(txt):
    """Parse_txt

    Funcion que parsea el archivo con las
    urls y devuelve una lista con ellas

    Params:
        txt, fichero con las urls
    """
    links = []
    for line in open(txt, 'r'):
        if not line[0].startswith("#"):
            links.append(line.rstrip("\n\r"))
    return links


def parse_args():
    """Parse_args

    Funcion que parsea los argumentos de consola
    """
    parser = argparse.ArgumentParser(description='WebCrawler')
    parser.add_argument("--file", help="Starting point. Default point:links.txt", type=str, default="links.txt")
    parser.add_argument("--name", help="Name of the crawler Default:payacrawler", type=str, default="payacrawler")
    parser.add_argument("--sec", help="Number of seconds", type=int)
    parser.add_argument("--mx", help="The max downloads", type=int)
    parser.add_argument("-a", help="Type of seed exploration: Width (a)", action="store_true")
    parser.add_argument("-p", help="Type of seed exploration: Depth (p)", action="store_true")
    args = parser.parse_args()
    return args


def menu(seconds, max_downloads, recorrido):
    """Menu

    Funcion que muestra un menu para obtener los
    argumentos que no se han pasado por consola previamente

    Params:
        seconds, int con el numero de segundos
        max_downloads, int con el numero de max_downloads
        recorrido, str con valor "a" para anchura o "p" para profundidad
    """
    print("Web Crawler test")
    print("===================================================================")

    if seconds != -1:
        while seconds <= 0:
            try:
                seconds = input("-> Insert the number of seconds:")
                seconds = int(seconds)
            except ValueError:
                seconds = -1
                print("Error: The seconds must be >= 0")

    if max_downloads != -1:
        while max_downloads <= 0:
            try:
                max_downloads = input("-> Insert the max downloads:")
                max_downloads = int(max_downloads)
            except ValueError:
                max_downloads = -1
                print("Error: The max downloads must be > 0")

    if recorrido == "":
        recorrido = input("->Type of seed exploration: Width (a) / Depth (p):")
        while recorrido != "a" and recorrido != "p":
            print("Error: Must be (a) for Width or (p) for Depth")
            recorrido = input("->Type of seed exploration: Width (a) / Depth (p):")

    return seconds, max_downloads, recorrido
