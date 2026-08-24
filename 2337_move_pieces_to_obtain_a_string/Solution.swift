// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution {
    func canChange(_ start: String, _ target: String) -> Bool {
        let s = Array(start), t = Array(target)
        let n = s.count
        var i = 0, j = 0
        while i < n || j < n {
            while i < n && s[i] == "_" { i += 1 }
            while j < n && t[j] == "_" { j += 1 }
            if i == n || j == n { return i == n && j == n }
            if s[i] != t[j] { return false }
            if s[i] == "L" && i < j { return false }
            if s[i] == "R" && i > j { return false }
            i += 1
            j += 1
        }
        return true
    }
}
