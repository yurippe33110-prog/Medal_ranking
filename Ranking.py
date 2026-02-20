def get_medal(score):

    """Determines the Olympic medal. Includes logic for word record detection and input validation. """

    WORLD_RECORED = 158
    GOLD = 152
    SILVER = 145
    Bronze = 142


    if score >=158:
        return "Gold Medal! Also, word record! Congratulations!"
    elif score >=152:
        return "Gold Medal!"
    elif score >=145:
        return "Silver Medal!"
    elif score >= 142:
        return "Bronze Medal!"
    else:
        return "No medal."
    
if __name__ == "__main__":
    try:
        user_input = input ("What is the athlete's score?")
        score = float(user_input)
        result = get_medal(score)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number.")