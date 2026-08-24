// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

class Solution {
    func mirrorReflection(_ p: Int, _ q: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var p = p, q = q
        let g = gcd(p, q)
        p /= g
        q /= g
        if p % 2 == 0 { return 2 }
        if q % 2 == 0 { return 0 }
        return 1
    }
}
