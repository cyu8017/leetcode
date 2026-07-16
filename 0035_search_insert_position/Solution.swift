// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count

        while left < right {
            let mid = (left + right) / 2
            if nums[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }

        return left
    }
}
