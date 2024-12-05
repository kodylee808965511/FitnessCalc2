import tkinter as tk
from tkinter import Button, Label, ttk
import os


# Placeholder event handlers
def on_focus_in(event):
    if event.widget.get() == event.widget.placeholder_text:
        event.widget.delete(0, tk.END)
        event.widget.config(foreground='black')

def on_focus_out(event):
    if event.widget.get() == "":
        event.widget.insert(0, event.widget.placeholder_text)
        event.widget.config(foreground='grey')

def setup_placeholder(entry, text):
    entry.placeholder_text = text
    entry.insert(0, text)
    entry.config(foreground='grey')
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# Calculate BMI
def getBmiCalculator():
    try:
        age = int(age_entry1.get())
        height = int(height_entry1.get())
        feet = int(height / 12)
        inches = height - (feet * 12)
        weight = float(weight_entry1.get())
        gender = gender_var1.get()
        bmi = float(weight / (height * height) * 703.0)
        bmi = f"{bmi:.2f}"

        result_text1.delete(1.0, tk.END)
        result_text1.insert(tk.END, f"Gender: {gender}\n")
        result_text1.insert(tk.END, f"Age: {age}\n")
        result_text1.insert(tk.END, f"Height: {feet}'{inches}\"\n")
        result_text1.insert(tk.END, f"Weight: {weight} lbs\n")
        result_text1.insert(tk.END, f"BMI: {bmi}\n")

    except ValueError:
        result_text1.delete(1.0, tk.END)
        result_text1.insert(tk.END, "Invalid input. Enter valid numbers.")

# Calculate BFP
def bfpCalculator():
    try:
        age = int(age_entry2.get())
        weight = float(weight_entry2.get())
        gender = gender_var2.get()
        bmi = float(bmi_entry2.get())
        bfp = float()
        if gender == "Male":
            bfp = (1.20 * bmi) + (0.23 * age) - 16.2
        elif gender == "Boy":
            bfp = (1.51 * bmi) + (0.23 * age) - 2.2
        elif gender == "Female":
            bfp = (1.20 * bmi) + (0.23 * age) - 5.4
        elif gender == "Girl":
            bfp = (1.51 * bmi) + (0.23 * age) + 1.4
        bfp = f"{bfp:.2f}"

        result_text2.delete(1.0, tk.END)
        result_text2.insert(tk.END, f"Gender: {gender}\n")
        result_text2.insert(tk.END, f"Age: {age}\n")
        result_text2.insert(tk.END, f"Weight: {weight} lbs\n")
        result_text2.insert(tk.END, f"Estimated BFP: {bfp}&\n")

    except ValueError:
        result_text2.delete(1.0, tk.END)
        result_text2.insert(tk.END, "Invalid input. Enter valid numbers.")

# Main window setup
window = tk.Tk()
window.title("Fitness Calculator")
window.geometry("700x550")

# Create a custom title bar frame
title_bar = tk.Frame(window, bg="light blue")
title_bar.pack(fill="x")

# Create a label for the title
title_label = tk.Label(title_bar, text="Fitness Calculator", bg="light blue", fg="white")
title_label.pack(side="left")


# Remove the default title bar
window.overrideredirect(True)

# Create tabbed interface
notebook = ttk.Notebook(window)

# Tab 0 - Welcome Page
welcome_tab = ttk.Frame(notebook)
notebook.add(welcome_tab, text="Welcome")

# Tab 1 - BMI Calculator
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="BMI Calculator")

# Tab 2 - BFP Calculator
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="BFP Calculator")

# Tab 3 - Hypertrophy and Strength
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="One Rep Max")

# Place notebook in window
notebook.pack(expand=1, fill='both')

# --- Welcome Tab Widgets ---
welcome_label = ttk.Label(welcome_tab, text="Welcome to the Fitness Calculator!", font='Calibri 20 bold')
welcome_label.pack(pady=30)

# Show main tabs after welcome page
def bmi_select():
    notebook.select(1)  # Select the first tab (BMICalculator Info) after the welcome page
def bfp_select():
    notebook.select(2)
def orm_select():
    notebook.select(3)
# --- BMI Button ---
bmi_calc_button = ttk.Button(welcome_tab, text="BMI Calculator", command=bmi_select)
bmi_calc_button.pack(pady=10)
# --- BFP Button ---
bfp_calc_button = ttk.Button(welcome_tab, text="BFP Calculator", command=bfp_select)
bfp_calc_button.pack(pady=10)
# --- Nutrition Button ---
orm_calc_button = ttk.Button(welcome_tab, text = "One Rep Max", command=orm_select)
orm_calc_button.pack(pady=10)

