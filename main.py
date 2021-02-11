from test.test_crawler import main, parse_args


def test_crawler():
    """Test crawler

    Ejemplo recorrido en anchura:
        python main.py --name prueba --sec 10 --mx 50
    """
    main(parse_args())


if __name__ == '__main__':
    test_crawler()
