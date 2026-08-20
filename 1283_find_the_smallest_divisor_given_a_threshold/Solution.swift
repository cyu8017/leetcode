// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    func smallestDivisor(_ nums: [Int], _ threshold: Int) -> Int {
        var lo = 1, hi = nums.max()!
        while lo < hi {
            let mid = (lo + hi) / 2
            let total = nums.reduce(0) { $0 + ($1 + mid - 1) / mid }
            if total > threshold { lo = mid + 1 } else { hi = mid }
        }
        return lo
    }
}
