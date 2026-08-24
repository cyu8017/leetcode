// LeetCode 3904 - Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/

class Solution {
    func firstStableIndex(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var right = [Int](repeating: 0, count: n)
        right[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                right[i] = min(right[i + 1], nums[i])
            }
        }
        var left = 0
        for i in 0..<n {
            left = max(left, nums[i])
            if left - right[i] <= k { return i }
        }
        return -1
    }
}
