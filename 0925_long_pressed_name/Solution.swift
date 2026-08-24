// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

class Solution {
    func isLongPressedName(_ name: String, _ typed: String) -> Bool {
        let n = Array(name), t = Array(typed)
        var i = 0, j = 0
        while j < t.count {
            if i < n.count && n[i] == t[j] { i += 1; j += 1 }
            else if j > 0 && t[j] == t[j - 1] { j += 1 }
            else { return false }
        }
        return i == n.count
    }
}
