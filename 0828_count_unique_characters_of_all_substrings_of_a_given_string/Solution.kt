// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution {
    fun uniqueLetterString(s: String): Int {
        var n = s.length
        var last = HashMap<Char, MutableList<Int>>()
        for (ch in s.toCharArray()) {
            last.computeIfAbsent(ch, k -> ArrayList(List.of(-1)))
        }
        for (i in 0 until n) { last[s[i]].add(i) }
        for (indices in last.values()) { indices.add(n) }
        var ans = 0
        for (indices in last.values()) {
            var k = 1
            while (k + 1 < indices.size) {
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k])
                k++
            }
        }
        return ans
    }
}
