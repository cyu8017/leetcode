// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

class Solution {
    func minCost(_ nums: [Int]) -> Int {
        let n = nums.count
        var memo = [Int: Int]()
        func key(_ i: Int, _ prev: Int) -> Int { return (i << 32) | (prev & ((1 << 32) - 1)) }
        func max2(_ a: Int, _ b: Int) -> Int { a > b ? a : b }
        func min3(_ a: Int, _ b: Int, _ c: Int) -> Int { min(a, min(b, c)) }
        func dfs(_ i: Int, _ prev: Int) -> Int {
            if i >= n { return prev == -1 ? 0 : nums[prev] }
            let k = key(i, prev)
            if let c = memo[k] { return c }
            var res = 0
            if prev == -1 {
                if i + 1 >= n { res = nums[i] }
                else if i + 2 >= n { res = max2(nums[i], nums[i + 1]) }
                else {
                    let a = nums[i], b = nums[i + 1], c = nums[i + 2]
                    res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2))
                }
            } else {
                if i + 1 >= n { res = max2(nums[prev], nums[i]) }
                else {
                    let a = nums[prev], b = nums[i], c = nums[i + 1]
                    res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1))
                }
            }
            memo[k] = res
            return res
        }
        return dfs(0, -1)
    }
}
