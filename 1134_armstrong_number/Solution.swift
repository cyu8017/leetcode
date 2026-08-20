// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    func isArmstrong(_ n: Int) -> Bool {
        let s = String(n)
        let k = s.count
        var total = 0
        var x = n
        while x > 0 {
            let d = x % 10
            var p = 1
            for _ in 0..<k { p *= d }
            total += p
            x /= 10
        }
        return total == n
    }
}
