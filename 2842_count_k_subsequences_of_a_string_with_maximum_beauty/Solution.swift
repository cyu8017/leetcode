// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

class Solution {
    private let mod = 1_000_000_007

    func countKSubsequencesWithMaxBeauty(_ s: String, _ k: Int) -> Int {
        var freq = Array(repeating: 0, count: 26)
        let aVal = Int(Character("a").asciiValue!)
        for c in s {
            freq[Int(c.asciiValue!) - aVal] += 1
        }
        var vals: [Int] = []
        for f in freq where f > 0 { vals.append(f) }
        if vals.count < k { return 0 }
        vals.sort(by: >)
        let threshold = vals[k - 1]
        var need = 0, avail = 0
        var prod = 1
        for v in vals {
            if v > threshold {
                prod = prod * v % mod
                need += 1
            } else if v == threshold {
                avail += 1
            }
        }
        let remain = k - need
        prod = prod * comb(avail, remain) % mod
        for _ in 0..<remain {
            prod = prod * threshold % mod
        }
        return prod
    }

    private func modPow(_ a0: Int, _ b0: Int) -> Int {
        var a = a0 % mod, b = b0, res = 1
        while b > 0 {
            if b & 1 != 0 { res = res * a % mod }
            a = a * a % mod
            b >>= 1
        }
        return res
    }

    private func comb(_ n: Int, _ r: Int) -> Int {
        if r < 0 || r > n { return 0 }
        var num = 1, den = 1
        for i in 0..<r {
            num = num * (n - i) % mod
            den = den * (i + 1) % mod
        }
        return num * modPow(den, mod - 2) % mod
    }
}
