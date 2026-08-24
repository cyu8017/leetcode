// LeetCode 3974 - Maximum Total Sum of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/


class Solution {
    func maxSum(_ nums: [Int], _ k: Int, _ mul: Int) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var ans = 0
        var mul = mul
        for i in stride(from: n - 1, through: n - k, by: -1) {
            let m = max(1, mul)
            ans += nums[i] * m
            mul -= 1
        }
        return ans
    }
}
