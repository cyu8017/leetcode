// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

class Solution {
    func stringShift(_ s: String, _ shift: [[Int]]) -> String {
        var offset = 0
        for sh in shift { offset += sh[0] == 1 ? sh[1] : -sh[1] }
        let n = s.count
        offset = ((offset % n) + n) % n
        if offset == 0 { return s }
        let chars = Array(s)
        return String(chars[(n - offset)...] + chars[..<(n - offset)])
    }
}
