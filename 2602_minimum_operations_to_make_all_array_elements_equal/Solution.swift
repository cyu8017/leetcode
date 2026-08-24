// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution {
    func minOperations(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let nums = nums.sorted()
        let n = nums.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + nums[i] }
        func lowerBound(_ x: Int) -> Int {
            var lo = 0, hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if nums[mid] < x { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
        return queries.map { q in
            let i = lowerBound(q)
            let left = q * i - pref[i]
            let right = pref[n] - pref[i] - q * (n - i)
            return left + right
        }
    }
}
