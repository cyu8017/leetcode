// LeetCode 2543 - Check if Point Is Reachable
// https://leetcode.com/problems/check-if-point-is-reachable/

class Solution {
    func isReachable(_ targetX: Int, _ targetY: Int) -> Bool {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var g = gcd(targetX, targetY)
        while g % 2 == 0 { g /= 2 }
        return g == 1
    }
}
