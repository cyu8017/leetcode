// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

class Solution {
    func countAnagrams(_ s: String) -> Int {
        let MOD = 1_000_000_007
        func modPow(_ a: Int, _ e: Int) -> Int {
            var a = a % MOD, e = e, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % MOD }
                a = a * a % MOD
                e >>= 1
            }
            return res
        }
        let words = s.split(separator: " ").map(String.init)
        let maxN = words.map(\.count).max() ?? 0
        var fact = [Int](repeating: 1, count: maxN + 1)
        var invFact = [Int](repeating: 1, count: maxN + 1)
        if maxN >= 1 {
            for i in 1...maxN { fact[i] = fact[i - 1] * i % MOD }
        }
        invFact[maxN] = modPow(fact[maxN], MOD - 2)
        if maxN >= 1 {
            for i in stride(from: maxN, through: 1, by: -1) {
                invFact[i - 1] = invFact[i] * i % MOD
            }
        }
        var ans = 1
        for word in words {
            var cnt = [Int](repeating: 0, count: 26)
            for c in word {
                cnt[Int(c.asciiValue! - Character("a").asciiValue!)] += 1
            }
            var cur = fact[word.count]
            for c in cnt { cur = cur * invFact[c] % MOD }
            ans = ans * cur % MOD
        }
        return ans
    }
}
