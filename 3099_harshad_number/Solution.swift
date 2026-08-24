// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

class Solution {
    func sumOfTheDigitsOfHarshadNumber(_ x: Int) -> Int {
        var s = 0, y = x
        while y > 0 {
            s += y % 10
            y /= 10
        }
        return x % s == 0 ? s : -1
    }
}
