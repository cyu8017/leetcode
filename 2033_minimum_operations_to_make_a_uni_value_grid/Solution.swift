// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution {
    func minOperations(_ grid: [[Int]], _ x: Int) -> Int {
        var vals = [Int]()
        let bas = grid[0][0] % x
        for row in grid {
            for v in row {
                if v % x != bas { return -1 }
                vals.append(v)
            }
        }
        vals.sort()
        let median = vals[vals.count / 2]
        return vals.reduce(0) { $0 + abs($1 - median) / x }
    }
}
