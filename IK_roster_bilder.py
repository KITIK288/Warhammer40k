import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox

def show_info_unit(unit):
    if unit == "Armiger knight Warglaive":
        messagebox.showinfo("Информация", f"Информация о юните 1: {unit}")
    elif unit == "Armiger knight Helverin":
        messagebox.showinfo("Информация", f"Информация о юните 2: {unit}")
    elif unit == "Armiger knight Moraix":
        messagebox.showinfo("Информация", f"Информация о юните 3: {unit}")
    elif unit == "Questoris Knight Paladin":
        messagebox.showinfo("Информация", f"Информация о юните 4: {unit}")
    elif unit == "Questoris Knight Errant":
        messagebox.showinfo("Информация", f"Информация о юните 5: {unit}")
    elif unit == "Questoris Knight Warden":
        messagebox.showinfo("Информация", f"Информация о юните 6: {unit}")
    elif unit == "Questoris Crusader Knight":
        messagebox.showinfo("Информация", f"Информация о юните 7: {unit}")
    elif unit == "Questoris Gallant Knight":
        messagebox.showinfo("Информация", f"Информация о юните 8: {unit}")
    elif unit == "Cerastus Lancer":
        messagebox.showinfo("Информация", f"Информация о юните 9: {unit}")
    elif unit == "Cerastus Castigator":
        messagebox.showinfo("Информация", f"Информация о юните 10: {unit}")
    elif unit == "Cerastus Acheron":
        messagebox.showinfo("Информация", f"Информация о юните 11: {unit}")
    elif unit == "Cerastus Atrapos":
        messagebox.showinfo("Информация", f"Информация о юните 12: {unit}")
    elif unit == "Knight Castellan":
        messagebox.showinfo("Информация", f"Информация о юните 13: {unit}")
    elif unit == "Knight Valiant":
        messagebox.showinfo("Информация", f"Информация о юните 14: {unit}")
    elif unit == "Knight Acastus Porphyrion":
        messagebox.showinfo("Информация", f"Информация о юните 15: {unit}")
    elif unit == "Knight Acastus Asterius":
        messagebox.showinfo("Информация", f"Информация о юните 16: {unit}")
    elif unit == "Questoris Knight Styrix":
        messagebox.showinfo("Информация", f"Информация о юните 17: {unit}")
    elif unit == "Questoris Knight Magaera":
        messagebox.showinfo("Информация", f"Информация о юните 18: {unit}")

def show_info_enchantments(enchantment):
    if enchantment == "Revered Knight":
        messagebox.showinfo("Информация", f"Информация о енчачменте 1: {enchantment}")
    if enchantment == "Mysterious Guardian":
        messagebox.showinfo("Информация", f"Информация о енчачменте 2: {enchantment}")
    if enchantment == "Banner of Macharius Triumphant":
        messagebox.showinfo("Информация", f"Информация о енчачменте 3: {enchantment}")
    if enchantment == "Mythic Hero":
        messagebox.showinfo("Информация", f"Информация о енчачменте 4: {enchantment}")
    if enchantment == "Unyielding Paragon":
        messagebox.showinfo("Информация", f"Информация о енчачменте 5: {enchantment}")

def show_info_warlords(warlord):
    print('warlord: ' + warlord)
    if warlord == "Questoris Knight Paladin":
        messagebox.showinfo("Информация", f"Информация о варлорде 1: {warlord}")
    elif warlord == "Questoris Knight Errant":
        messagebox.showinfo("Информация", f"Информация о варлорде 2: {warlord}")
    elif warlord == "Questoris Knight Warden":
        messagebox.showinfo("Информация", f"Информация о варлорде 3: {warlord}")
    elif warlord == "Questoris Crusader Knight":
        messagebox.showinfo("Информация", f"Информация о варлорде 4: {warlord}")
    elif warlord == "Questoris Gallant Knight":
        messagebox.showinfo("Информация", f"Информация о варлорде 5: {warlord}")
    elif warlord == "Cerastus Lancer":
        messagebox.showinfo("Информация", f"Информация о варлорде 6: {warlord}")
    elif warlord == "Cerastus Castigator":
        messagebox.showinfo("Информация", f"Информация о варлорде 7: {warlord}")
    elif warlord == "Cerastus Acheron":
        messagebox.showinfo("Информация", f"Информация о варлорде 8: {warlord}")
    elif warlord == "Cerastus Atrapos":
        messagebox.showinfo("Информация", f"Информация о варлорде 9: {warlord}")
    elif warlord == "Knight Castellan":
        messagebox.showinfo("Информация", f"Информация о варлорде 10: {warlord}")
    elif warlord == "Knight Valiant":
        messagebox.showinfo("Информация", f"Информация о варлорде 11: {warlord}")
    elif warlord == "Questoris Knight Styrix":
        messagebox.showinfo("Информация", f"Информация о варлорде 12: {warlord}")
    elif warlord == "Questoris Knight Magaera":
        messagebox.showinfo("Информация", f"Информация о варлорде 13: {warlord}")


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


# Данные о юнитах, варлордах и энчантментах
units = {
    "Armiger knight Warglaive": 150,
    "Armiger knight Helverin": 140,
    "Armiger knight Moraix": 160,
    "Questoris Knight Paladin": 425,
    "Questoris Knight Errant": 405,
    "Questoris Knight Warden": 450,
    "Questoris Crusader Knight": 445,
    "Questoris Gallant Knight": 400,
    "Cerastus Lancer": 465,
    "Cerastus Castigator": 465,
    "Cerastus Acheron": 425,
    "Cerastus Atrapos": 440,
    "Knight Castellan": 525,
    "Knight Valiant": 530,
    "Knight Acastus Porphyrion": 765,
    "Knight Acastus Asterius": 710,
    "Questoris Knight Styrix": 460,
    "Questoris Knight Magaera": 425,
}

