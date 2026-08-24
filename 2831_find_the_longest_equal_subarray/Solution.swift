// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
    func longestEqualSubarray(_ nums: [Int], _ k: Int) -> Int {
        var pos: [Int: [Int]] = [:]
        for i in nums.indices { pos[nums[i], default: []].append(i) }
        var ans = 0
        for p in pos.values {
            var left = 0
            for right in p.indices {
                while p[right] - p[left] - (right - left) > k { left += 1 }
                ans = max(ans, right - left + 1)
            }
        }
        return ans
    }
}
