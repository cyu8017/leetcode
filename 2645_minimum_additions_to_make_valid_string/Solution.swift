// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
    func addMinimum(_ word: String) -> Int {
        var ans = 0
        var expect = 0
        var i = 0
        let chars = Array(word)
        let n = chars.count
        while i < n {
            let need = Character(UnicodeScalar(Int(UnicodeScalar("a").value) + expect)!)
            if chars[i] == need { i += 1 } else { ans += 1 }
            expect = (expect + 1) % 3
        }
        ans += (3 - expect) % 3
        return ans
    }
}
