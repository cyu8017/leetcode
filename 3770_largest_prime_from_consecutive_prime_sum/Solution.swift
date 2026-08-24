// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

class Solution {
    private static let MX = 500000
    private static let S: [Int] = {
        var isPrime = [Bool](repeating: true, count: MX + 1)
        isPrime[0] = false
        isPrime[1] = false
        var primes = [Int]()
        for i in 2...MX {
            if isPrime[i] {
                primes.append(i)
                if i * i <= MX {
                    var j = i * i
                    while j <= MX {
                        isPrime[j] = false
                        j += i
                    }
                }
            }
        }
        var s = [0]
        var t = 0
        for x in primes {
            t += x
            if t > MX { break }
            if isPrime[t] { s.append(t) }
        }
        return s
    }()

    func largestPrime(_ n: Int) -> Int {
        var lo = 0, hi = Solution.S.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.S[mid] <= n { lo = mid + 1 }
            else { hi = mid }
        }
        return Solution.S[lo - 1]
    }
}
