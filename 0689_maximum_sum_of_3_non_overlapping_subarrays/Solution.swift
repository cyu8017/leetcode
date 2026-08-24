// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution {
    func maxSumOfThreeSubarrays(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        let windows = n - k + 1
        var sums = Array(repeating: 0, count: windows)
        var total = nums[0..<k].reduce(0, +)
        sums[0] = total
        if windows > 1 {
            for i in 1..<windows {
                total += nums[i + k - 1] - nums[i - 1]
                sums[i] = total
            }
        }
        var left = Array(repeating: 0, count: windows)
        var best = 0
        for i in 0..<windows {
            if sums[i] > sums[best] { best = i }
            left[i] = best
        }
        var right = Array(repeating: 0, count: windows)
        best = windows - 1
        for i in stride(from: windows - 1, through: 0, by: -1) {
            if sums[i] >= sums[best] { best = i }
            right[i] = best
        }
        var answer = [0, 0, 0]
        var bestTotal = -1
        if k < windows - k {
            for mid in k..<(windows - k) {
                let l = left[mid - k], r = right[mid + k]
                let cur = sums[l] + sums[mid] + sums[r]
                if cur > bestTotal {
                    bestTotal = cur
                    answer = [l, mid, r]
                }
            }
        }
        return answer
    }
}
