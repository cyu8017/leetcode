// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution {
    func maximumTop(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 1 { return k % 2 != 0 ? -1 : nums[0] }
        if k == 0 { return nums[0] }
        var ans = -1
        let limit = min(k - 1, n)
        for i in 0..<limit { ans = max(ans, nums[i]) }
        if k < n { ans = max(ans, nums[k]) }
        return ans
    }
}
