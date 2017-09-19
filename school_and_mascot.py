# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment - Unit1-01
# This program displays the name of one of three schools and the name of its mascot using buttons

import ui

def mother_teresa_hs_touch_up_inside(sender):
    # displays the names of the school and its mascot for Mother Teresa HS
    view['school_name_label'].text = 'Mother Teresa HS'
    view['school_mascot_label'].text = 'Titans'

def st_joe_touch_up_inside(sender):
    # displays the names of the school and its mascot for St. Joe
    view['school_name_label'].text = 'St. Joe'
    view['school_mascot_label'].text = 'Jaguars'

def st_mark_touch_up_inside(sender):
    # displays the names of the school and its mascot for St. Mark
    view['school_name_label'].text = 'St. Mark'
    view['school_mascot_label'].text = 'Lions'

view = ui.load_view()
view.present('full_screen')
