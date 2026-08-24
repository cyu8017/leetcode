// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution {
    func generateKey(_ num1: Int, _ num2: Int, _ num3: Int) -> Int {
        var a = num1, b = num2, c = num3
        var ans = 0, mul = 1
        for _ in 0..<4 {
            ans += min(a % 10, min(b % 10, c % 10)) * mul
            mul *= 10
            a /= 10; b /= 10; c /= 10
        }
        return ans
    }
}
