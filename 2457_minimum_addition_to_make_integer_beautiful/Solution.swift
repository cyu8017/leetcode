// LeetCode 2457 - Minimum Addition to Make Integer Beautiful
// https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution {
    func makeIntegerBeautiful(_ n: Int, _ target: Int) -> Int {
        func digitSum(_ x: Int) -> Int {
            var x = x, s = 0
            while x > 0 {
                s += x % 10
                x /= 10
            }
            return s
        }
        var n = n
        let orig = n
        var pow10 = 1
        while digitSum(n) > target {
            n = n / 10 + 1
            pow10 *= 10
        }
        return n * pow10 - orig
    }
}
