// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

class Solution {
    func minLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = n + 1, l = 0
        var cnt = [Int: Int]()
        var s = 0
        for r in 0..<n {
            cnt[nums[r], default: 0] += 1
            if cnt[nums[r]] == 1 { s += nums[r] }
            while s >= k {
                if r - l + 1 < ans { ans = r - l + 1 }
                let left = nums[l]
                cnt[left]! -= 1
                if cnt[left] == 0 {
                    cnt.removeValue(forKey: left)
                    s -= left
                }
                l += 1
            }
        }
        return ans > n ? -1 : ans
    }
}
