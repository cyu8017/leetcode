// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution {
    func longestSubarray(_ nums: [Int], _ limit: Int) -> Int {
        var low = [Int](), high = [Int]()
        var left = 0, answer = 0
        for (right, value) in nums.enumerated() {
            while !low.isEmpty && nums[low.last!] > value { low.removeLast() }
            while !high.isEmpty && nums[high.last!] < value { high.removeLast() }
            low.append(right); high.append(right)
            while nums[high[0]] - nums[low[0]] > limit {
                left += 1
                if low[0] < left { low.removeFirst() }
                if high[0] < left { high.removeFirst() }
            }
            answer = max(answer, right - left + 1)
        }
        return answer
    }
}
