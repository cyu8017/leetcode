// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution {
    fun removeAlmostEqualCharacters(word: String): Int {
        var ans = 0
        var n = word.length
        var i = 1
        while (i < n) {
            if (kotlin.math.abs(word[i] - word[i - 1]) <= 1) {
                ans++
                i += 2
            } else i++
        }
        return ans
    }
}
