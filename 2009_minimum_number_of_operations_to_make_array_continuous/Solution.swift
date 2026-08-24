// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        let uniq = Array(Set(nums)).sorted()
        var ans = n, j = 0
        for i in 0..<uniq.count {
            while j < uniq.count && uniq[j] - uniq[i] + 1 <= n { j += 1 }
            ans = min(ans, n - (j - i))
        }
        return ans
    }
}
