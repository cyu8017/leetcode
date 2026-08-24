// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var f = [nums[0]: 0]
        if nums.count > 1 {
            for i in 1..<nums.count {
                let x = nums[i]
                var g = [Int: Int]()
                for (pre, s) in f {
                    var cur = (x + pre - 1) / pre * pre
                    while cur <= 100 {
                        let val = s + (cur - x)
                        if g[cur] == nil || g[cur]! > val { g[cur] = val }
                        cur += pre
                    }
                }
                f = g
            }
        }
        return f.values.min() ?? 0
    }
}
