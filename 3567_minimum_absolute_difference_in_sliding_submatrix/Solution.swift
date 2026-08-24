// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution {
    func minAbsDiff(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var ans = Array(repeating: Array(repeating: 0, count: n - k + 1), count: m - k + 1)
        for i in 0...(m - k) {
            for j in 0...(n - k) {
                var nums = [Int]()
                for x in i..<(i + k) {
                    for y in j..<(j + k) { nums.append(grid[x][y]) }
                }
                nums.sort()
                var d = Int.max
                if nums.count > 1 {
                    for t in 1..<nums.count {
                        if nums[t] != nums[t - 1] { d = min(d, abs(nums[t] - nums[t - 1])) }
                    }
                }
                if d != Int.max { ans[i][j] = d }
            }
        }
        return ans
    }
}
