// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

class Solution {
    func minimumSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = Int.max
        for j in 1..<(n - 1) {
            var left = Int.max, right = Int.max
            for i in 0..<j where nums[i] < nums[j] {
                left = min(left, nums[i])
            }
            for k in (j + 1)..<n where nums[k] < nums[j] {
                right = min(right, nums[k])
            }
            if left < Int.max && right < Int.max {
                ans = min(ans, left + nums[j] + right)
            }
        }
        return ans == Int.max ? -1 : ans
    }
}
