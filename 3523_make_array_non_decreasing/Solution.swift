// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

class Solution {
    func maximumPossibleSize(_ nums: [Int]) -> Int {
        var ans = 0, mx = 0
        for x in nums {
            if mx <= x {
                ans += 1
                mx = x
            }
        }
        return ans
    }
}
