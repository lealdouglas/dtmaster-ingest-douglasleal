import os

from dtmaster_ingest_douglasleal.input import input


def test_input_dev_funcionar():

    # System.setProperty('hadoop.home.dir', 'd:\\winutil\\')

    path = '/origem/arquivo.cs'

    result = input(path)

    assert result
