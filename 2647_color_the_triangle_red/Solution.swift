// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

class Solution {
    func colorRed(_ n: Int) -> [[Int]] {
        var ans: [[Int]] = []
        for i in 1...n { ans.append([i, 1]) }
        var i = n % 2 + 2
        while i <= n {
            let hi = 2 * (n - i) + 2
            if hi >= 2 {
                for j in 2...hi { ans.append([i, j]) }
            }
            i += 2
        }
        return ans
    }
}
