// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution {
    func answerQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        var nums = nums.sorted()
        if nums.count > 1 {
            for i in 1..<nums.count { nums[i] += nums[i - 1] }
        }
        return queries.map { q in
            var lo = 0, hi = nums.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if nums[mid] <= q { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
    }
}
