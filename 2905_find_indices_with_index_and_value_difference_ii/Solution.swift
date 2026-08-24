// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution {
    func findIndices(_ nums: [Int], _ indexDifference: Int, _ valueDifference: Int) -> [Int] {
        let n = nums.count
        var minIdx = 0, maxIdx = 0
        var j = indexDifference
        while j < n {
            let i = j - indexDifference
            if nums[i] < nums[minIdx] { minIdx = i }
            if nums[i] > nums[maxIdx] { maxIdx = i }
            if nums[j] - nums[minIdx] >= valueDifference { return [minIdx, j] }
            if nums[maxIdx] - nums[j] >= valueDifference { return [maxIdx, j] }
            j += 1
        }
        return [-1, -1]
    }
}
