// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/


class Solution {
    func concatWithReverse(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: 2 * n)
        for i in 0..<n {
            ans[i] = nums[i]
            ans[i + n] = nums[n - i - 1]
        }
        return ans
    }
}
