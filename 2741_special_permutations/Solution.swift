// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

class Solution {
    private let MOD = 1_000_000_007
    private var nums: [Int] = []
    private var memo: [[Int]] = []

    func specialPerm(_ nums: [Int]) -> Int {
        self.nums = nums
        let n = nums.count
        memo = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)
        var ans = 0
        for i in 0..<n { ans = (ans + dfs(1 << i, i)) % MOD }
        return ans
    }

    private func dfs(_ mask: Int, _ last: Int) -> Int {
        if mask == (1 << nums.count) - 1 { return 1 }
        if memo[mask][last] != -1 { return memo[mask][last] }
        var res = 0
        for i in 0..<nums.count {
            if (mask & (1 << i)) != 0 { continue }
            if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0 {
                res = (res + dfs(mask | (1 << i), i)) % MOD
            }
        }
        memo[mask][last] = res
        return res
    }
}
