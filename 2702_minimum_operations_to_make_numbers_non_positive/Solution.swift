// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

class Solution {
    func minOperations(_ nums: [Int], _ x: Int, _ y: Int) -> Int {
        var lo = 0
        var hi = 0
        for v in nums {
            hi = max(hi, (v + y - 1) / y)
            hi = max(hi, (v + x - 1) / x)
        }
        hi += nums.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if ok(nums, x, y, mid) { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func ok(_ nums: [Int], _ x: Int, _ y: Int, _ ops: Int) -> Bool {
        var extra = 0
        for v in nums {
            let remain = v - ops * y
            if remain > 0 { extra += (remain + (x - y) - 1) / (x - y) }
        }
        return extra <= ops
    }
}
