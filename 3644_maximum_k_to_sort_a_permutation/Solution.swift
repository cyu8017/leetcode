// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

class Solution {
    func sortPermutation(_ nums: [Int]) -> Int {
        var ans = -1
        for i in 0..<nums.count {
            if i != nums[i] { ans &= nums[i] }
        }
        return max(ans, 0)
    }
}
