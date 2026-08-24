// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution {
    func canSortArray(_ nums: [Int]) -> Bool {
        var preMx = 0
        var i = 0
        let n = nums.count
        while i < n {
            let cnt = nums[i].nonzeroBitCount
            var j = i + 1
            var mi = nums[i], mx = nums[i]
            while j < n && nums[j].nonzeroBitCount == cnt {
                mi = min(mi, nums[j])
                mx = max(mx, nums[j])
                j += 1
            }
            if preMx > mi { return false }
            preMx = mx
            i = j
        }
        return true
    }
}
