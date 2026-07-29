// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution {
    func sumOfDigits(_ nums: [Int]) -> Int {
        var n = nums.min()!
        var digitSum = 0
        while n > 0 {
            digitSum += n % 10
            n /= 10
        }
        return digitSum % 2 == 0 ? 1 : 0
    }
}
