// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution {
    func differenceOfSum(_ nums: [Int]) -> Int {
        var elem = 0, digit = 0
        for num in nums {
            elem += num
            var x = num
            while x > 0 {
                digit += x % 10
                x /= 10
            }
        }
        return abs(elem - digit)
    }
}
