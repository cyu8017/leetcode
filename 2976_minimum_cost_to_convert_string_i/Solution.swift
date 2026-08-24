// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution {
    func minimumCost(_ source: String, _ target: String, _ original: [String], _ changed: [String], _ cost: [Int]) -> Int {
        let inf = 1 << 60
        var dist = Array(repeating: Array(repeating: inf, count: 26), count: 26)
        for i in 0..<26 { dist[i][i] = 0 }
        let aVal = Int(Character("a").asciiValue!)
        for i in 0..<original.count {
            let u = Int(original[i].first!.asciiValue!) - aVal
            let v = Int(changed[i].first!.asciiValue!) - aVal
            dist[u][v] = min(dist[u][v], cost[i])
        }
        for k in 0..<26 {
            for i in 0..<26 {
                for j in 0..<26 {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                }
            }
        }
        var ans = 0
        let s = Array(source), t = Array(target)
        for i in 0..<s.count {
            let a = Int(s[i].asciiValue!) - aVal
            let b = Int(t[i].asciiValue!) - aVal
            if dist[a][b] >= inf / 2 { return -1 }
            ans += dist[a][b]
        }
        return ans
    }
}
