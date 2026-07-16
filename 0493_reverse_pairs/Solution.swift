// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

class Solution {
    func reversePairs(_ nums: [Int]) -> Int {
        var values = nums
        return mergeSort(0, values.count - 1, &values)
    }

    private func mergeSort(_ start: Int, _ end: Int, _ nums: inout [Int]) -> Int {
        if start >= end {
            return 0
        }
        let mid = (start + end) / 2
        var count = mergeSort(start, mid, &nums) + mergeSort(mid + 1, end, &nums)
        var j = mid + 1
        for i in start...mid {
            while j <= end && nums[i] > 2 * nums[j] {
                j += 1
            }
            count += j - (mid + 1)
        }
        let slice = Array(nums[start...end]).sorted()
        for (offset, value) in slice.enumerated() {
            nums[start + offset] = value
        }
        return count
    }
}
