// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution {
    func separateDigits(_ nums: [Int]) -> [Int] {
        var ans = [Int]()
        for num in nums {
            var digits = [Int]()
            var x = num
            while x > 0 {
                digits.append(x % 10)
                x /= 10
            }
            ans += digits.reversed()
        }
        return ans
    }
}
