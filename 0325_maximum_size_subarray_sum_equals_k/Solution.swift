// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution {
    func maxSubArrayLen(_ nums: [Int], _ k: Int) -> Int {
        var prefixIndex: [Int: Int] = [0: -1]
        var prefix = 0
        var best = 0
        for (index, num) in nums.enumerated() {
            prefix += num
            if let start = prefixIndex[prefix - k] {
                best = max(best, index - start)
            }
            if prefixIndex[prefix] == nil {
                prefixIndex[prefix] = index
            }
        }
        return best
    }
}
