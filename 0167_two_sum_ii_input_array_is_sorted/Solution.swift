// LeetCode 0167 - Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var left = 0, right = numbers.count - 1
        while left < right {
            let sum = numbers[left] + numbers[right]
            if sum == target { return [left + 1, right + 1] }
            if sum < target { left += 1 } else { right -= 1 }
        }
        return []
    }
}