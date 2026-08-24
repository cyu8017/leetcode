// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

class Solution {
    func checkContradictions(_ equations: [[String]], _ values: [Double]) -> Bool {
        var parent: [String: String] = [:]
        var weight: [String: Double] = [:]
        func find(_ x: String) -> String {
            if parent[x] == nil {
                parent[x] = x
                weight[x] = 1.0
                return x
            }
            if parent[x]! != x {
                let old = parent[x]!
                let p = find(old)
                weight[x] = weight[x]! * weight[old]!
                parent[x] = p
            }
            return parent[x]!
        }
        for i in 0..<equations.count {
            let a = equations[i][0], b = equations[i][1]
            let ra = find(a), rb = find(b)
            if ra == rb {
                if abs(weight[a]! / weight[b]! - values[i]) > 1e-5 { return true }
            } else {
                parent[ra] = rb
                weight[ra] = values[i] * weight[b]! / weight[a]!
            }
        }
        return false
    }
}
