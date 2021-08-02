# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators

import doskvolBuildingGenerator as building
import doskvolDemonGenerator as demon
import doskvolGhostgenerator as ghost
import doskvolPeopleGenerator as npc
import doskvolStreetsGenerator as street
import PySimpleGUI as sg


output_column = [[sg.Text('Output')],
                    [sg.Multiline('', size=(160,14), key='_OUTPUT_', do_not_clear=True)]]
demon_column = [[sg.Button('Generate Demon')]]
street_column = [[sg.Button('Generate Street')]]
ghost_column = [[sg.Button('Generate Ghost')]]

npc_column = [[sg.Button('Generate NPC')]]
building_column = [[sg.Button('Generate Building')]]
npcRare_column = [[sg.Button('Generate Rare NPC')]]
buildingRare_column = [[sg.Button('Generate Rare Building')]]

layout = [[sg.Column(output_column, background_color="#D5D5D5")],
          [sg.Column(npc_column, background_color="#D5D5D5"),
          sg.Column(building_column, background_color="#D5D5D5"),
          sg.Column(street_column, background_color="#D5D5D5"),
          sg.Column(npcRare_column, background_color="#D5D5D5"),
          sg.Column(buildingRare_column, background_color="#D5D5D5"),
          sg.Column(ghost_column, background_color="#D5D5D5"),
          sg.Column(demon_column, background_color="#D5D5D5")]]
  
window = sg.Window('Blades in the Dark Generators').Layout(layout)

def main():
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event == "Generate Demon":
            window.FindElement('_OUTPUT_').Update(demon.print_demon())
        if event == "Generate Street":
            window.FindElement('_OUTPUT_').Update(street.print_street())
        if event == "Generate Ghost":
            window.FindElement('_OUTPUT_').Update(ghost.print_ghost())
        if event == 'Generate NPC':
            window.FindElement('_OUTPUT_').Update(npc.print_person('common'))
        if event == 'Generate Building':
            window.FindElement('_OUTPUT_').Update( building.print_building('common'))
        if event == 'Generate Rare NPC':
            window.FindElement('_OUTPUT_').Update(npc.print_person('rare'))
        if event == 'Generate Rare Building':
            window.FindElement('_OUTPUT_').Update( building.print_building('rare'))
if __name__ == "__main__":
    main()
