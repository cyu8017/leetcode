// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

class Solution {
    func primeSubarray(_ nums: [Int], _ k: Int) -> Int {
        var mx = 0
        for v in nums { mx = max(mx, v) }
        var isPrime = Array(repeating: false, count: mx + 1)
        if mx >= 2 {
            for i in 2...mx { isPrime[i] = true }
            var i = 2
            while i * i <= mx {
                if isPrime[i] {
                    var j = i * i
                    while j <= mx { isPrime[j] = false; j += i }
                }
                i += 1
            }
        }
        let n = nums.count
        var ans = 0
        for l in 0..<n {
            var primes = [Int]()
            for r in l..<n {
                if isPrime[nums[r]] { primes.append(nums[r]) }
                if primes.count >= 2 {
                    var mn = primes[0], mxp = primes[0]
                    for p in primes { mn = min(mn, p); mxp = max(mxp, p) }
                    if mxp - mn <= k { ans += 1 }
                }
            }
        }
        return ans
    }
}
