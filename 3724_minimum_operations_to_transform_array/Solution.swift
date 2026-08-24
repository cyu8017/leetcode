// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var ans = 1
        let n = nums1.count
        var ok = false
        var d = 1 << 30
        for i in 0..<n {
            let x = max(nums1[i], nums2[i])
            let y = min(nums1[i], nums2[i])
            ans += x - y
            d = min(d, min(abs(x - nums2[n]), abs(y - nums2[n])))
            if nums2[n] >= y && nums2[n] <= x { ok = true }
        }
        if !ok { ans += d }
        return ans
    }
}
