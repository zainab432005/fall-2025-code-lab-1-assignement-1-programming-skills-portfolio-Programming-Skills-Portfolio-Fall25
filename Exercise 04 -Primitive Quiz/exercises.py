quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Sudan": "Alkhartoum",
    "UK": "London",
    "KSA": "Riyadh",
    "Japan": "Tokyo"
}

score = 0

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")

print(f"You got {score} out of {len(quiz)} correct.")
