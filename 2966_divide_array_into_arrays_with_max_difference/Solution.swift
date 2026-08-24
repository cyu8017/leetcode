// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution {
    func divideArray(_ nums: [Int], _ k: Int) -> [[Int]] {
        let nums = nums.sorted()
        var ans: [[Int]] = []
        var i = 0
        while i < nums.count {
            if nums[i + 2] - nums[i] > k { return [] }
            ans.append([nums[i], nums[i + 1], nums[i + 2]])
            i += 3
        }
        return ans
    }
}
