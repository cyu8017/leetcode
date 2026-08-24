// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution {
    fun numSplits(s: String): Int {
        val right = HashMap<Char, Int>()
        for (ch in s) {
            right[ch] = right.getOrDefault(ch, 0) + 1
        }
        val left = HashSet<Char>()
        var answer = 0
        for (i in 0 until s.length - 1) {
            val ch = s[i]
            left.add(ch)
            val count = right[ch]!! - 1
            if (count == 0) right.remove(ch) else right[ch] = count
            if (left.size == right.size) answer++
        }
        return answer
    }
}
