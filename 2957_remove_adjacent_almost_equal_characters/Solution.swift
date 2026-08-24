// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution {
    func removeAlmostEqualCharacters(_ word: String) -> Int {
        let chars = Array(word)
        var ans = 0, i = 1
        while i < chars.count {
            if abs(Int(chars[i].asciiValue!) - Int(chars[i - 1].asciiValue!)) <= 1 {
                ans += 1
                i += 2
            } else {
                i += 1
            }
        }
        return ans
    }
}
