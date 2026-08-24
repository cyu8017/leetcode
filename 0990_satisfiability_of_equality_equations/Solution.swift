// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution {
    func equationsPossible(_ equations: [String]) -> Bool {
        var parent = Array(0..<26)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        for eq in equations {
            let chars = Array(eq)
            if chars[1] == "=" {
                parent[find(Int(chars[0].asciiValue! - 97))] = find(Int(chars[3].asciiValue! - 97))
            }
        }
        for eq in equations {
            let chars = Array(eq)
            if chars[1] == "!" && find(Int(chars[0].asciiValue! - 97)) == find(Int(chars[3].asciiValue! - 97)) {
                return false
            }
        }
        return true
    }
}
