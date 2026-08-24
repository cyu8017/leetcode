// LeetCode 2624 - Snail Traversal
// https://leetcode.com/problems/snail-traversal/

class Solution {
    func snail(_ nums: [Int], _ rowsCount: Int, _ colsCount: Int) -> [[Int]] {
        if rowsCount * colsCount != nums.count { return [] }
        var ans = Array(repeating: Array(repeating: 0, count: colsCount), count: rowsCount)
        var idx = 0
        for c in 0..<colsCount {
            if c % 2 == 0 {
                for r in 0..<rowsCount {
                    ans[r][c] = nums[idx]
                    idx += 1
                }
            } else {
                for r in stride(from: rowsCount - 1, through: 0, by: -1) {
                    ans[r][c] = nums[idx]
                    idx += 1
                }
            }
        }
        return ans
    }
}
