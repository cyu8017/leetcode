// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

class Solution {
    func sortColors(_ nums: inout [Int]) {
        var low = 0
        var mid = 0
        var high = nums.count - 1

        while mid <= high {
            if nums[mid] == 0 {
                nums.swapAt(low, mid)
                low += 1
                mid += 1
            } else if nums[mid] == 1 {
                mid += 1
            } else {
                nums.swapAt(mid, high)
                high -= 1
            }
        }
    }
}
