// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution {
    func sumOfNumberAndReverse(_ num: Int) -> Bool {
        func rev(_ x: Int) -> Int {
            var x = x, r = 0
            while x > 0 {
                r = r * 10 + x % 10
                x /= 10
            }
            return r
        }
        for i in 0...num {
            if i + rev(i) == num { return true }
        }
        return false
    }
}
