import copy


# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie = {"title": title,
             "genre": genre,
             "rating": rating}
    
    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    total = 0.0

    if not user_data["watched"]:
        return total

    for movie in user_data["watched"]:
        total += movie["rating"]

    avg_rating = total / len(user_data["watched"])

    return avg_rating


def get_most_watched_genre(user_data):
    user_genres = {}
    most_watched = None
    times_watched = 0

    for movie in user_data["watched"]:
        if movie["genre"] not in user_genres:
            user_genres[movie["genre"]] = 1
        else:
            user_genres[movie["genre"]] += 1

    for genre in user_genres:
        if user_genres[genre] > times_watched:
            most_watched = genre
            times_watched = user_genres[genre]

    return most_watched


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    unique_watched = copy.deepcopy(user_data["watched"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in unique_watched:
                unique_watched.remove(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in unique_watched:
                unique_watched.append(movie)

    return unique_watched


# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    friends_recs = get_friends_unique_watched(user_data)
    available_recs = []

    for movie in friends_recs:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)

    return available_recs


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    friends_recs = get_friends_unique_watched(user_data)
    user_fav_genre = get_most_watched_genre(user_data)
    final_recs = []
    
    for movie in friends_recs:
        if movie["genre"] is user_fav_genre:
            final_recs.append(movie)

    return final_recs


def get_rec_from_favorites(user_data):
    user_recs = get_unique_watched(user_data)
    final_recs = []

    for movie in user_recs:
        if movie in user_data["favorites"]:
            final_recs.append(movie)

    return final_recs