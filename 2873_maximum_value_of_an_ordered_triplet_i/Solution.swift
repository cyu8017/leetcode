// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution {
    func maximumTripletValue(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in (i + 1)..<n {
                for k in (j + 1)..<n {
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
                }
            }
        }
        return ans
    }
}
