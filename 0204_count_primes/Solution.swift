// LeetCode 0204 - Count Primes
// https://leetcode.com/problems/count-primes/

class Solution {
    func countPrimes(_ n: Int) -> Int {
        guard n > 2 else { return 0 }
        var isPrime = Array(repeating: true, count: n)
        isPrime[0] = false
        isPrime[1] = false
        var p = 2
        while p * p < n {
            if isPrime[p] {
                var multiple = p * p
                while multiple < n {
                    isPrime[multiple] = false
                    multiple += p
                }
            }
            p += 1
        }
        return isPrime.filter { $0 }.count
    }
}