Fitness Calculator Application README

Overview:
-------------
This Python-based Fitness Calculator Application is built using the Tkinter library for the graphical user interface (GUI). It offers various features for fitness enthusiasts, including:
1. BMI (Body Mass Index) and BFP (Body Fat Percentage) calculators
2. 1RM (One-Rep Max) strength training estimator
3. Exercise recommendations based on muscle group selection
4. Nutrition Tracker for logging meals and tracking macronutrients
5. Progress tracking for calories, protein, fat, and carbohydrates

The application is designed to help users monitor their fitness and nutrition goals while offering intuitive user input and output displays.

Features:
-----------
1. **BMI & BFP Calculator**: Allows users to calculate their Body Mass Index (BMI) and Body Fat Percentage (BFP) based on their weight, height, age, and gender.
2. **1RM Strength Estimator**: Estimates the user’s One-Rep Max (1RM) based on the weight lifted and number of reps.
3. **Exercise Recommendations**: Suggests exercises based on the primary muscle group selected by the user, including secondary muscle group exercises.
4. **Nutrition Tracker**: Logs daily meals, calculates calories, protein, fat, and carbohydrates, and tracks progress toward nutrition goals (calories, protein, fat, carbs).
5. **Progress Monitoring**: Real-time progress bars and totals for calories and macronutrients, and an automatic reset feature for meal logs.
6. **Personalized Nutrition Goals**: Calculates nutrition goals (calories, protein, fat, carbs) based on user input (weight, height, age, gender) using the Mifflin-St Jeor equation for BMR calculation.

Requirements:
--------------
- Python 3.x
- Tkinter library (usually included with standard Python distributions)
- Basic knowledge of Python and Tkinter for custom modifications

Installation:
--------------
1. Make sure you have Python 3.x installed on your system.
2. Download or clone the project files from the repository.

Usage:
--------
1. **BMI & BFP Calculator**: 
- Enter your weight, height, age, and gender, then click "Calculate" to get your BMI and BFP results.
2. **1RM Calculator**:
- Enter the name of the lift, the weight lifted, and the number of reps completed, then click "Calculate" to estimate your 1RM.
3. **Exercise Recommendations**:
- Select a primary muscle group, and the program will display a list of recommended exercises for that muscle group.
4. **Nutrition Tracker**:
- Input your weight, height, age, and gender to calculate your daily nutrition goals.
- Add meal entries by entering the meal name and its nutritional information (calories, protein, fat, carbs).
- Track your progress with real-time updates and progress bars.
- Reset your daily nutrition log anytime using the "Reset Log" button.

Features in Detail:
--------------------
### BMI & BFP Calculation:
- Users input weight (lbs), height (inches), age, and gender.
- The BMI and BFP are calculated and displayed based on the input values.

### 1RM Estimator:
- Users input the name of the lift, the weight lifted, and the number of reps performed.
- The application calculates the estimated 1RM using an appropriate formula.

### Exercise Recommendations:
- Users can select from a list of primary muscle groups (e.g., Chest, Back, Legs).
- Recommended exercises for the selected muscle group are displayed, and secondary exercises for other muscle groups are also shown.

### Nutrition Tracker:
- Users input personal details (weight, height, age, gender).
- Nutrition goals (calories, protein, fat, carbs) are calculated.
- Users can add meal entries with nutritional values (calories, protein, fat, carbs).
- The program tracks the total intake and updates real-time progress bars for calories and macronutrients.
- Users can reset their log to start fresh at any time.

Features and Calculations:
---------------------------
- **Basal Metabolic Rate (BMR)**: Calculated using the Mifflin-St Jeor equation for males and females.
- **Daily Nutrition Goals**: Adjusted based on user details and activity level.
- **Macronutrient Distribution**: Example breakdown of 30% protein, 30% fat, and 40% carbohydrates.

Future Enhancements:
--------------------
- Add more exercise recommendations and categorization by difficulty level.
- Implement more advanced macronutrient tracking with options for custom nutrient breakdowns.
- Improve user experience with more visual elements and interactive widgets.