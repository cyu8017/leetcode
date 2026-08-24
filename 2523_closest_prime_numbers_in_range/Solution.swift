// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution {
    func closestPrimes(_ left: Int, _ right: Int) -> [Int] {
        var isPrime = [Bool](repeating: true, count: right + 1)
        if right >= 0 { isPrime[0] = false }
        if right >= 1 { isPrime[1] = false }
        var i = 2
        while i * i <= right {
            if isPrime[i] {
                var j = i * i
                while j <= right {
                    isPrime[j] = false
                    j += i
                }
            }
            i += 1
        }
        var primes = [Int]()
        if left <= right {
            for x in left...right where isPrime[x] { primes.append(x) }
        }
        if primes.count < 2 { return [-1, -1] }
        var bestDiff = Int.max
        var best = [-1, -1]
        for i in 0..<(primes.count - 1) {
            let d = primes[i + 1] - primes[i]
            if d < bestDiff {
                bestDiff = d
                best = [primes[i], primes[i + 1]]
            }
        }
        return best
    }
}
