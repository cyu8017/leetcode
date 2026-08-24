// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution {
    func countDigits(_ num: Int) -> Int {
        var ans = 0, x = num
        while x > 0 {
            let d = x % 10
            if d != 0 && num % d == 0 { ans += 1 }
            x /= 10
        }
        return ans
    }
}
