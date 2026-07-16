class Solution:
    def sortFeatures(self, features, responses):
        from collections import Counter
        count = Counter()
        feature_set = set(features)
        for response in responses:
            seen = set()
            for word in response.split():
                if word in feature_set:
                    seen.add(word)
            for word in seen:
                count[word] += 1
        return sorted(features, key=lambda f: (-count[f], f))
