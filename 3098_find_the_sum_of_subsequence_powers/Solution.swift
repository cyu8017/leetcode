// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution {
    private let MOD = 1_000_000_007
    private var nums: [Int] = []
    private var n = 0
    private var f: [Int: Int] = [:]

    func sumOfPowers(_ nums: [Int], _ k: Int) -> Int {
        self.nums = nums.sorted()
        self.n = nums.count
        self.f = [:]
        return dfs(0, n, k, 1_000_000_001)
    }

    private func dfs(_ i: Int, _ j: Int, _ kk: Int, _ mi: Int) -> Int {
        if i >= n { return kk == 0 ? mi : 0 }
        if n - i < kk { return 0 }
        let key = (mi << 18) | (i << 12) | (j << 6) | kk
        if let cached = f[key] { return cached }
        var ans = dfs(i + 1, j, kk, mi)
        if j == n {
            ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
        } else {
            ans = (ans + dfs(i + 1, i, kk - 1, min(mi, nums[i] - nums[j]))) % MOD
        }
        f[key] = ans
        return ans
    }
}
