// LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution {
    func minimumSum(_ num: Int) -> Int {
        var d = [num / 1000, (num / 100) % 10, (num / 10) % 10, num % 10]
        d.sort()
        return 10 * d[0] + d[2] + 10 * d[1] + d[3]
    }
}
