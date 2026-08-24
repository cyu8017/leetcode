// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution {
    func countMaxOrSubsets(_ nums: [Int]) -> Int {
        let maxOr = nums.reduce(0, |)
        var ans = 0
        func dfs(_ i: Int, _ cur: Int) {
            if i == nums.count {
                if cur == maxOr { ans += 1 }
                return
            }
            dfs(i + 1, cur)
            dfs(i + 1, cur | nums[i])
        }
        dfs(0, 0)
        return ans
    }
}
