// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

class Solution {
    func replicate(_ str: String, _ times: Int) -> String {
        if times <= 0 { return "" }
        return String(repeating: str, count: times)
    }
}
