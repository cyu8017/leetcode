// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution {
    func checkDivisibility(_ n: Int) -> Bool {
        var s = 0, p = 1, x = n
        while x != 0 {
            let v = x % 10
            x /= 10
            s += v
            p *= v
        }
        return n % (s + p) == 0
    }
}
