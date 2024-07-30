# NaheulbeukGameMaster

Anything that might make the GMs life easier! No knowledge of programming required.

This code is designed to act as a helper for the Game Master (GM) in streamlining the proceedings of a roleplaying session for example by making combat more fluid and in preparing the next Naheulbeuk roleplaying session.

## Prerequisite

Be able to run interactive Python notebooks (.ipynb). Don't worry, the goal is that no knowledge of programming is needed.

## Strategy

This was initially made for personal use, however I am no longer acting as GM for Naheulbeuk currently. My plan is therefore to continue working on this as a showcase of my skills to portray on my personal CV, so I will be changing everything to English even though Naheulbeuk is in french initially as was reflected by initial code output. I am however, **open to requests**, if someone someday wants to use this code, I am willing to rework my priorities, and don't worry I plan to add French translation for the User Guide and eventually when I get to making a graphical interface, it will be available in both English and French.

Nevertheless, <http://www.naheulbeuk.com/> contains all the rules and regulations for the game. Any GM who knows the rules should in theory understand how to use the program by following prompts written in the .ipynb notebooks.

## Files and Folders

- "Documentation" - Will contain User Guide
- "Fights" - Character creation and Combat sequence
- "Test" unit testing - framework yet to be determined
- example_* files - Example use PDFs of .ipynb notebooks

## First Time Setup (How to make repo usable)

1. Make a folder Fights/save\_file
2. Run notebook (.ipynb) in Fights/resources once to generate .json files
3. Start Fights/fights.ipynb and follow indications

TO-DO: Split Fights and NPC.py into Characters and Combat to match new User Guide
TO-DO: make User Guide for Characters and Combat
TO-DO: Add install.sh and/or install.bat that does steps 1 and 2
TO-DO: Make installation completely portable (currently relies on Python and Jupyter Notebook to be installed)

## Character Creation

Coming soon.

## Combat ("Fights" folder)

Fights can take a long time, especially when there are a lots of NPC (Non-Playable Character) enemies the GM has to manage. Players are kept waiting for GM dice rolls to figure out what's going to happen. That interrupts combat flow. "Fights" aim to streamline this process. Instead of rolling the dice, determining the outcome by looking at charts, checking for critical hit, what's the exact critical hit, how much resistance does the enemy have, do they take damage, does the weapon break, how does it break, etc. "Fights" is going to be such that only the enemies need to be configured once (even days before the actual fight in a .txt file), and during combat only hits that players land on the enemy need to be input; and everything else is just a matter of clicking a button to get the outcome during defense. During NPC attack turns, the only one click ensures to get the attack outcome of the whole NPC party however many NPCs are in play. This saves the GM great amount of time and helps to keep player engagement as the GM is left to be more interactive in their turn to control NPCs.  

### Somewhere in the very very far future

(this depends on my free time)

- Extend Python code to more than just fights (Character Creation and Combat)
- Make installation portable (no longer dependent in Python and Jupyter Notebook local installations)
- Add Graphical User Interface (GUI). This will also remove the Jupyter Notebook prerequisite or make it optional as the user (GM) will be able to just run a software and interact with the GUI. but in what, Qt cause C++?
- Potentially grid-based placement for fights
