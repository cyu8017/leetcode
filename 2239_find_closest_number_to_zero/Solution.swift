// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

class Solution {
    func findClosestNumber(_ nums: [Int]) -> Int {
        var ans = nums[0]
        for x in nums {
            if abs(x) < abs(ans) || (abs(x) == abs(ans) && x > ans) { ans = x }
        }
        return ans
    }
}
