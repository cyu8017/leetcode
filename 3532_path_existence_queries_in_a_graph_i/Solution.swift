// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

class Solution {
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Bool] {
        var g = Array(repeating: 0, count: n)
        var cnt = 0
        if n > 1 {
            for i in 1..<n {
                if nums[i] - nums[i - 1] > maxDiff { cnt += 1 }
                g[i] = cnt
            }
        }
        return queries.map { g[$0[0]] == g[$0[1]] }
    }
}