# --- Tab 1 Widgets ---
age_label1 = ttk.Label(tab1, text="Age:", font='Calibri 16')
age_entry1 = ttk.Entry(tab1, width=20)
height_label1 = ttk.Label(tab1, text="Height:", font='Calibri 16')
height_entry1 = ttk.Entry(tab1, width=20)
weight_label1 = ttk.Label(tab1, text="Weight:", font='Calibri 16')
weight_entry1 = ttk.Entry(tab1, width=20)
gender_label1 = ttk.Label(tab1, text="Gender:", font='Calibri 16')
gender_var1 = tk.StringVar()
gender_entry1 = ttk.Combobox(tab1, textvariable=gender_var1, values=["Male", "Female"], state="readonly")
calculate_button1 = ttk.Button(tab1, text="Calculate BMI", command=getBmiCalculator)
result_text1 = tk.Text(tab1, height=10, width=30, bg="light blue", fg="blue")

# Tab 1 placeholders
setup_placeholder(age_entry1, "Age in yrs")
setup_placeholder(height_entry1, "Height in inches")
setup_placeholder(weight_entry1, "Weight in lbs")


# Tab 1 layout
age_label1.grid(row=0, column=0, padx=10, pady=5, sticky='e')
age_entry1.grid(row=0, column=1, padx=10, pady=5)
height_label1.grid(row=1, column=0, padx=10, pady=5, sticky='e')
height_entry1.grid(row=1, column=1, padx=10, pady=5)
weight_label1.grid(row=2, column=0, padx=10, pady=5, sticky='e')
weight_entry1.grid(row=2, column=1, padx=10, pady=5)
gender_label1.grid(row=3, column=0, padx=10, pady=5, sticky='e')
gender_entry1.grid(row=3, column=1, padx=10, pady=5)
calculate_button1.grid(row=5, column=0, columnspan=2, pady=20)
result_text1.grid(row=5, column=2, padx=10)


# --- BFP Tab Widgets ---
age_label2 = ttk.Label(tab2, text="Age:", font='Calibri 16')
age_entry2 = ttk.Entry(tab2, width=20)
bmi_label2 = ttk.Label(tab2, text="BMI:", font='Calibri 16')
bmi_entry2 = ttk.Entry(tab2, width=20)
weight_label2 = ttk.Label(tab2, text="Weight:", font='Calibri 16')
weight_entry2 = ttk.Entry(tab2, width=20)
gender_label2 = ttk.Label(tab2, text="Gender:", font='Calibri 16')
gender_var2 = tk.StringVar()
gender_entry2 = ttk.Combobox(tab2, textvariable=gender_var2, values=["Male", "Female", "Boy", "Girl"], state="readonly")
calculate_button2 = ttk.Button(tab2, text="Calculate BFP", command=bfpCalculator)
result_text2 = tk.Text(tab2, height=10, width=30, bg="light blue", fg="blue")

# Layout for BFP Tab
age_label2.grid(row=0, column=0, padx=10, pady=5, sticky='e')
age_entry2.grid(row=0, column=1, padx=10, pady=5)
bmi_label2.grid(row=1, column=0, padx=10, pady=5, sticky='e')
bmi_entry2.grid(row=1, column=1, padx=10, pady=5)
weight_label2.grid(row=2, column=0, padx=10, pady=5, sticky='e')
weight_entry2.grid(row=2, column=1, padx=10, pady=5)
gender_label2.grid(row=3, column=0, padx=10, pady=5, sticky='e')
gender_entry2.grid(row=3, column=1, padx=10, pady=5)
calculate_button2.grid(row=5, column=0, columnspan=2, pady=20)
result_text2.grid(row=5, column=2, padx=10)

# Tab 2 placeholders
setup_placeholder(age_entry2, "Age in yrs")
setup_placeholder(bmi_entry2, "BMI")
setup_placeholder(weight_entry2, "Weight in lbs")

# --- Hypertrophy and Strength Tab Widgets ---
# Function to calculate 1RM (One Rep Max) based on user input



