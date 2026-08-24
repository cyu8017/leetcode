// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

class Solution {
    func simulationResult(_ windows: [Int], _ queries: [Int]) -> [Int] {
        let n = windows.count
        var s = Array(repeating: false, count: n + 1)
        var ans: [Int] = []
        for i in stride(from: queries.count - 1, through: 0, by: -1) {
            let q = queries[i]
            if !s[q] {
                s[q] = true
                ans.append(q)
            }
        }
        for w in windows where !s[w] { ans.append(w) }
        return ans
    }
}
