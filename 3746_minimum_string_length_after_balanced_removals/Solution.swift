// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    func minLengthAfterRemovals(_ s: String) -> Int {
        var a = 0
        for c in s where c == "a" { a += 1 }
        let b = s.count - a
        return abs(a - b)
    }
}
