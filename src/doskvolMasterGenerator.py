# doskvolMasterGenerator.py
# A menu interface capable of calling the individual Doskvol generators


import doskvolBuildingGenerator as building
import doskvolDemonGenerator as demon
import doskvolGhostgenerator as ghost
import doskvolPeopleGenerator as npc
import doskvolStreetsGenerator as street
import doskvolCultGenerator as cult
import doskvolScoresGenerator as score
import utils
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
cult_column = [[sg.Button('Generate Cult')]]
score_column = [[sg.Button('Generate Score')]]

layout = [[sg.Column(output_column, background_color="#D5D5D5")],
          [sg.Column(npc_column, background_color="#D5D5D5"),
          sg.Column(building_column, background_color="#D5D5D5"),
          sg.Column(street_column, background_color="#D5D5D5"),
          sg.Column(npcRare_column, background_color="#D5D5D5"),
          sg.Column(buildingRare_column, background_color="#D5D5D5"),
          sg.Column(ghost_column, background_color="#D5D5D5"),
          sg.Column(cult_column, background_color="#D5D5D5"),
          sg.Column(score_column, background_color="#D5D5D5"),
          sg.Column(demon_column, background_color="#D5D5D5")]]
  
window = sg.Window('Blades in the Dark Generators').Layout(layout)

def main():
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event == "Generate Demon":
            random_demon = demon.build_demon()
            window.FindElement('_OUTPUT_').Update(demon.print_demon(random_demon))
        if event == "Generate Street":
            random_street = street.build_street()
            window.FindElement('_OUTPUT_').Update(street.print_street(random_street))
        if event == "Generate Ghost":
            random_ghost = ghost.build_ghost()
            window.FindElement('_OUTPUT_').Update(ghost.print_ghost(random_ghost))
        if event == 'Generate NPC':
            common_person = npc.build_person()
            window.FindElement('_OUTPUT_').Update(npc.print_person("common", common_person))
        if event == 'Generate Building':
            common_building = building.build_building()
            window.FindElement('_OUTPUT_').Update( building.print_building("common", common_building))
        if event == 'Generate Rare NPC':
            rare_person = npc.build_person()
            window.FindElement('_OUTPUT_').Update(npc.print_person("rare", rare_person))
        if event == 'Generate Rare Building':
            rare_building = building.build_building()
            window.FindElement('_OUTPUT_').Update( building.print_building("rare", rare_building))
        if event == 'Generate Cult':
            random_cult = cult.build_cult()
            window.FindElement('_OUTPUT_').Update( cult.print_cult(random_cult))
        if event == 'Generate Score':
            random_score = score.build_score()
            window.FindElement('_OUTPUT_').Update( score.print_score(random_score))
if __name__ == "__main__":
    main()
