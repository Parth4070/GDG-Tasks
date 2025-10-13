players = [
    {
        "name": "Kohli",
        "strengths": {"chase_master", "fast_bowling_destroyer", "fielding"},
        "weaknesses": {"left_arm_spin"}
    },
    {
        "name": "Rahul",
        "strengths": {"opener", "power_play", "wicketkeeping"},
        "weaknesses": {"pressure", "death_bowling"}
    },
    {
        "name": "Bumrah",
        "strengths": {"death_bowling", "yorkers", "economy"},
        "weaknesses": {"batting"}
    },
    {
        "name": "Jadeja",
        "strengths": {"power_hitting", "off_spin", "fielding"},
        "weaknesses": set()
    },
    {
        "name": "Maxwell",
        "strengths": {"spin_bowling", "fielding", "finisher"},
        "weaknesses": {"pace_bounce", "consistency"}
    },
    {
        "name": "Siraj",
        "strengths": {"swing_bowling", "new_ball"},
        "weaknesses": {"batting"}
    },
    {
        "name": "Shreyas",
        "strengths": {"middle_order", "spin_hitter"},
        "weaknesses": {"express_pace", "short_ball"}
    },
    {
        "name": "Chahal",
        "strengths": {"leg_spin", "wicket_taker"},
        "weaknesses": {"fielding", "batting", "expensive"}
    },
    {
        "name": "DK",
        "strengths": {"finisher", "wicketkeeping", "experience"},
        "weaknesses": {"poor_wicketkeeping"}
    },
    {
        "name": "Faf",
        "strengths": {"opener", "experience", "fielding"},
        "weaknesses": {"slow_starter"}
    }
]


def compute_score(team):
    total_strengths = set()
    total_weakness = set()

    for player in team:
        total_strengths |= player['strengths']
        total_weakness |= player['weaknesses']
    
    return len(total_strengths) - len(total_weakness)


from itertools import combinations

def find_team(players, k):
    best_score = float('-inf')
    best_team = None

    for team in combinations(players, k):
        score = compute_score(team)
        if score > best_score:
            best_score = score
            best_team = team

    return best_team,  best_score



bonus_scores = {'chase_master': 2, 'death_bowling': 3, 'opener':1}
def bonus_calculate(team):
    bonus_score = 0

    for player in team:
        for strength in player['strengths']:
            if strength in bonus_scores:
                bonus_score += bonus_scores[strength]
        
    return bonus_score

n = int(input("Enter the team size:"))
best_team, score = find_team(players, n)
bonus = bonus_calculate(best_team)
print(f"{[p['name'] for p in best_team]}, Score: {score}, Bonus: {bonus}, Net Score: {score+bonus}")