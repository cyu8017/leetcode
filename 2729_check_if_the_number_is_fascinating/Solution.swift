// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution {
    func isFascinating(_ n: Int) -> Bool {
        let s = String(n) + String(2 * n) + String(3 * n)
        if s.count != 9 { return false }
        var cnt = Array(repeating: 0, count: 10)
        for c in s { cnt[Int(String(c))!] += 1 }
        if cnt[0] != 0 { return false }
        for i in 1...9 where cnt[i] != 1 { return false }
        return true
    }
}
