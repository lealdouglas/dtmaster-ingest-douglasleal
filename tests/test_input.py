import re

from pytest import raises

from dtmaster_ingest_douglasleal.input import input


def test_dev_funcionar():

    # System.setProperty('hadoop.home.dir', 'd:\\winutil\\')
    path = '/origem/arquivo.cs'
    result = input(path)
    assert result


def test_deve_retormar_nao_pode_vazio():

    path = ''
    msg_erro = 'path is required'
    with raises(ValueError, match=re.escape(msg_erro)):
        input(path)
