// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution {
    private let INF = 1 << 29
    private var nums: [Int] = []
    private var andValues: [Int] = []
    private var n = 0, m = 0
    private var f: [Int: Int] = [:]

    func minimumValueSum(_ nums: [Int], _ andValues: [Int]) -> Int {
        self.nums = nums
        self.andValues = andValues
        self.n = nums.count
        self.m = andValues.count
        self.f = [:]
        let ans = dfs(0, 0, -1)
        return ans < INF ? ans : -1
    }

    private func dfs(_ i: Int, _ j: Int, _ a: Int) -> Int {
        if n - i < m - j { return INF }
        if j == m { return i == n ? 0 : INF }
        let a2 = a & nums[i]
        if a2 < andValues[j] { return INF }
        let key = (i << 36) | (j << 32) | (a2 & 0xffffffff)
        if let cached = f[key] { return cached }
        var ans = dfs(i + 1, j, a2)
        if a2 == andValues[j] {
            ans = min(ans, dfs(i + 1, j + 1, -1) + nums[i])
        }
        f[key] = ans
        return ans
    }
}
