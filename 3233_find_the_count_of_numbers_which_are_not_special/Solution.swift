// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution {
    private static let M = 31623
    private static var primes: [Bool] = []
    private static var inited = false

    private static func initPrimes() {
        if inited { return }
        primes = Array(repeating: true, count: M + 1)
        primes[0] = false
        primes[1] = false
        for i in 2...M where primes[i] {
            var j = i * 2
            while j <= M {
                primes[j] = false
                j += i
            }
        }
        inited = true
    }

    func nonSpecialCount(_ l: Int, _ r: Int) -> Int {
        Solution.initPrimes()
        let lo = Int(ceil(sqrt(Double(l))))
        let hi = Int(floor(sqrt(Double(r))))
        var cnt = 0
        if lo <= hi {
            for i in lo...hi where Solution.primes[i] { cnt += 1 }
        }
        return r - l + 1 - cnt
    }
}
