print("===================================")
print("      BMI CALCULATOR SYSTEM")
print("===================================\n")

# Taking user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

# BMI Calculation
bmi = weight / (height ** 2)

print("\n-----------------------------------")
print(f"Hello {name} ")
print(f"Your BMI is: {round(bmi, 2)}")
print("-----------------------------------")

# Age Group Classification
if age < 13:
    age_group = "Child"
elif age < 60:
    age_group = "Adult"
else:
    age_group = "Senior Citizen"

print(f"Age Group: {age_group}")

print("\n========= BMI CATEGORY =========")

# BMI Category + Health Tips
if bmi < 18.5:
    print("Category: UNDERWEIGHT")
    print("""
Health Risks:
- Weak immunity
- Fatigue
- Nutritional deficiencies

Health Tips:
:- Eat more frequently
:- Include protein-rich foods
:- Add healthy fats (nuts, milk, ghee)
:- Avoid skipping meals
""")

elif 18.5 <= bmi < 25:
    print("Category: NORMAL WEIGHT")
    print("""
Health Status:
. Healthy body weight
. Lower risk of diseases

Health Tips:
:- Maintain balanced diet
:- Regular physical activity
:- Proper sleep schedule
:- Stay hydrated
""")

elif 25 <= bmi < 30:
    print("Category: OVERWEIGHT")
    print("""
Health Risks:
- High blood pressure
- Increased risk of diabetes
- Joint pain

Health Tips:
:- Reduce sugar & junk food
:- Increase fruits and vegetables
:- Daily walking / exercise
:- Monitor portion size
""")

else:
    print("Category: OBESE")
    print("""
Health Risks:
- Heart disease
- Diabetes
- High cholesterol
- Breathing problems

Health Tips:
:- Consult a healthcare professional
:- Structured diet plan
:- Regular cardio exercise
:- Avoid fried & processed foods
""")

print("===================================")
print("        THANK YOU FOR USING         ")
print("           BMI CALCULATOR           ")
print("===================================")

