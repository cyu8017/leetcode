// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

class Solution {
    private static let MX = 200000
    private static let isPrime: [Bool] = {
        var ip = [Bool](repeating: true, count: MX + 1)
        ip[0] = false
        ip[1] = false
        var i = 2
        while i <= MX / i {
            if ip[i] {
                var j = i * i
                while j <= MX {
                    ip[j] = false
                    j += i
                }
            }
            i += 1
        }
        return ip
    }()
    private static let primes: [Int] = {
        var p = [Int]()
        for i in 2...MX where isPrime[i] { p.append(i) }
        return p
    }()

    func minOperations(_ nums: [Int]) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            let x = nums[i]
            if i % 2 == 0 {
                var lo = 0, hi = Solution.primes.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if Solution.primes[mid] < x { lo = mid + 1 }
                    else { hi = mid }
                }
                ans += Solution.primes[lo] - x
            } else if Solution.isPrime[x] {
                ans += (x == 2) ? 2 : 1
            }
        }
        return ans
    }
}
