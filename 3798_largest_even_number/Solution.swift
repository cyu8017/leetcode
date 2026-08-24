// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

class Solution {
    func largestEven(_ s: String) -> String {
        var s = s
        while !s.isEmpty && s.last == "1" { s.removeLast() }
        return s
    }
}
