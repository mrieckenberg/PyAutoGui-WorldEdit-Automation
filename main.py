import pyautogui as gui
import time
import random
import tkinter as tk



class WorldEditAutomationClass():
    def __init__(self):

        self.coordinates = [
            # Test coordinates *************************
            # [(646, 66, 2029), (621, 75, 2082)],
            # [(588, 71, 2056), (570, 82, 2077)],
            # ******************************************

            # Row house coordinates
            [(-1207, 113, -153), (-1227, 65, -271)],
            [(-1194, 113, -275), (-1171, 65, -156)],
        ]

        self.old_materials = [
            # Test materials *************************
            # "red_sand",
            # "orange_terracotta",
            # "terracotta",
            # ****************************************

            # Row house old materials
            "chiseled_red_sandstone",
            "red_terracotta",
            "stripped_jungle_log",
            "green_terracotta",
            "bricks",

        ]

        self.new_materials = [
            # Test materials *************************
            # "gold_block",
            # "bricks",
            # "acacia_planks",
            # "oak_planks",
            # ****************************************

            # Row house new materials
            "terracotta",
            "blue_terracotta",
            "brown_terracotta",
            "light_blue_terracotta",
            "purple_terracotta",
            "chiseled_sandstone",
            "bricks",


        ]

        # Any blocks that wish to be deleted
        self.delete_materials = [
            "dirt",
            "gray_concrete",
            "yellow_concrete",
        ]

    def replace_old_materials(self):
        print("Replacing old materials")
        time.sleep(5) # Time to open Minecraft
        # Loop through the list of coordinate pairs
        for i in range(len(self.coordinates)):
            # Position 1
            pos1 = "pos1 " + str(self.coordinates[i][0][0]) + "," + str(self.coordinates[i][0][1]) + "," + str(
                self.coordinates[i][0][2])
            # print(pos1)
            gui.press('/')
            gui.typewrite('/' + pos1)
            gui.press('enter')

            # Position 2
            pos2 = "pos2 " + str(self.coordinates[i][1][0]) + "," + str(self.coordinates[i][1][1]) + "," + str(
                self.coordinates[i][1][2])
            # print(pos2)
            gui.press('/')
            gui.typewrite('/' + pos2)
            gui.press('enter')


            # Replace the old material with a random new material
            for x in range(len(self.old_materials)):
                gui.press('/')
                command = "replace " + self.old_materials[x] + " " + \
                          self.new_materials[random.randint(0, len(self.new_materials))-1]
                print(command)
                gui.typewrite('/' + command)
                gui.press('enter')

            # Destroy (replace with air) scaffolding materials
            for y in range(len(self.delete_materials)):
                gui.press('/')
                command = "replace " + self.delete_materials[y] + " air"
                print(command)
                gui.typewrite('/' + command)
                gui.press('enter')




world_edit = WorldEditAutomationClass()
world_edit.replace_old_materials()
