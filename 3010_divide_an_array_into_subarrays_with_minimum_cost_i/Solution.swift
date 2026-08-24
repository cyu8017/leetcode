// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        let a = nums[0]
        var b = 100, c = 100
        for i in 1..<nums.count {
            let x = nums[i]
            if x < b {
                c = b
                b = x
            } else if x < c {
                c = x
            }
        }
        return a + b + c
    }
}
