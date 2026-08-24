// LeetCode 0878 - Nth Magical Number
// https://leetcode.com/problems/nth-magical-number/

class Solution {
    func nthMagicalNumber(_ n: Int, _ a: Int, _ b: Int) -> Int {
        let mod = 1_000_000_007
        func gcd(_ x: Int, _ y: Int) -> Int {
            var x = x, y = y
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        let lcm = a / gcd(a, b) * b
        var lo = 1, hi = n * min(a, b)
        while lo < hi {
            let mid = (lo + hi) / 2
            if mid / a + mid / b - mid / lcm >= n { hi = mid }
            else { lo = mid + 1 }
        }
        return lo % mod
    }
}
