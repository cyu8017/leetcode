// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution {
    func resultsArray(_ nums: [Int], _ k: Int) -> [Int] {
        if k == 1 { return nums }
        let n = nums.count
        var ans = Array(repeating: 0, count: n - k + 1)
        var streak = 1
        for i in 1..<n {
            streak = nums[i] == nums[i - 1] + 1 ? streak + 1 : 1
            if i >= k - 1 { ans[i - k + 1] = streak >= k ? nums[i] : -1 }
        }
        return ans
    }
}
