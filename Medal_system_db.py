import sqlite3

def init_db():
    conn = sqlite3.connect('athlete_results.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS results (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   athlete_name TEXT, score REAL, medal TEXT) ''')
    conn.commit()
    return conn

def save_result(conn, neme, score, medal):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO results (athlete_name, score, medal) VALUES(?, ?, ?)",
        (name, score, medal)
    )
    conn.commit()

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
    db_conn = init_db()
    try:
        name = input("Athlete name: ")
        score_input = input("Athlete score: ")
        score = float (score_input)

        medal = get_medal(score)
        print(f"Result for {name}: {medal}")

        save_result(db_conn, name, score, medal)
        print("Olympic 2026 data successfully saved to SQL database.")

    except ValueError:
        print("Error: Please enter a valid number.")
    
    finally:
        db_conn.close()
    