// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

class Solution {
    func maxCaloriesBurnt(_ heights: [Int]) -> Int {
        let h = heights.sorted()
        var ans = 0
        var pre = 0, l = 0, r = h.count - 1
        while l < r {
            let d1 = h[r] - pre
            ans += d1 * d1
            let d2 = h[l] - h[r]
            ans += d2 * d2
            pre = h[l]
            l += 1
            r -= 1
        }
        let d = h[r] - pre
        ans += d * d
        return ans
    }
}
