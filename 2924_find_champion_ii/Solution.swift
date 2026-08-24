// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

class Solution {
    func findChampion(_ n: Int, _ edges: [[Int]]) -> Int {
        var indeg = Array(repeating: 0, count: n)
        for e in edges { indeg[e[1]] += 1 }
        var ans = -1
        for i in 0..<n where indeg[i] == 0 {
            if ans != -1 { return -1 }
            ans = i
        }
        return ans
    }
}
