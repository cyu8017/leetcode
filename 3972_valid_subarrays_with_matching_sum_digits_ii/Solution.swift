// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/


class Solution {
    func countValidSubarrays(_ nums: [Int], _ x: Int) -> Int {
        var byRemainder = Array(repeating: [Int](), count: 10)
        byRemainder[0].append(0)
        var prefix = 0, answer = 0
        func lowerBound(_ a: [Int], _ x: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] < x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        func upperBound(_ a: [Int], _ x: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] <= x { lo = mid + 1 }
                else { hi = mid }
            }
            return lo
        }
        for value in nums {
            prefix += value
            let required = ((prefix - x) % 10 + 10) % 10
            let values = byRemainder[required]
            var power = 1
            while x * power <= prefix {
                let low = x * power
                let high = (x + 1) * power - 1
                let minPrefix = prefix - high, maxPrefix = prefix - low
                let left = lowerBound(values, minPrefix)
                let right = upperBound(values, maxPrefix)
                answer += right - left
                if power > prefix / 10 { break }
                power *= 10
            }
            byRemainder[prefix % 10].append(prefix)
        }
        return answer
    }
}
