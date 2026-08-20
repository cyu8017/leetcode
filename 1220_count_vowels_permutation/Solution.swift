// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

class Solution {
    func countVowelPermutation(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var a = 1, e = 1, i = 1, o = 1, u = 1
        if n == 1 { return 5 }
        for _ in 2...n {
            let na = (e + i + u) % MOD
            let ne = (a + i) % MOD
            let ni = (e + o) % MOD
            let no = i % MOD
            let nu = (i + o) % MOD
            a = na; e = ne; i = ni; o = no; u = nu
        }
        return (((((a + e) % MOD) + i) % MOD + o) % MOD + u) % MOD
    }
}
