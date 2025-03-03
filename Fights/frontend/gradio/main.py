import gradio as gr

# To-Do : have an environment file for gradio specifically
import sys, os
backend_path = os.path.join(os.path.dirname(__file__), "..", "..", "backend")
sys.path.append(os.path.abspath(backend_path))
from NPC import enemy

# To-Do : move to interface
import glob
def process_file(filename):
    # Check and prepare file for loading saved encounter
    if filename in ["saved_encounter", "save_file"]:
        filename = "current_save"
        relative_path = "save_file/"
        states = glob.glob(relative_path+'saved_*')
        states = [s[len(relative_path):] for s in states]
        
        compiled_save = str(len(states)) + " (NAME, AT, PRD, EV, PR, WEAPON, DMG_DICE_N, DMG_BONUS, COU, EXP)"
        for save in states:
            with open(relative_path+save, 'r') as file:
                compiled_save += "\n" + file.readline()
    
        with open(filename, 'w') as file:
            file.write(compiled_save)
        
    # Create list of enemies
    enemies = []

    with open(filename, 'r') as file:
        x = file.readline().split();
        try:
            nb_enemies = int(x[0])
        except ValueError:
            print("First line should be number of enemies followed by legend.")
    
        for i in range(nb_enemies):
            # Read enemy (1 line per enemy)
            NAME, AT, PRD, EV, PR, WEAPON, DMG_DICE_N, DMG_BONUS, COU, EXP = file.readline().split();
            # Convert specific variables to int for further use
            AT, PRD, EV, PR, DMG_DICE_N, DMG_BONUS, COU, EXP = \
                int(AT), int(PRD), int(EV), int(PR), int(DMG_DICE_N), int(DMG_BONUS), int(COU), int(EXP)
            # Create enemy instance
            myVars = vars()
            myVars[NAME] = enemy(NAME, AT, PRD, EV, PR, WEAPON, DMG_DICE_N, DMG_BONUS, COU, EXP)
            enemies.append(myVars[NAME])
        
    print("These enemies were loaded:\n")
    enemy_dict = {}
    for opponent in enemies:
        enemy_dict.update({opponent.NAME:opponent})
        print(opponent.info(),"\n")

    return opponent.info() 

iface = gr.Interface(
    fn=process_file,
    inputs=gr.File(label="Upload File"),
    outputs="text"
)

# To-Do : Suppress share=True message
iface.launch()
