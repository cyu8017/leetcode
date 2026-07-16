// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        var values = nums
        let target = values.count - k
        var left = 0
        var right = values.count - 1
        while left <= right {
            let pivotIndex = partition(&values, left, right)
            if pivotIndex == target {
                return values[pivotIndex]
            }
            if pivotIndex < target {
                left = pivotIndex + 1
            } else {
                right = pivotIndex - 1
            }
        }
        return values[left]
    }

    private func partition(_ nums: inout [Int], _ left: Int, _ right: Int) -> Int {
        let pivotIndex = left + Int.random(in: left...right)
        nums.swapAt(pivotIndex, right)
        var store = left
        for index in left..<right {
            if nums[index] <= nums[right] {
                nums.swapAt(store, index)
                store += 1
            }
        }
        nums.swapAt(store, right)
        return store
    }
}
