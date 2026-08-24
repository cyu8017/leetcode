// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
    func longestAlternatingSubarray(_ nums: [Int], _ threshold: Int) -> Int {
        var ans = 0
        let n = nums.count
        for i in 0..<n {
            if nums[i] % 2 != 0 || nums[i] > threshold { continue }
            var j = i
            while j + 1 < n && nums[j + 1] <= threshold && nums[j + 1] % 2 != nums[j] % 2 { j += 1 }
            ans = max(ans, j - i + 1)
        }
        return ans
    }
}
