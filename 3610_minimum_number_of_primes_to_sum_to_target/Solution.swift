// LeetCode 3610 - Minimum Number of Primes to Sum to Target
// https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

class Solution {
    func minNumberOfPrimes(_ n: Int, _ m: Int) -> Int {
        var primes = [Int]()
        var x = 2
        while primes.count < 1000 {
            var isPrime = true
            for p in primes {
                if p * p > x { break }
                if x % p == 0 { isPrime = false; break }
            }
            if isPrime { primes.append(x) }
            x += 1
        }
        let Inf = Int.max / 2
        var f = Array(repeating: Inf, count: n + 1)
        f[0] = 0
        for pi in 0..<m {
            let x = primes[pi]
            if x <= n {
                for i in x...n {
                    if f[i - x] + 1 < f[i] { f[i] = f[i - x] + 1 }
                }
            }
        }
        return f[n] < Inf ? f[n] : -1
    }
}
