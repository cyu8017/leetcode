// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var a1 = nums1, a2 = nums2
        let n = a1.count
        var ans = calc(a1, a2)
        let t = a1[n - 1]
        a1[n - 1] = a2[n - 1]
        a2[n - 1] = t
        ans = min(ans, calc(a1, a2) + 1)
        return ans >= (1 << 30) ? -1 : ans
    }

    private func calc(_ a1: [Int], _ a2: [Int]) -> Int {
        let n = a1.count
        var ops = 0
        let last1 = a1[n - 1], last2 = a2[n - 1]
        for i in 0..<(n - 1) {
            let x = a1[i], y = a2[i]
            if x <= last1 && y <= last2 { continue }
            if y <= last1 && x <= last2 {
                ops += 1
                continue
            }
            return 1 << 30
        }
        return ops
    }
}