warlords = {
    "Questoris Knight Paladin": 425,
    "Questoris Knight Errant": 405,
    "Questoris Knight Warden": 450,
    "Questoris Crusader Knight": 445,
    "Questoris Gallant Knight": 400,
    "Cerastus Lancer": 465,
    "Cerastus Castigator": 465,
    "Cerastus Acheron": 425,
    "Cerastus Atrapos": 440,
    "Questoris Knight Styrix": 460,
    "Questoris Knight Magaera": 425,
}

enchantments = {
    "Revered Knight": 20,
    "Mysterious Guardian": 35,
    "Banner of Macharius Triumphant": 230,
    "Mythic Hero": 25,
    "Unyielding Paragon": 40,
}

# Функция для расчета общей стоимости ростера
def calculate_roster():
    total_cost = 0
    selected_units = []
    selected_warlord = None
    selected_enchantments = []

    # Юниты
    for unit, cost in units.items():
        count = unit_vars[unit].get()
        if count > 0:
            total_cost += cost * count
            selected_units.append(f"{count} x {unit}")

    # Варлорд
    for warlord, cost in warlords.items():
        if warlord_var.get() == warlord:
            total_cost += cost
            selected_warlord = warlord

    # Энчантменты
    for enchantment, cost in enchantments.items():
        if enchantment_vars[enchantment].get():
            total_cost += cost
            selected_enchantments.append(enchantment)

    selected_units_text = "\n".join(selected_units)
    selected_warlord_text = selected_warlord if selected_warlord else ""
    selected_enchantments_text = "\n".join(selected_enchantments) if selected_enchantments else ""
    result_output.delete("0.0", "end")
    result_output.insert("end", selected_units_text + "\n")
    result_output.insert("end", selected_warlord_text + "\n")
    result_output.insert("end", selected_enchantments_text + "\n")

    total_cost_label.config(text=f"Общая стоимость ростера: {total_cost} очков")


# Создание графического интерфейса
root = tk.Tk()
root.title("Создание ростера Имперских Рыцарей")

# Создание основного фрейма
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Создание фрейма для юнитов, варлордов и энчантментов
units_warlords_enchantments_frame = ttk.Frame(main_frame)
units_warlords_enchantments_frame.pack(padx=10, pady=10, fill="x")

# Юниты
unit_frame = ScrollableFrame(units_warlords_enchantments_frame, padding=10)
unit_frame.pack(side="left", padx=10, fill="both", expand=True)

unit_vars = {}
unit_spinboxes = {}
unit_labels = {}
for unit in units:
    unit_vars[unit] = tk.IntVar()
    info_button = ttk.Button(unit_frame.scrollable_frame, text="i", command=lambda u=unit: show_info_unit(u), width=2)
    info_button.grid(row=len(unit_vars), column=2, padx=0, pady=0)
    unit_spinbox = ttk.Spinbox(unit_frame.scrollable_frame, from_=0, to=10, textvariable=unit_vars[unit], width=3)
    unit_spinbox.grid(row=len(unit_vars), column=0, padx=0, pady=0)
    unit_label = ttk.Label(unit_frame.scrollable_frame, text=unit)
    unit_label.grid(row=len(unit_vars), column=1, padx=0, pady=0)
    unit_spinboxes[unit] = unit_spinbox
    unit_labels[unit] = unit_label

# Варлорд
warlord_frame = ttk.LabelFrame(units_warlords_enchantments_frame, text="Варлорд", padding=10)
warlord_frame.pack(side="left", padx=10, fill="both", expand=True)
warlords_vars = {}

warlord_var = tk.StringVar()
for index, warlord in enumerate(warlords):
    # Radiobutton
    radiobutton = ttk.Radiobutton(warlord_frame, text=warlord, variable=warlord_var, value=warlord)
    radiobutton.grid(row=index, column=0, sticky="w")

    # Info button
    info_button_warlord = ttk.Button(warlord_frame, text="i", command=lambda w=warlord: show_info_warlords(w), width=2)
    info_button_warlord.grid(row=index, column=1, padx=(5, 0))

# Энчантменты
enchantment_frame = ttk.LabelFrame(units_warlords_enchantments_frame, text="Энчантменты", padding=10)
enchantment_frame.pack(side="left", padx=10, fill="both", expand=True)

result = ttk.Frame(main_frame)
result.pack(side="left", fill="both", expand="true")

result_output = tk.Text(result, width=20, height=10, bg=root['bg'])
result_output.pack(fill="both", expand="true")

enchantment_vars = {}
for enchantment in enchantments:
    enchantment_vars[enchantment] = tk.IntVar()
    checkbox = ttk.Checkbutton(enchantment_frame, text='', variable=enchantment_vars[enchantment])
    checkbox.grid(row=len(enchantment_vars), column=0, padx=5, pady=5)
    info_button = ttk.Button(enchantment_frame, text="i", command=lambda e=enchantment: show_info_enchantments(e), width=2)
    info_button.grid(row=len(enchantment_vars), column=2, padx=0, pady=0)
    enchantment_label = ttk.Label(enchantment_frame, text=enchantment)
    enchantment_label.grid(row=len(enchantment_vars), column=1, padx=0, pady=0)

total_cost_label = ttk.Label(root, text="Список выбранных юнитов, энчачментов и варлорда")
total_cost_label.pack(pady=10)

# Кнопка расчета
calculate_button = tk.Button(root, text="Рассчитать ростер", command=calculate_roster, padx=20, pady=20)
calculate_button.pack(pady=10)

# Вывод общей стоимости
total_cost_label = ttk.Label(root, text="Общая стоимость ростера: 0 очков")
total_cost_label.pack(pady=10)

root.mainloop()
