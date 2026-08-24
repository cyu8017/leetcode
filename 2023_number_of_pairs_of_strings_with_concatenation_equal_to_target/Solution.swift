// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution {
    func numOfPairs(_ nums: [String], _ target: String) -> Int {
        var ans = 0
        for i in 0..<nums.count {
            for j in 0..<nums.count where i != j && nums[i] + nums[j] == target {
                ans += 1
            }
        }
        return ans
    }
}
