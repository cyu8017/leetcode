// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

class Solution {
    func numPrimeArrangements(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        func isPrime(_ x: Int) -> Bool {
            if x < 2 { return false }
            var i = 2
            while i * i <= x {
                if x % i == 0 { return false }
                i += 1
            }
            return true
        }
        var primes = 0
        for i in 1...n where isPrime(i) { primes += 1 }
        func fact(_ x: Int) -> Int {
            var r = 1
            if x >= 1 {
                for i in 1...x { r = r * i % MOD }
            }
            return r
        }
        return fact(primes) * fact(n - primes) % MOD
    }
}
