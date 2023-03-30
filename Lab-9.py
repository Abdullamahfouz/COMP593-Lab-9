from tkinter import *
from tkinter import ttk 
from poke_api import get_pokemon_info
from tkinter import messagebox
# create window 
root = Tk()
root.title("Poki Info Veiwer")
root.resizable(False, False)
# Add widget to the Window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2,  padx=(20, 10))

frm_btm_left = ttk.LabelFrame(root, text='info:')
frm_btm_left.grid(row=1, column=0, padx= (20, 10), pady= (10,20), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='stats:')
frm_btm_right.grid(row=1, column=1,padx= (10,20), pady= (10,20))

lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0 , padx=(10, 5), pady = 10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle_get_info():
    
    #Message box 
    poki_name = ent_name.get().strip()
    if len(poki_name) == 0 :
        return
    poki_info = get_pokemon_info(poki_name)
    if poki_info is None:
        err_msg =  f'Unable to fetch information for { poki_name.capitalize()} from the PokeAPI'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
    #Displays the Weight, Height 
    lbl_height_value['text'] = f" {poki_info['height'] } dm"
    lbl_weight_value['text'] = f" {poki_info['weight'] } hg"
    
    
    types_list = [t['type']['name'].title() for t in poki_info['types']]
    n = len(types_list)
    # Checks the length of the abilities and then prints it
    if n == 1:
        lbl_type_true['text'] = f"{types_list[0]}"
    
    else:
        types_csl = ', '.join(types_list[:-1])
        lbl_type_true['text'] = f"{types_csl}, {types_list[-1]}"
    
    # displays the stats 
    bar_hp['value'] = poki_info['stats'][0]['base_stat']
    bar_attack['value'] = poki_info['stats'][1]['base_stat']
    bar_defense['value'] = poki_info['stats'][2]['base_stat']
    bar_Special_attack['value'] = poki_info['stats'][3]['base_stat']
    bar_speed['value'] = poki_info['stats'][4]['base_stat']
    bar_Special_Defense['value'] = poki_info['stats'][5]['base_stat']
    return

# Populaate widget in the info frame
btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx= 10, pady= 10)


# Adds the weight value 
lbl_height = ttk.Label (frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0)
lbl_height_value = ttk.Label(frm_btm_left, text= 'TBD')
lbl_height_value.grid(row=0, column=1)


# Adds the height value 
lbl_weight = ttk.Label (frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0)
lbl_weight_value = ttk.Label(frm_btm_left, text= 'TBD')
lbl_weight_value.grid(row=1, column=1)


# Pokemon type info
lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=(10, 5), pady=(10, 5), )

lbl_type_true = ttk.Label(frm_btm_left, text='TBD')
lbl_type_true.grid(row=2, column=1, padx=(0, 10), pady=(10,5))


#Adds the hp
lbl_hp = ttk.Label(frm_btm_right, text= 'HP:')
lbl_hp.grid(row=0, column=0)
bar_hp = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0 , column=1)

# Adds the attack
lbl_attack = ttk.Label(frm_btm_right, text= 'Attack:')
lbl_attack.grid(row=1, column=0)
bar_attack = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1 , column=1)

# Adds the defense
lbl_defense = ttk.Label(frm_btm_right, text= 'Defense')
lbl_defense.grid(row=2, column=0)
bar_defense = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_defense.grid(row=2, column=1)

# Adds Special attack
lbl_special_attack=ttk.Label(frm_btm_right, text= 'Special Attack')
lbl_special_attack.grid(row=3, column=0)
bar_Special_attack = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_Special_attack.grid(row=3, column=1)

# Adds Special defense
lbl_special_Defense=ttk.Label(frm_btm_right, text= 'Special Defense')
lbl_special_Defense.grid(row=4, column=0)
bar_Special_Defense = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_Special_Defense.grid(row=4, column=1)

# Adds Speed
lbl_speed=ttk.Label(frm_btm_right, text= 'Speed')
lbl_speed.grid(row=5, column=0)
bar_speed = ttk.Progressbar(frm_btm_right, orient= HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1)


#loop until window is closed 
root.mainloop()
