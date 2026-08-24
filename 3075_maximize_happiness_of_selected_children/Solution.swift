// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

class Solution {
    func maximumHappinessSum(_ happiness: [Int], _ k: Int) -> Int {
        let h = happiness.sorted()
        var ans = 0
        for i in 0..<k {
            let x = h[h.count - i - 1] - i
            ans += max(x, 0)
        }
        return ans
    }
}
