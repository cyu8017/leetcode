// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        if nums.count <= 1 { return nums }
        let mid = nums.count / 2
        let left = sortArray(Array(nums[..<mid]))
        let right = sortArray(Array(nums[mid...]))
        var merged = [Int]()
        var i = 0, j = 0
        while i < left.count && j < right.count {
            if left[i] <= right[j] { merged.append(left[i]); i += 1 }
            else { merged.append(right[j]); j += 1 }
        }
        if i < left.count { merged.append(contentsOf: left[i...]) }
        if j < right.count { merged.append(contentsOf: right[j...]) }
        return merged
    }
}
