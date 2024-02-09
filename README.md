This is the first go at the metadata checker. It checks which pieces of metadata are missing, automatically fills in what it can, and allows the user to manually change what it can't. The parameters for auto-filling are as follows:
- track number: pulls from beginning of filename
- track title: pulls from filename, fixes capitalization and spacing
- artist/albumartist: assumes equality between the two
- total tracks: checks rest of songs with same album
