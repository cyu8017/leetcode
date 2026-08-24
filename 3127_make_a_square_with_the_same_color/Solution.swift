// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution {
    func canMakeSquare(_ grid: [[Character]]) -> Bool {
        let dirs = [0, 0, 1, 1, 0]
        for i in 0..<2 {
            for j in 0..<2 {
                var cnt1 = 0, cnt2 = 0
                for k in 0..<4 {
                    let x = i + dirs[k], y = j + dirs[k + 1]
                    if grid[x][y] == "W" { cnt1 += 1 }
                    else { cnt2 += 1 }
                }
                if cnt1 != cnt2 { return true }
            }
        }
        return false
    }
}
