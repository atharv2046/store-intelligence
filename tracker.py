from collections import defaultdict

tracks = defaultdict(dict)

def update_track(track_id, x, y):

    tracks[track_id]["x"] = x
    tracks[track_id]["y"] = y

    return tracks[track_id]