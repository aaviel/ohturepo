import unittest
from statistics_service import StatisticsService
from player import Player

# testejä varten korvataan netistä haettava pelaajalista kovakoodatulla datalla
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.statisticsService = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_luo_pelaajalistan(self):
        self.assertEqual(len(self.statisticsService._players), 5)

    def test_pelaajalistasta_haku_toimii(self):
        pelaaja = self.statisticsService.search("Kurri")

        self.assertEqual(pelaaja.name, "Kurri")
        self.assertEqual(pelaaja.team, "EDM")
        self.assertEqual(pelaaja.goals, 37)
        self.assertEqual(pelaaja.assists, 53)
        self.assertEqual(pelaaja.points, pelaaja.goals + pelaaja.assists)

        pelaaja = self.statisticsService.search ("Koivu")

        self.assertEqual(pelaaja, None)

    def test_joukkueen_haku_toimii(self):
        joukkue = self.statisticsService.team("EDM")

        self.assertEqual(len(joukkue), 3)
        self.assertEqual(str(joukkue[0].name), "Semenko")
        self.assertEqual(str(joukkue[1].name), "Kurri")
        self.assertEqual(str(joukkue[2].name), "Gretzky")

        self.assertEqual(str(self.statisticsService._players[0]), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(str(self.statisticsService._players[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(str(self.statisticsService._players[2]), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(str(self.statisticsService._players[3]), "Yzerman DET 42 + 56 = 98")
        self.assertEqual(str(self.statisticsService._players[4]), "Gretzky EDM 35 + 89 = 124")

    def test_top(self):
        toplista = self.statisticsService.top(2)

        self.assertEqual(str(toplista[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(toplista[1]), "Lemieux PIT 45 + 54 = 99")

"""
class StatisticsService:
    def __init__(self, playerReader):
        reader = playerReader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
"""
