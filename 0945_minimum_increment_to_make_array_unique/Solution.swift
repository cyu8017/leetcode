// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution {
    func minIncrementForUnique(_ nums: [Int]) -> Int {
        var a = nums.sorted()
        var ans = 0
        for i in 1..<a.count {
            if a[i] <= a[i - 1] {
                let need = a[i - 1] + 1
                ans += need - a[i]
                a[i] = need
            }
        }
        return ans
    }
}
