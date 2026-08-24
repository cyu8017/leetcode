// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

class Solution {
    func shortestSuperstring(_ s1: String, _ s2: String) -> String {
        if s1.count > s2.count { return shortestSuperstring(s2, s1) }
        if s2.contains(s1) { return s2 }
        let a = Array(s1), b = Array(s2)
        let m = a.count
        for i in 0..<m {
            let suf = String(a[i...])
            if s2.hasPrefix(suf) { return String(a[0..<i]) + s2 }
            let len = m - i
            if b.count >= len && Array(b[(b.count - len)...]) == Array(a[0..<len]) {
                return s2 + String(a[(m - i)...])
            }
        }
        return s1 + s2
    }
}
