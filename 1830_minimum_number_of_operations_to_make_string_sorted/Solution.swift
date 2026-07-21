// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

class Solution {
    func makeStringSorted(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var fact = Array(repeating: 1, count: n + 1)
        if n >= 2 {
            for i in 2...n {
                fact[i] = Int((Int64(fact[i - 1]) * Int64(i)) % Int64(mod))
            }
        }
        var invFact = Array(repeating: 1, count: n + 1)
        invFact[n] = modPow(fact[n], mod - 2, mod)
        for i in stride(from: n - 1, through: 0, by: -1) {
            invFact[i] = Int((Int64(invFact[i + 1]) * Int64(i + 1)) % Int64(mod))
        }

        var freq = Array(repeating: 0, count: 26)
        for ch in chars {
            freq[Int(ch.asciiValue! - Character("a").asciiValue!)] += 1
        }

        var ans = 0
        for i in 0..<n {
            let c = Int(chars[i].asciiValue! - Character("a").asciiValue!)
            for smaller in 0..<c where freq[smaller] > 0 {
                freq[smaller] -= 1
                var ways = fact[n - i - 1]
                for count in freq {
                    ways = Int((Int64(ways) * Int64(invFact[count])) % Int64(mod))
                }
                ans = (ans + ways) % mod
                freq[smaller] += 1
            }
            freq[c] -= 1
        }
        return ans
    }

    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var b = Int64(base % mod)
        var e = exp
        var res: Int64 = 1
        let m = Int64(mod)
        while e > 0 {
            if e & 1 == 1 { res = res * b % m }
            b = b * b % m
            e >>= 1
        }
        return Int(res)
    }
}
