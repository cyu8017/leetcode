// LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var a = nums
        var ans = 0
        for i in 0..<a.count where a[i] == 0 {
            if i + 2 >= a.count { return -1 }
            a[i + 1] ^= 1
            a[i + 2] ^= 1
            ans += 1
        }
        return ans
    }
}
