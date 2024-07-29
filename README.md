# NaheulbeukGameMaster
Anything that might make the GMs life easier!

As it's for personal use, code will come first, then when it's "finished" the User Guide (UG) will come.
Nevertheless, http://www.naheulbeuk.com/ contains all the rules and regulations for the game. Any GM who knows the rules (and some programming) should in theory understand how to use the code without a UG. UG will probably end up being heavily inspired or a direct translation of the rulebook.

Files and Folders:
- "Test" unit testing - framework yet to be determined
- "User Guide" - Will contain User Guide
- example_* files - Example use PDFs of .ipynb notebooks

## Prerequisite
Be able to run interactive Python notebooks (.ipynb)

## How to make repo usable (first time setup)
1. Make a folder Fights/save\_file
2. Run notebook (.ipynb) in Fights/resources to generate .json files
3. Start Fights/fights.ipynb and follow indications

TODO: Add proper instructions
TODO: Add install.sh that does steps 1 and 2

## Fights
Fights can take a long time, especially when there are a lots of enemies. Players are kept waiting for dice rolls to figure out what's going to happen. That interrupts combat flow. "Fights" aim to streamline this process. Instead of rolling the dice and determining the outcome by looking at charts, checking for critical hit, what's the exact critical hit, how much resistance does the enemy have, does the weapon break, how does it break, etc. "Fights" is going to be such that only the enemies need to be configured once (even days before the actual fight in a .txt file), and during combat only hits that players land on the enemy need to be input; and everything else is just a matter of running the block to get the outcome during defense. During NPC (Non-Playable Character) attack turns, the block only needs to be run once to get the attack outcome of the whole NPC party. 

### Somewhere in the very very far future
(this depends on my free time and the players willingness to continue the game (they aren't willing to continue with Naheulbeuk anymore so updates will severely slow down and recent lack of updates))
- Extend Python code to more than just fights
- When Python covers most of the rulebook and nothing can be made easier with some code, Port to C++
- Graphical User Interface (in C++?)
- Potentially grid-based placement for fights
