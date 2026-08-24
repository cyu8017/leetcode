// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

class Solution {
    func largeGroupPositions(_ s: String) -> [[Int]] {
        let chars = Array(s)
        var ans = [[Int]]()
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] { j += 1 }
            if j - i >= 3 { ans.append([i, j - 1]) }
            i = j
        }
        return ans
    }
}
