// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

class Solution {
    func minimumBoxes(_ n: Int) -> Int {
        var height = 0
        var used = 0
        var base = 0
        while used + (height + 1) * (height + 2) / 2 <= n {
            height += 1
            let layer = height * (height + 1) / 2
            used += layer
            base += height
        }
        var extra = 0
        while used < n {
            extra += 1
            used += extra
        }
        return base + extra
    }
}
