import sys
from collections import namedtuple
from mocks import ui

#mock pythonista ui package
sys.modules['ui'] = ui
from src.scripts.Three_Column_Sortable_TableView import MyTableView

import pytest


def test_Name():
    toto = MyTableView()
    toto.btn_action(namedtuple('Sender', ['name', 'background_color'])('Name', 3))


def test_Size():
    toto = MyTableView()
    with pytest.raises(TypeError):
        toto.btn_action(namedtuple('Sender', ['name', 'background_color'])('Size', 3))


def test_Daten():
    toto = MyTableView()
    toto.btn_action(namedtuple('Sender', ['name', 'background_color'])('Date', 3))
