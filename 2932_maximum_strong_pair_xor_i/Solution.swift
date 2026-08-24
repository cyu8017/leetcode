// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution {
    func maximumStrongPairXor(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            for j in i..<nums.count {
                let x = nums[i], y = nums[j]
                if abs(x - y) <= min(x, y) {
                    ans = max(ans, x ^ y)
                }
            }
        }
        return ans
    }
}