# Function to calculate 1RM (One Rep Max) and Training Max based on user input
def calculate_strength_info():
    try:
        weight = float(weight_entry3.get())
        reps = int(reps_entry3.get())
        goal = goal_var3.get()

        result_text3.delete(1.0, tk.END)  # Clear previous results

        # Special case for reps = 1 and goal is "Train Max"
        if reps == 1 and goal == "Train Max":
            train_max_weight = weight * 0.85
            result_text3.insert(tk.END, f"Training Max: 5 x {train_max_weight:.2f} lbs\n")
        else:
            # The Epley formula for calculating 1RM
            one_rm = weight * (1 + reps / 30)
            result_text3.insert(tk.END, f"Weight lifted: {weight} lbs\n")
            result_text3.insert(tk.END, f"Reps performed: {reps}\n")
            result_text3.insert(tk.END, f"Training Goal: {goal}\n")
            result_text3.insert(tk.END, f"Estimated 1RM: {one_rm:.2f} lbs\n")

            # Additional check if the goal is Train Max but reps are not 1
            if goal == "Train Max":
                train_max_weight = one_rm * 0.85
                result_text3.insert(tk.END, f"Training Max (85% of 1RM): 5 x {train_max_weight:.2f} lbs\n")

    except ValueError:
        result_text3.delete(1.0, tk.END)
        result_text3.insert(tk.END, "Invalid input. Please enter valid numbers for weight and reps.")



'''
def calculate_strength_info():
    try:
        weight = float(weight_entry3.get())
        reps = int(reps_entry3.get())
        goal = goal_var3.get()

        # The Epley formula for calculating 1RM
        one_rm = weight * (1 + reps / 30)
        one_rm = f"{one_rm:.2f}"

        result_text3.delete(1.0, tk.END)  # Clear previous results
        result_text3.insert(tk.END, f"Weight lifted: {weight} lbs\n")
        result_text3.insert(tk.END, f"Reps performed: {reps}\n")
        result_text3.insert(tk.END, f"Training Goal: {goal}\n")
        result_text3.insert(tk.END, f"Estimated 1RM: {one_rm} lbs\n")

    except ValueError:
        result_text3.delete(1.0, tk.END)
        result_text3.insert(tk.END, "Invalid input. Please enter valid numbers for weight and reps.")
'''

# Create labels and entry fields for weight, reps, and goal
weight_label3 = ttk.Label(tab3, text="Weight Lifted (lbs):", font='Calibri 16')
weight_entry3 = ttk.Entry(tab3, width=20)

reps_label3 = ttk.Label(tab3, text="Number of Reps:", font='Calibri 16')
reps_entry3 = ttk.Entry(tab3, width=20)

goal_label3 = ttk.Label(tab3, text="Training Goal:", font='Calibri 16')
goal_var3 = tk.StringVar()
goal_combo3 = ttk.Combobox(tab3, textvariable=goal_var3, values=["Train Max", "Estimated Max"], state="readonly")

# Button to trigger the calculation
calculate_button3 = ttk.Button(tab3, text="Calculate Goal", command=calculate_strength_info)



# Text widget to display the results
result_text3 = tk.Text(tab3, height=10, width=40, bg="light blue", fg="blue")

# Layout for Hypertrophy and Strength Tab
weight_label3.grid(row=0, column=0, padx=10, pady=5, sticky='e')
weight_entry3.grid(row=0, column=1, padx=10, pady=5)
reps_label3.grid(row=1, column=0, padx=10, pady=5, sticky='e')
reps_entry3.grid(row=1, column=1, padx=10, pady=5)
goal_label3.grid(row=2, column=0, padx=10, pady=5, sticky='e')
goal_combo3.grid(row=2, column=1, padx=10, pady=5)
calculate_button3.grid(row=3, column=0, columnspan=2, pady=20)
result_text3.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# --- Exercise Recommendation Tab ---
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Exercise Recommendations")

