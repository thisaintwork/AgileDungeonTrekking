Feature: Naming a character

  Agile Dungeon Trekking is a website that allows players to create Dungeons & Dragon characters.
  A player can choose to name their character or randomly generate one.

  Rule: Players can create a character

    Scenario: Player creates a new character
        Given Player navigates to Website "http://agiledungeontrekking.online/login"
        When Player enters valid credentials
            | username | password |
            | adt_user1 | adt_password123 |
        When Player creates a new character
        Then Player can enter a name for the new character
        Then the character has a name
