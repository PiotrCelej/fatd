"""Unit tests for the tiles module."""

import unittest
import tiles


class TestTilesModule(unittest.TestCase):
    """Test cases for the tiles module."""

    def test_tiles_list_exists(self):
        """Test that tiles list exists and is not empty."""
        self.assertTrue(hasattr(tiles, 'tiles'), "Module should have tiles list")
        self.assertIsInstance(tiles.tiles, list, "tiles should be a list")
        self.assertGreater(len(tiles.tiles), 0, "tiles list should not be empty")

    def test_tiles_contains_strings(self):
        """Test that all tiles are strings."""
        for i, tile in enumerate(tiles.tiles):
            self.assertIsInstance(tile, str, f"Tile {i} should be a string")

    def test_tiles_contain_corridors(self):
        """Test that tiles contain valid corridor layouts."""
        for i, tile in enumerate(tiles.tiles):
            self.assertIn('\n', tile, f"Tile {i} should contain newline characters")
            # Check for expected characters
            valid_chars = {'X', ' ', '\n'}
            for char in tile:
                self.assertIn(char, valid_chars, 
                            f"Tile {i} contains invalid character: {repr(char)}")

    def test_rooms_list_exists(self):
        """Test that rooms list exists and is not empty."""
        self.assertTrue(hasattr(tiles, 'rooms'), "Module should have rooms list")
        self.assertIsInstance(tiles.rooms, list, "rooms should be a list")
        self.assertGreater(len(tiles.rooms), 0, "rooms list should not be empty")

    def test_rooms_contains_strings(self):
        """Test that all rooms are strings."""
        for i, room in enumerate(tiles.rooms):
            self.assertIsInstance(room, str, f"Room {i} should be a string")

    def test_rooms_have_valid_structure(self):
        """Test that rooms have valid structure."""
        for i, room in enumerate(tiles.rooms):
            self.assertIn('\n', room, f"Room {i} should contain newline characters")
            lines = room.strip('\n').split('\n')
            self.assertGreater(len(lines), 0, f"Room {i} should have content")
            # All lines should have same length
            if len(lines) > 1:
                first_len = len(lines[0])
                for j, line in enumerate(lines[1:], 1):
                    self.assertEqual(len(line), first_len, 
                                   f"Room {i} line {j} has different length")

    def test_entrances_list_exists(self):
        """Test that entrances list exists and is not empty."""
        self.assertTrue(hasattr(tiles, 'entrances'), "Module should have entrances list")
        self.assertIsInstance(tiles.entrances, list, "entrances should be a list")
        self.assertGreater(len(tiles.entrances), 0, "entrances list should not be empty")

    def test_entrances_contains_strings(self):
        """Test that all entrances are strings."""
        for i, entrance in enumerate(tiles.entrances):
            self.assertIsInstance(entrance, str, f"Entrance {i} should be a string")

    def test_entrances_have_valid_structure(self):
        """Test that entrances have valid structure."""
        for i, entrance in enumerate(tiles.entrances):
            self.assertIn('\n', entrance, f"Entrance {i} should contain newline characters")
            # Entrances should be smaller than rooms/tiles
            self.assertLess(len(entrance), 200, 
                          f"Entrance {i} seems too large for an entrance")

    def test_all_tiles_use_valid_characters(self):
        """Test that all tile collections use only valid characters."""
        valid_chars = {'X', ' ', '\n'}
        
        for collection_name in ['tiles', 'rooms', 'entrances']:
            collection = getattr(tiles, collection_name)
            for i, item in enumerate(collection):
                for char in item:
                    self.assertIn(char, valid_chars,
                                f"{collection_name}[{i}] contains invalid character: {repr(char)}")

    def test_tiles_are_nonempty_strings(self):
        """Test that no tiles are empty strings."""
        for collection_name in ['tiles', 'rooms', 'entrances']:
            collection = getattr(tiles, collection_name)
            for i, item in enumerate(collection):
                self.assertGreater(len(item), 0, 
                                 f"{collection_name}[{i}] should not be empty")

    def test_rooms_contain_enclosed_spaces(self):
        """Test that rooms appear to have enclosed spaces (basic validation)."""
        for i, room in enumerate(tiles.rooms):
            # Rooms should have both X (walls) and spaces (interior)
            self.assertIn('X', room, f"Room {i} should contain walls (X)")
            self.assertIn(' ', room, f"Room {i} should contain spaces")

    def test_entrances_smaller_than_rooms(self):
        """Test that entrances are generally smaller than rooms."""
        avg_room_size = sum(len(room) for room in tiles.rooms) / len(tiles.rooms)
        avg_entrance_size = sum(len(entrance) for entrance in tiles.entrances) / len(tiles.entrances)
        self.assertLess(avg_entrance_size, avg_room_size,
                       "Entrances should be smaller than rooms on average")


if __name__ == '__main__':
    unittest.main()
