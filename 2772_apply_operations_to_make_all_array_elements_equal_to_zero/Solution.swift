// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

class Solution {
    func checkArray(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            let need = nums[i] - cur
            if need < 0 { return false }
            if need > 0 {
                if i + k > n { return false }
                cur += need
                diff[i + k] -= need
            }
        }
        return true
    }
}
