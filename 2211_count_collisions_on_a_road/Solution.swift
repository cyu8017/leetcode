// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

class Solution {
    func countCollisions(_ directions: String) -> Int {
        let s = Array(directions)
        var i = 0, j = s.count - 1
        while i < s.count && s[i] == "L" { i += 1 }
        while j >= 0 && s[j] == "R" { j -= 1 }
        var ans = 0
        if i <= j {
            for k in i...j where s[k] != "S" { ans += 1 }
        }
        return ans
    }
}
