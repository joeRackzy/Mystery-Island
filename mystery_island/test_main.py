
import unittest
from unittest.mock import patch

import main


class TestMysteryIsland(unittest.TestCase):

    def test_create_player(self):
        player = main.create_player("John")

        self.assertEqual(player["name"], "John")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["inventory"], [])

    @patch("main.random.randint", return_value=15)
    def test_raining_at_15_degrees(self, mock_temperature):
        player = main.create_player("John")

        main.update_weather(player)

        self.assertTrue(player["raining"])

    @patch("main.random.randint", return_value=20)
    def test_no_rain_at_20_degrees(self, mock_temperature):
        player = main.create_player("John")

        main.update_weather(player)

        self.assertFalse(player["raining"])

    def test_beach_connections(self):
        locations = main.get_available_locations("Beach")

        self.assertEqual(locations, ["Jungle"])

    @patch("builtins.input", return_value="yes")
    def test_collect_rope(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Jungle"

        main.collect_object(player)

        self.assertIn("Rope", player["inventory"])

    @patch("builtins.input", return_value="yes")
    def test_cannot_collect_rope_twice(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Jungle"

        main.collect_object(player)
        main.collect_object(player)

        self.assertEqual(player["inventory"].count("Rope"), 1)

    def test_cannot_move_during_rain(self):
        player = main.create_player("John")
        player["raining"] = True

        main.move_player(player)

        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    @patch("builtins.input", return_value="yes")
    def test_restore_lighthouse(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Lighthouse"
        player["inventory"].append("Lantern")

        result = main.restore_lighthouse(player)

        self.assertTrue(result)
    @patch("builtins.input", return_value="1")
    def test_movement_reduces_energy(self, mock_input):
        player = main.create_player("John")

        player["raining"] = False

        main.move_player(player)

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)
    @patch("builtins.input", return_value="2")
    def test_cannot_cross_bridge_without_rope(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Cave"

        main.move_player(player)

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5) 
    @patch("builtins.input", return_value="yes")
    def test_cannot_restore_without_lantern(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Lighthouse"

        result = main.restore_lighthouse(player)

        self.assertFalse(result)

    @patch("builtins.input", return_value="1")
    def test_energy_never_goes_below_zero(self, mock_input):
        player = main.create_player("John")
        player["location"] = "Jungle"
        player["inventory"].append("Rope")
        player["energy"] = 1

        main.move_player(player)

        self.assertEqual(player["energy"], 0)  

    @patch("builtins.input", return_value="0")
    def test_cancel_movement_keeps_energy(self, mock_input):
        player = main.create_player("John")

        main.move_player(player)

        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)    



if __name__ == "__main__":
    unittest.main()        


