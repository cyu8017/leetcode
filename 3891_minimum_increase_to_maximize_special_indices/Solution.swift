// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    private var nums = [Int]()
    private var f = [[Int]]()
    private var n = 0

    func minIncrease(_ nums: [Int]) -> Int {
        self.nums = nums
        n = nums.count
        f = Array(repeating: [-1, -1], count: n)
        return dfs(1, (n & 1) ^ 1)
    }

    private func dfs(_ i: Int, _ j: Int) -> Int {
        if i >= n - 1 { return 0 }
        if f[i][j] != -1 { return f[i][j] }
        let cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        var ans = cost + dfs(i + 2, j)
        if j > 0 { ans = min(ans, dfs(i + 1, 0)) }
        f[i][j] = ans
        return ans
    }
}
