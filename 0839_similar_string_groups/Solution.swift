// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

class Solution {
    func numSimilarGroups(_ strs: [String]) -> Int {
        let n = strs.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        func similar(_ a: String, _ b: String) -> Bool {
            let ca = Array(a), cb = Array(b)
            var d0 = -1, d1 = -1, diffs = 0
            for i in 0..<ca.count where ca[i] != cb[i] {
                diffs += 1
                if diffs > 2 { return false }
                if d0 < 0 { d0 = i } else { d1 = i }
            }
            return diffs == 0 || (diffs == 2 && ca[d0] == cb[d1] && ca[d1] == cb[d0])
        }
        var groups = n
        for i in 0..<n {
            for j in (i + 1)..<n where similar(strs[i], strs[j]) {
                let pi = find(i), pj = find(j)
                if pi != pj {
                    parent[pi] = pj
                    groups -= 1
                }
            }
        }
        return groups
    }
}
