def feature_store_lookup(feature_store, requests, defaults):
    combined_features = []

    for req in requests:
        user_id = req["user_id"]
        online_features = req.get("online_features", {})

        
        offline_features = feature_store.get(user_id, defaults)
        combined = {}
        combined.update(offline_features)
        combined.update(online_features)

        combined_features.append(combined)

    return combined_features
