// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

class Solution {
    func reversePrefix(_ word: String, _ ch: Character) -> String {
        var arr = Array(word)
        guard let pos = arr.firstIndex(of: ch) else { return word }
        var l = 0, r = pos
        while l < r {
            arr.swapAt(l, r)
            l += 1
            r -= 1
        }
        return String(arr)
    }
}
