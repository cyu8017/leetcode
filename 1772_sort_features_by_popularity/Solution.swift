// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

class Solution {
    func sortFeatures(_ features: [String], _ responses: [String]) -> [String] {
        let featureSet = Set(features)
        var count = [String: Int]()
        for response in responses {
            var seen = Set<String>()
            for word in response.split(separator: " ") {
                let w = String(word)
                if featureSet.contains(w) {
                    seen.insert(w)
                }
            }
            for word in seen {
                count[word, default: 0] += 1
            }
        }
        return features.sorted { a, b in
            let ca = count[a] ?? 0
            let cb = count[b] ?? 0
            if ca != cb {
                return ca > cb
            }
            return a < b
        }
    }
}
