from test.test_crawler import main, parse_args


def test_crawler():
    """Test crawler

    Ejemplo recorrido en profundidad:
        python main.py --file links.txt --name prueba --sec 100 --mx 50 -p
    Ejemplo recorrido en anchura:
        python main.py --file links.txt --name prueba --sec 100 --mx 50 -a
    """
    main(parse_args())


if __name__ == '__main__':
    test_crawler()
