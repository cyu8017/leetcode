// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution {
    func cellsInRange(_ s: String) -> [String] {
        let chars = Array(s)
        var ans = [String]()
        var c = chars[0]
        while c <= chars[3] {
            var r = chars[1]
            while r <= chars[4] {
                ans.append(String([c, r]))
                r = Character(UnicodeScalar(r.asciiValue! + 1))
            }
            c = Character(UnicodeScalar(c.asciiValue! + 1))
        }
        return ans
    }
}
