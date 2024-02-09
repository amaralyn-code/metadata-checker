AL METADATA CHECKER
A simple metadata checker! Automatically checks for missing metadata, fills in what it can, and allows the user to manually fill in what it can't. Allows the user to select which metadata traits are important to them before hand.
Autofilling works as follows:
- track number: pulls from beginning of filename
- track title: pulls from filename, fixes capitalization and spacing
- artist/albumartist: assumes equality between the two
- total tracks: checks rest of songs with same album
