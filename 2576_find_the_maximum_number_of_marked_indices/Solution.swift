// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution {
    func maxNumOfMarkedIndices(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        let n = nums.count
        var i = 0, ans = 0
        for j in ((n + 1) / 2)..<n {
            if 2 * nums[i] <= nums[j] {
                ans += 2
                i += 1
            }
        }
        return ans
    }
}
