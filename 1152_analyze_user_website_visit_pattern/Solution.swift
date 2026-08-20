// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution {
    func mostVisitedPattern(_ username: [String], _ timestamp: [Int], _ website: [String]) -> [String] {
        var visits: [String: [(Int, String)]] = [:]
        for i in 0..<username.count {
            visits[username[i], default: []].append((timestamp[i], website[i]))
        }
        var scores: [[String]: Int] = [:]
        for (_, list) in visits {
            let sites = list.sorted { $0.0 < $1.0 }.map { $0.1 }
            var patterns = Set<[String]>()
            for i in 0..<sites.count {
                for j in (i + 1)..<sites.count {
                    for k in (j + 1)..<sites.count {
                        patterns.insert([sites[i], sites[j], sites[k]])
                    }
                }
            }
            for p in patterns { scores[p, default: 0] += 1 }
        }
        let best = scores.min { a, b in
            if a.value != b.value { return a.value > b.value }
            return a.key.joined(separator: "\0") < b.key.joined(separator: "\0")
        }!.key
        return best
    }
}
