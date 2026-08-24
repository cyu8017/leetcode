// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution {
    private var nums: [Int] = []
    private var f: [[Int]] = []
    private var s = 0

    func maxOperations(_ nums: [Int]) -> Int {
        self.nums = nums
        let n = nums.count
        let a = g(2, n - 1, nums[0] + nums[1])
        let b = g(0, n - 3, nums[n - 1] + nums[n - 2])
        let c = g(1, n - 2, nums[0] + nums[n - 1])
        return 1 + max(a, max(b, c))
    }

    private func g(_ i0: Int, _ j0: Int, _ score: Int) -> Int {
        let n = nums.count
        f = Array(repeating: Array(repeating: -1, count: n), count: n)
        s = score
        return dfs(i0, j0)
    }

    private func dfs(_ i: Int, _ j: Int) -> Int {
        if j - i < 1 { return 0 }
        if f[i][j] != -1 { return f[i][j] }
        var ans = 0
        if nums[i] + nums[i + 1] == s { ans = max(ans, 1 + dfs(i + 2, j)) }
        if nums[i] + nums[j] == s { ans = max(ans, 1 + dfs(i + 1, j - 1)) }
        if nums[j - 1] + nums[j] == s { ans = max(ans, 1 + dfs(i, j - 2)) }
        f[i][j] = ans
        return ans
    }
}
