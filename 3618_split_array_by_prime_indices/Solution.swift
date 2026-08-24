// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

class Solution {
    func splitArray(_ nums: [Int]) -> Int {
        let M = 100010
        var primes = Array(repeating: true, count: M)
        primes[0] = false; primes[1] = false
        for i in 2..<M {
            if primes[i] {
                var j = i + i
                while j < M { primes[j] = false; j += i }
            }
        }
        var ans = 0
        for i in 0..<nums.count {
            if primes[i] { ans += nums[i] } else { ans -= nums[i] }
        }
        return abs(ans)
    }
}
