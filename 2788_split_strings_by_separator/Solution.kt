// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

class Solution {
    fun splitWordsBySeparator(words: MutableList<String>, separator: Char): MutableList<String> {
        var ans = ArrayList<String>()
        for (w in words) {
            var start = 0
            for (i in 0 ..w.length) {
                if (i == w.length || w[i] == separator) {
                    if (i > start) ans.add(w.substring(start, i))
                    start = i + 1
                }
            }
        }
        return ans
    }
}
