def get_medal(score):
    if score >=158:
        return "Gold Medal! Also, word record! Congratulations!"
    elif score >=152:
        return "Glod Medal!"
    elif score >=145:
        return "Silver Medal!"
    elif score >= 142:
        return "Bronze Medal!"
    else:
        return "No medal."
    

try:
    user_input = input ("What is the athlete's score?")
    score = float(user_input)
    result = get_medal(score)
    print(f"Result: {result}")
except:
    print("Error: Please enter a valid number.")