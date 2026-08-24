// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

class Solution {
    func maximumStrongPairXor(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var ans = 0
        for i in 0..<nums.count {
            let x = nums[i]
            var j = i
            while j < nums.count && nums[j] <= 2 * x {
                ans = max(ans, x ^ nums[j])
                j += 1
            }
        }
        return ans
    }
}
