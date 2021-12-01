"""Vastuussa tietokannan toiminnoista
"""

import sqlite3
import os
from entities.readingtip import ReadingTip
from repositories.db_connection import get_connection

class DatabaseInterface:
    """Luokka joka vastaa tietokannasta
    """
    def __init__(self):
        """Luokan konstrukstori
        """
        self._db = get_connection("readingtips.db")

    def add(self, reading_tip: ReadingTip):
        """Ottaa ReadingTip-olion, lisää tietokantaan
        """
        self._db.execute("INSERT INTO readingtips (description) VALUES (?)", [reading_tip.description])

    def read(self):
        """Palauttaa listan reading_tip-olioita
        """
        sql = "SELECT * FROM readingtips"
        return [ReadingTip(reading_tip[1]) for reading_tip in self._db.execute(sql).fetchall()]

    def remove_tip(self, index: int):
        """Poistaa yhden lukuvinkin näkyvistä
        """
        self._db.execute("UPDATE readingtips SET visible = 0 WHERE id = (?)", [index])
