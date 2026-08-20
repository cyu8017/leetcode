// LeetCode 1201 - Ugly Number III
// https://leetcode.com/problems/ugly-number-iii/

class Solution {
    func nthUglyNumber(_ n: Int, _ a: Int, _ b: Int, _ c: Int) -> Int {
        func gcd(_ x: Int, _ y: Int) -> Int {
            var x = x, y = y
            while y != 0 { let t = y; y = x % y; x = t }
            return x
        }
        func lcm(_ x: Int, _ y: Int) -> Int { x / gcd(x, y) * y }
        let ab = lcm(a, b), ac = lcm(a, c), bc = lcm(b, c), abc = lcm(ab, c)
        func count(_ x: Int) -> Int {
            x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc
        }
        var lo = 1, hi = 2_000_000_000
        while lo < hi {
            let mid = (lo + hi) / 2
            if count(mid) < n { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
