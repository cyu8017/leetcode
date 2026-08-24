// LeetCode 3940 - Limit Occurrences in Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/


class Solution {
    func limitOccurrences(_ nums: [Int], _ k: Int) -> [Int] {
        if nums.isEmpty { return [] }
        var nums = nums
        var cnt = 1, l = 1
        for r in 1..<nums.count {
            if nums[r] != nums[r - 1] { cnt = 1 }
            else { cnt += 1 }
            if cnt <= k {
                nums[l] = nums[r]
                l += 1
            }
        }
        return Array(nums.prefix(l))
    }
}
