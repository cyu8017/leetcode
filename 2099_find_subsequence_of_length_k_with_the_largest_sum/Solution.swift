// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution {
    func maxSubsequence(_ nums: [Int], _ k: Int) -> [Int] {
        let idx = nums.enumerated().sorted { $0.element > $1.element }.prefix(k).map { $0.offset }.sorted()
        return idx.map { nums[$0] }
    }
}
