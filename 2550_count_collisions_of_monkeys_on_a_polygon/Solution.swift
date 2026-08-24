// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
    func monkeyMove(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        func powMod(_ a: Int, _ e: Int) -> Int {
            var a = a, e = e, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % MOD }
                a = a * a % MOD
                e >>= 1
            }
            return res
        }
        return (powMod(2, n) - 2 + MOD) % MOD
    }
}
