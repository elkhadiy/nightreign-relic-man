# Nightreign relic managment

## Usage

Quick and dirty interface for testing base functionality.

Still undecided for the best method to know when we finished scraping all relics so for now I just hardcode the number of relics I expect in `collect_relic_screenshots()` and store the screenshots in a `relics` directory created in the current working directory.

The "Inventory" database is just a yaml file that pops up in the current directory also.

```shell
$ collect-relic-screenshots
$ build-inventory
```

## Roadmap
- Scraping player's inventory state from the game: relics, available vessels
- Best fit search algorithm for each character or desired "build"
- Nice GUI with simple string search function
- Relic autosale, automate gamba