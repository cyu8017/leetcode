// LeetCode 0372 - Super Pow
// https://leetcode.com/problems/super-pow/

class Solution {
    func superPow(_ a: Int, _ b: [Int]) -> Int {
        let mod = 1337
        var base = a % mod
        var result = 1

        for digit in b {
            result = powMod(result, 10, mod) * powMod(base, digit, mod) % mod
        }

        return result
    }

    private func powMod(_ base: Int, _ exponent: Int, _ mod: Int) -> Int {
        var value = base
        var power = exponent
        var result = 1

        while power > 0 {
            if power & 1 == 1 {
                result = result * value % mod
            }
            value = value * value % mod
            power >>= 1
        }

        return result
    }
}
