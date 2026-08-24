// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution {
    func countWays(_ ranges: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let ranges = ranges.sorted { $0[0] < $1[0] }
        var groups = 0, end = -1
        for r in ranges {
            if r[0] > end {
                groups += 1
                end = r[1]
            } else if r[1] > end {
                end = r[1]
            }
        }
        var ans = 1
        for _ in 0..<groups { ans = ans * 2 % MOD }
        return ans
    }
}
