// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

class Solution {
    func minimumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        var mn = Int.max
        for i in 0..<n {
            left[i] = mn
            mn = min(mn, nums[i])
        }
        mn = Int.max
        for i in stride(from: n - 1, through: 0, by: -1) {
            right[i] = mn
            mn = min(mn, nums[i])
        }
        var ans = Int.max
        for j in 1..<(n - 1) {
            if left[j] < nums[j] && right[j] < nums[j] {
                ans = min(ans, left[j] + nums[j] + right[j])
            }
        }
        return ans == Int.max ? -1 : ans
    }
}
