def recommend(user_prefs, items):
    scores = {}

    for item, tags in items.items():
        match_count = 0

        for pref in user_prefs:
            if pref in tags:
                match_count += 1

        scores[item] = match_count

    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [(item, score) for item, score in sorted_items if score > 0]