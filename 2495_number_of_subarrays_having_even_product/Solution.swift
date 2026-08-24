// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

class Solution {
    func evenProduct(_ nums: [Int]) -> Int {
        let n = nums.count
        let total = n * (n + 1) / 2
        var oddLen = 0, odd = 0
        for x in nums {
            if x % 2 == 1 {
                odd += 1
                oddLen += odd
            } else {
                odd = 0
            }
        }
        return total - oddLen
    }
}
