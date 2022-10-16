# NaheulbeukGameMaster
Anything that might make the GMs life easier!

As it's for personal use, code will come first, then when it's "finished" the User Guide (UG) will come.
Nevertheless, http://www.naheulbeuk.com/ contains all the rules and regulations for the game. Any GM who knows the rules (and some programming) should in theory understand how to use the code without a UG. UG will probably end up being heavily inspired or a direct translation of the rulebook.

Files and Folders:
"Test" unit testing - format yet to be fixed
"User Guide" - Will contain User Guides (1 chapter per .ipynb notebook)
example_* files - Example use PDFs of .ipynb notebooks
Finally, 1 folder per chapter of UG (Fights, ...)

## Fights
Fights can take a long time, especially when there are a lots of enemies, players are kept waiting for dice rolls to figure out what's going to happen. That interrupts flow. "Fights" aim to streamline this process. Instead of rolling the dice, determining the outcome, looking at charts, what's the critical hit, how much resistance does the enemy have, does the weapon break, how does it break, etc. "Fights" is going to be such that only the enemies need to be configured (separate files per encounter prepared beforehand), and hits that players land on the enemy to be input when hit is taken; and everything else is just a matter on changing maybe the name of the enemy concerned and running the block to get the outcome.

### Somewhere in the very very far future
(this depends on my free time and my players willingness to continue the game)
- Extend Python code to more than just fights
- When Python covers most of the rulebook and nothing can be made easier with some code, Port to C++
- Graphical User Interface in C++
- Potentially grid-based placement for fights
