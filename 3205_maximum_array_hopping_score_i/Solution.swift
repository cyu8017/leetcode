// LeetCode 3205 - Maximum Array Hopping Score I
// https://leetcode.com/problems/maximum-array-hopping-score-i/

class Solution {
    private var nums: [Int] = []
    private var f: [Int] = []
    private var n = 0

    func maxScore(_ nums: [Int]) -> Int {
        self.nums = nums
        n = nums.count
        f = Array(repeating: 0, count: n)
        return dfs(0)
    }

    private func dfs(_ i: Int) -> Int {
        if f[i] > 0 { return f[i] }
        if i + 1 < n {
            for j in (i + 1)..<n {
                f[i] = max(f[i], (j - i) * nums[j] + dfs(j))
            }
        }
        return f[i]
    }
}
