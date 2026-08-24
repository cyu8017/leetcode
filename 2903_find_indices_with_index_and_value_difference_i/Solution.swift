// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution {
    func findIndices(_ nums: [Int], _ indexDifference: Int, _ valueDifference: Int) -> [Int] {
        let n = nums.count
        for i in 0..<n {
            for j in i..<n {
                if abs(j - i) >= indexDifference && abs(nums[i] - nums[j]) >= valueDifference {
                    return [i, j]
                }
            }
        }
        return [-1, -1]
    }
}