# Updated exercise dictionary with deeper subdivisions
exercise_dict = {
    "Chest": {
        "Lower Chest": ["Decline Bench Press", "Chest Dips", "Decline Push-ups"],
        "Middle Chest": ["Flat Bench Press", "Chest Fly", "Push-ups"],
        "Upper Chest": ["Incline Bench Press", "Incline Fly", "Incline Push-ups"]
    },
    "Back": {
        "Traps": ["Barbell Shrugs", "Face Pulls", "Farmer Walks"],
        "Upper Back": ["Face Pulls", "T-Bar Rows", "Seated Cable Rows"],
        "Lats": ["Pull-ups", "Lat Pulldowns", "Barbell Rows"],
        "Spinal Erectors": ["Deadlifts", "Back Extensions", "Good Mornings"]
    },
    "Arms": {
        "Biceps": {
            "Long Head": ["Incline Dumbbell Curls", "Hammer Curls", "Cable Rope Curls"],
            "Short Head": ["Preacher Curls", "Concentration Curls", "EZ Bar Curls"],
            "Brachialis": ["Hammer Curls", "Reverse Curls", "Zottman Curls"]
        },
        "Triceps": {
            "Long Head": ["Overhead Extensions", "Skull Crushers", "Close-grip Bench Press"],
            "Short Head": ["Cable Pushdowns", "Kickbacks", "Dips"]
        }
    },
    "Legs": {
        "Quads": ["Squats", "Lunges", "Leg Press"],
        "Hamstrings": ["Romanian Deadlifts", "Leg Curls", "Nordic Curls"],
        "Calves": ["Standing Calf Raises", "Seated Calf Raises", "Donkey Calf Raises"],
        "Glutes": ["Hip Thrusts", "Glute Bridges", "Bulgarian Split Squats"]
    },
    "Abs": {
        "Upper Abs": ["Crunches", "Sit-ups", "Mountain Climbers"],
        "Lower Abs": ["Leg Raises", "Hanging Knee Raises", "Flutter Kicks"],
        "Obliques": ["Russian Twists", "Side Planks", "Woodchoppers"]
    },
    "Shoulders": {
        "Anterior Delt": ["Front Raises", "Overhead Press", "Push Press"],
        "Lateral Delt": ["Lateral Raises", "Arnold Press", "Cable Lateral Raises"],
        "Posterior Delt": ["Reverse Fly", "Face Pulls", "Bent-over Raises"]
    }
}

# Function to clear all buttons from a specified row
def clear_buttons_from_row(row):
    for widget in tab4.grid_slaves(row=row):
        widget.destroy()

# Function to show secondary muscle group buttons
def show_secondary_buttons(main_group):
    clear_buttons_from_row(1)  # Clear secondary-level buttons
    clear_buttons_from_row(2)  # Clear tertiary-level buttons
    result_text4.delete(1.0, tk.END)

    sub_groups = exercise_dict.get(main_group, {})
    for idx, sub_group in enumerate(sub_groups):
        button = ttk.Button(tab4, text=sub_group, 
                            command=lambda sg=sub_group: show_tertiary_buttons(main_group, sg))
        button.grid(row=1, column=idx, padx=10, pady=10)

# Function to show tertiary muscle group buttons (if applicable)
def show_tertiary_buttons(main_group, sub_group):
    clear_buttons_from_row(2)  # Clear previous tertiary-level buttons

    tertiary_groups = exercise_dict[main_group].get(sub_group, None)

    if isinstance(tertiary_groups, dict):  # If further subdivisions exist
        for idx, group in enumerate(tertiary_groups):
            button = ttk.Button(tab4, text=group, 
                                command=lambda g=group: recommend_exercises(main_group, sub_group, g))
            button.grid(row=2, column=idx, padx=10, pady=10)
    else:
        recommend_exercises(main_group, sub_group)

# Function to display exercises for the selected group
def recommend_exercises(main_group, sub_group, tertiary_group=None):
    if tertiary_group:
        exercises = exercise_dict[main_group][sub_group][tertiary_group]
        title = f"{main_group} - {sub_group} - {tertiary_group} Exercises:\n"
    else:
        exercises = exercise_dict[main_group][sub_group]
        title = f"{main_group} - {sub_group} Exercises:\n"

    result_text4.delete(1.0, tk.END)
    result_text4.insert(tk.END, title + "\n".join(exercises))

# Create primary muscle group buttons
primary_groups = exercise_dict.keys()
for idx, group in enumerate(primary_groups):
    button = ttk.Button(tab4, text=group, command=lambda g=group: show_secondary_buttons(g))
    button.grid(row=0, column=idx, padx=10, pady=10)

# Text widget to display the recommended exercises
result_text4 = tk.Text(tab4, height=10, width=50, bg="light blue", fg="blue")
result_text4.grid(row=3, column=0, columnspan=len(primary_groups), padx=10, pady=10)

# Data structure to store the user's meals
nutrition_data = []

# Initial daily goal values
daily_calorie_goal = 2000
daily_protein_goal = 150  # grams
daily_fat_goal = 70       # grams
daily_carb_goal = 250     # grams

