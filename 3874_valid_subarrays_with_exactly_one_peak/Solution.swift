// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

class Solution {
    func validSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var peaks = [Int]()
        if n > 2 {
            for i in 1..<(n - 1) {
                if nums[i] > nums[i - 1] && nums[i] > nums[i + 1] { peaks.append(i) }
            }
        }
        var ans = 0
        for j in 0..<peaks.count {
            let p = peaks[j]
            var leftMin = max(p - k, 0)
            if j > 0 { leftMin = max(leftMin, peaks[j - 1] + 1) }
            var rightMax = min(p + k, n - 1)
            if j < peaks.count - 1 { rightMax = min(rightMax, peaks[j + 1] - 1) }
            ans += (p - leftMin + 1) * (rightMax - p + 1)
        }
        return ans
    }
}
