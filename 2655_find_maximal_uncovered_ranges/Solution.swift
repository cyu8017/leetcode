// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

class Solution {
    func findMaximalUncoveredRanges(_ n: Int, _ ranges: [[Int]]) -> [[Int]] {
        let ranges = ranges.sorted { $0[0] < $1[0] }
        var ans: [[Int]] = []
        var cur = 0
        for r in ranges {
            if r[0] > cur { ans.append([cur, r[0] - 1]) }
            if r[1] + 1 > cur { cur = r[1] + 1 }
        }
        if cur < n { ans.append([cur, n - 1]) }
        return ans
    }
}
