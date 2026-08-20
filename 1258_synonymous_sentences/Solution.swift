// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

class Solution {
    func generateSentences(_ synonyms: [[String]], _ text: String) -> [String] {
        var parent: [String: String] = [:]
        func find(_ x: String) -> String {
            if parent[x] == nil { parent[x] = x }
            if parent[x]! != x { parent[x] = find(parent[x]!) }
            return parent[x]!
        }
        func union(_ a: String, _ b: String) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[rb] = ra }
        }
        for pair in synonyms { union(pair[0], pair[1]) }
        var groups: [String: [String]] = [:]
        for (w, _) in parent {
            groups[find(w), default: []].append(w)
        }
        for k in groups.keys { groups[k]!.sort() }
        let words = text.split(separator: " ").map(String.init)
        var ans: [String] = []
        func dfs(_ i: Int, _ path: [String]) {
            if i == words.count {
                ans.append(path.joined(separator: " "))
                return
            }
            let w = words[i]
            if parent[w] != nil {
                for syn in groups[find(w)]! {
                    dfs(i + 1, path + [syn])
                }
            } else {
                dfs(i + 1, path + [w])
            }
        }
        dfs(0, [])
        return ans
    }
}
