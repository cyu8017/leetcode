// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

class Solution {
    func longestSubarray(_ nums: [Int], _ k: Int) -> Int {
        var cnt = [Int: Int]()
        var ans = 0, cur = 0, l = 0
        for r in 0..<nums.count {
            cnt[nums[r], default: 0] += 1
            if cnt[nums[r]] == 2 { cur += 1 }
            while cur > k {
                cnt[nums[l], default: 0] -= 1
                if cnt[nums[l]] == 1 { cur -= 1 }
                l += 1
            }
            ans = max(ans, r - l + 1)
        }
        return ans
    }
}
