// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        var nums = nums.sorted()
        let n = nums.count
        let mid = (n + 1) / 2
        let small = Array(nums[..<mid])
        let large = Array(nums[mid...])
        var ans: [Int] = []
        var i = 0, j = 0
        while i < small.count || j < large.count {
            if i < small.count { ans.append(small[i]); i += 1 }
            if j < large.count { ans.append(large[j]); j += 1 }
        }
        return ans
    }
}