# Function to add a meal entry
def add_meal():
    try:
        meal_name = meal_name_entry.get()
        calories = float(calorie_entry.get())
        protein = float(protein_entry.get())
        fat = float(fat_entry.get())
        carbs = float(carb_entry.get())

        # Add the meal to the list and update totals
        nutrition_data.append({"meal": meal_name, "calories": calories, "protein": protein, "fat": fat, "carbs": carbs})
        update_totals()

        # Clear the input fields
        meal_name_entry.delete(0, tk.END)
        calorie_entry.delete(0, tk.END)
        protein_entry.delete(0, tk.END)
        fat_entry.delete(0, tk.END)
        carb_entry.delete(0, tk.END)

    except ValueError:
        tk.messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Function to calculate daily nutrition goals based on user inputs
def calculate_nutrition_goals():
    global daily_calorie_goal, daily_protein_goal, daily_fat_goal, daily_carb_goal
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        # Basal Metabolic Rate (BMR) calculation using Mifflin-St Jeor Equation
        if gender == 'Male':
            bmr = 10 * weight + 6.25 * (height * 2.54) - 5 * age + 5  # weight in kg, height in cm
        else:
            bmr = 10 * weight + 6.25 * (height * 2.54) - 5 * age - 161

        # Daily calorie goal (adjusted for activity level)
        daily_calorie_goal = bmr * 1.55  # assuming moderate activity level

        # Setting protein goal (1g protein per lb of weight)
        daily_protein_goal = weight

        # Macro distribution (example: 30% protein, 30% fat, 40% carbs)
        daily_fat_goal = daily_calorie_goal * 0.30 / 9  # 9 calories per gram of fat
        daily_carb_goal = daily_calorie_goal * 0.40 / 4  # 4 calories per gram of carbs

        # Update the labels
        update_totals()

    except ValueError:
        tk.messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Function to update the total calories and macronutrients
def update_totals():
    total_calories = sum(meal['calories'] for meal in nutrition_data)
    total_protein = sum(meal['protein'] for meal in nutrition_data)
    total_fat = sum(meal['fat'] for meal in nutrition_data)
    total_carbs = sum(meal['carbs'] for meal in nutrition_data)

    # Update the labels to display totals
    total_calories_label.config(text=f"Total Calories: {total_calories:.0f} / {daily_calorie_goal:.0f}")
    total_protein_label.config(text=f"Protein: {total_protein:.0f}g / {daily_protein_goal:.0f}g")
    total_fat_label.config(text=f"Fat: {total_fat:.0f}g / {daily_fat_goal:.0f}g")
    total_carbs_label.config(text=f"Carbs: {total_carbs:.0f}g / {daily_carb_goal:.0f}g")

    # Update progress bars
    calorie_progress['value'] = min((total_calories / daily_calorie_goal) * 100, 100)
    protein_progress['value'] = min((total_protein / daily_protein_goal) * 100, 100)
    fat_progress['value'] = min((total_fat / daily_fat_goal) * 100, 100)
    carb_progress['value'] = min((total_carbs / daily_carb_goal) * 100, 100)

# Function to reset the day's log
def reset_log():
    global nutrition_data
    nutrition_data = []
    update_totals()

# Function to update protein based on weight
def update_protein_from_weight(event):
    try:
        weight = float(weight_entry.get())
        protein_entry.delete(0, tk.END)
        protein_entry.insert(0, str(weight))  # Set protein to weight in grams
    except ValueError:
        pass  # Ignore if weight is not valid

# Create a new Nutrition Tracker tab
nutrition_tab = ttk.Frame(notebook)
notebook.add(nutrition_tab, text="Nutrition Tracker")

# Personal Info input
weight_label = ttk.Label(nutrition_tab, text="Weight (lbs):")
weight_entry = ttk.Entry(nutrition_tab, width=10)
weight_entry.bind("<Return>", update_protein_from_weight)  # Update protein on Enter key
height_label = ttk.Label(nutrition_tab, text="Height (inches):")
height_entry = ttk.Entry(nutrition_tab, width=10)
age_label = ttk.Label(nutrition_tab, text="Age (years):")
age_entry = ttk.Entry(nutrition_tab, width=10)
gender_label = ttk.Label(nutrition_tab, text="Gender:")
gender_var = tk.StringVar()
gender_male = ttk.Radiobutton(nutrition_tab, text='Male', variable=gender_var, value='Male')
gender_female = ttk.Radiobutton(nutrition_tab, text='Female', variable=gender_var, value='Female')

