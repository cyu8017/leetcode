// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution {
    func maximumImportance(_ n: Int, _ roads: [[Int]]) -> Int {
        var deg = [Int](repeating: 0, count: n)
        for r in roads {
            deg[r[0]] += 1
            deg[r[1]] += 1
        }
        deg.sort()
        var ans = 0
        for i in 0..<n { ans += deg[i] * (i + 1) }
        return ans
    }
}
