// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

class Solution {
    func repeatedStringMatch(_ a: String, _ b: String) -> Int {
        var s = a
        var count = 1
        while s.count < b.count {
            s += a
            count += 1
        }
        if s.contains(b) { return count }
        s += a
        if s.contains(b) { return count + 1 }
        return -1
    }
}
