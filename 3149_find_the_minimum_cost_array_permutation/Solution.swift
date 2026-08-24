// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

class Solution {
    private var nums: [Int] = []
    private var n = 0
    private var memo: [[Int]] = []
    private var ans: [Int] = []

    func findPermutation(_ nums: [Int]) -> [Int] {
        self.nums = nums
        self.n = nums.count
        self.memo = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)
        self.ans = []
        g(1, 0)
        return ans
    }

    private func dfs(_ mask: Int, _ pre: Int) -> Int {
        if mask == (1 << n) - 1 { return abs(pre - nums[0]) }
        if memo[mask][pre] != -1 { return memo[mask][pre] }
        var res = Int.max
        for cur in 1..<n where ((mask >> cur) & 1) == 0 {
            res = min(res, abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur))
        }
        memo[mask][pre] = res
        return res
    }

    private func g(_ mask: Int, _ pre: Int) {
        ans.append(pre)
        if mask == (1 << n) - 1 { return }
        let res = dfs(mask, pre)
        for cur in 1..<n where ((mask >> cur) & 1) == 0 {
            if abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur) == res {
                g(mask | (1 << cur), cur)
                break
            }
        }
    }
}
