// LeetCode 3959 - Check Good Integer
// https://leetcode.com/problems/check-good-integer/


class Solution {
    func checkGoodInteger(_ n: Int) -> Bool {
        var n = n, s = 0
        while n > 0 {
            let x = n % 10
            s += x * (x - 1)
            n /= 10
        }
        return s >= 50
    }
}