# Calculate button to update nutrition goals
calculate_button = ttk.Button(nutrition_tab, text="Calculate", command=calculate_nutrition_goals)

# Input fields for meal entry
meal_name_label = ttk.Label(nutrition_tab, text="Meal Name:")
meal_name_entry = ttk.Entry(nutrition_tab, width=20)
calorie_label = ttk.Label(nutrition_tab, text="Calories:")
calorie_entry = ttk.Entry(nutrition_tab, width=10)
protein_label = ttk.Label(nutrition_tab, text="Protein (g):")
protein_entry = ttk.Entry(nutrition_tab, width=10)
fat_label = ttk.Label(nutrition_tab, text="Fat (g):")
fat_entry = ttk.Entry(nutrition_tab, width=10)
carb_label = ttk.Label(nutrition_tab, text="Carbs (g):")
carb_entry = ttk.Entry(nutrition_tab, width=10)

# Button to add the meal
add_meal_button = ttk.Button(nutrition_tab, text="Add Meal", command=add_meal)

# Labels to display daily totals and progress
total_calories_label = ttk.Label(nutrition_tab, text=f"Total Calories: 0 / {daily_calorie_goal:.0f}")
total_protein_label = ttk.Label(nutrition_tab, text=f"Protein: 0g / {daily_protein_goal:.0f}g")
total_fat_label = ttk.Label(nutrition_tab, text=f"Fat: 0g / {daily_fat_goal:.0f}g")
total_carbs_label = ttk.Label(nutrition_tab, text=f"Carbs: 0g / {daily_carb_goal:.0f}g")

# Progress bars for each macronutrient and calories
calorie_progress = ttk.Progressbar(nutrition_tab, length=300, maximum=100)
protein_progress = ttk.Progressbar(nutrition_tab, length=300, maximum=100)
fat_progress = ttk.Progressbar(nutrition_tab, length=300, maximum=100)
carb_progress = ttk.Progressbar(nutrition_tab, length=300, maximum=100)

# Button to reset the day's log
reset_button = ttk.Button(nutrition_tab, text="Reset Log", command=reset_log)

# Layout for the Nutrition Tracker tab
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
weight_entry.grid(row=0, column=1, padx=5, pady=5)
height_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
height_entry.grid(row=1, column=1, padx=5, pady=5)
age_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
age_entry.grid(row=2, column=1, padx=5, pady=5)
gender_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
gender_male.grid(row=3, column=1, padx=5, pady=5, sticky='w')
gender_female.grid(row=3, column=2, padx=5, pady=5, sticky='w')

calculate_button.grid(row=4, column=0, columnspan=3, pady=10)

meal_name_label.grid(row=0, column=3, padx=5, pady=5, sticky='e')
meal_name_entry.grid(row=0, column=4, padx=5, pady=5)
calorie_label.grid(row=1, column=3, padx=5, pady=5, sticky='e')
calorie_entry.grid(row=1, column=4, padx=5, pady=5)
protein_label.grid(row=2, column=3, padx=5, pady=5, sticky='e')
protein_entry.grid(row=2, column=4, padx=5, pady=5)
fat_label.grid(row=3, column=3, padx=5, pady=5, sticky='e')
fat_entry.grid(row=3, column=4, padx=5, pady=5)
carb_label.grid(row=4, column=3, padx=5, pady=5, sticky='e')
carb_entry.grid(row=4, column=4, padx=5, pady=5)

add_meal_button.grid(row=5, column=3, columnspan=2, pady=10)

total_calories_label.grid(row=6, column=0, columnspan=5, pady=5)
calorie_progress.grid(row=7, column=0, columnspan=5, pady=5)
total_protein_label.grid(row=8, column=0, columnspan=5, pady=5)
protein_progress.grid(row=9, column=0, columnspan=5, pady=5)
total_fat_label.grid(row=10, column=0, columnspan=5, pady=5)
fat_progress.grid(row=11, column=0, columnspan=5, pady=5)
total_carbs_label.grid(row=12, column=0, columnspan=5, pady=5)
carb_progress.grid(row=13, column=0, columnspan=5, pady=5)

reset_button.grid(row=14, column=0, columnspan=5, pady=10)

# Start the Tkinter event loop
window.mainloop()
