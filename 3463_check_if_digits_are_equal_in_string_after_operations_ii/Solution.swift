// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

class Solution {
    func hasSameDigits(_ s: String) -> Bool {
        let n = s.count
        return combineDigit(s, n, 0) == combineDigit(s, n, 1)
    }

    private func modPowP(_ a: Int, _ e: Int, _ p: Int) -> Int {
        var r = 1, a = a, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % p }
            a = a * a % p
            e >>= 1
        }
        return r
    }

    private func binomMod(_ n: Int, _ k: Int, _ p: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var num = 1, den = 1
        if k > 0 {
            for i in 0..<k {
                num = num * (n - i) % p
                den = den * (i + 1) % p
            }
        }
        return num * modPowP(den, p - 2, p) % p
    }

    private func crt(_ a1: Int, _ m1: Int, _ a2: Int, _ m2: Int) -> Int {
        for x in 0..<(m1 * m2) {
            if x % m1 == a1 && x % m2 == a2 { return x }
        }
        return 0
    }

    private func binomMod10(_ n: Int, _ k: Int) -> Int {
        return crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
    }

    private func combineDigit(_ s: String, _ n: Int, _ offset: Int) -> Int {
        let chars = Array(s)
        var sum = 0
        if n >= 2 {
            for i in 0...(n - 2) {
                sum = (sum + binomMod10(n - 2, i) * Int(chars[i + offset].asciiValue! - 48)) % 10
            }
        }
        return sum
    }
}
