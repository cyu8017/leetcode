// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/


class Solution {
    func maxDigitRange(_ nums: [Int]) -> Int {
        var mx = 0, ans = 0
        for x in nums {
            var a = 10, b = 0, y = x
            while y > 0 {
                let v = y % 10
                a = min(a, v)
                b = max(b, v)
                y /= 10
            }
            let r = b - a
            if mx < r {
                mx = r
                ans = x
            } else if mx == r {
                ans += x
            }
        }
        return ans
    }
}
