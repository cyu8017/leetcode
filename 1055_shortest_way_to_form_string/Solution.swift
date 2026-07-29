// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

class Solution {
    func shortestWay(_ source: String, _ target: String) -> Int {
        let sourceChars = Array(source)
        let targetChars = Array(target)
        let sourceSet = Set(sourceChars)
        for ch in targetChars {
            if !sourceSet.contains(ch) {
                return -1
            }
        }
        var ans = 0
        var i = 0
        let n = targetChars.count
        while i < n {
            ans += 1
            for ch in sourceChars {
                if i < n && targetChars[i] == ch {
                    i += 1
                }
            }
        }
        return ans
    }
}
