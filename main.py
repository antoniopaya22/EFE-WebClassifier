from crawler.crawler import Crawler
from exporters.excel_exporter import export_excel
from classificator.classificator import classify_all_pages
import bag_of_words.bag_of_words as bow
import words_correlation.words_correlation as wc
import argparse


def parse_args():
    """Parse_args

    Funcion que parsea los argumentos de consola
    """
    parser = argparse.ArgumentParser(description='WebCrawler')
    parser.add_argument("--url", help="Starting point", type=str, default="https://www.pudseycomputers.co.uk/")
    parser.add_argument("--name", help="Name of the crawler Default:payacrawler", type=str, default="payacrawler")
    parser.add_argument("--sec", help="Number of seconds", type=int)
    parser.add_argument("--mx", help="The max downloads", type=int)
    args = parser.parse_args()
    return args


def main(args):
    """Main

    Params: args, objeto parser.parse_args()
    """
    seconds = args.sec
    max_downloads = args.mx
    name = args.name
    url = args.url
    print("======> Starting Crawler")
    print("")
    crw = Crawler(max_downloads, seconds, name)
    crw.scan([url], max_downloads, url, url)
    print("======> Starting Bag Of Words")
    keywords = bow.main(crw.all_urls)
    print("======> Starting Word Correlation")
    corr_matrix = wc.main(keywords)
    print("======> Starting Classificator")
    categories = classify_all_pages(keywords)
    export_excel(corr_matrix, keywords, categories)


if __name__ == '__main__':
    main(parse_args())
