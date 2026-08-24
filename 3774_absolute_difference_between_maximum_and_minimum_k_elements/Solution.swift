// LeetCode 3774 - Absolute Difference Between Maximum And Minimum K Elements
// https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution {
    func absDifference(_ nums: [Int], _ k: Int) -> Int {
        let a = nums.sorted()
        var ans = 0
        let n = a.count
        for i in 0..<k { ans += a[n - i - 1] - a[i] }
        return ans
    }
}
