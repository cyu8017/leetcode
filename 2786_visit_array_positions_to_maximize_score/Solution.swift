// LeetCode 2786 - Visit Array Positions to Maximize Score
// https://leetcode.com/problems/visit-array-positions-to-maximize-score/

class Solution {
    func maxScore(_ nums: [Int], _ x: Int) -> Int {
        let NEG = -(1 << 60)
        var even = nums[0], odd = nums[0]
        if nums[0] % 2 == 0 { odd = NEG } else { even = NEG }
        for i in 1..<nums.count {
            let v = nums[i]
            if v % 2 == 0 {
                even = max(even + v, odd + v - x)
            } else {
                odd = max(odd + v, even + v - x)
            }
        }
        return max(even, odd)
    }
}
