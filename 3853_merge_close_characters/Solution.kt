// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

class Solution {
    fun mergeCharacters(s: String, k: Int): String {
        var last = HashMap<Char, Int>()
        var ans = StringBuilder()
        for (c in s.toCharArray()) {
            var cur = ans.length
            if (last.containsKey(c) && cur - last[c] <= k) continue
            ans.append(c)
            last[c] = cur
        }
        return ans.toString()
    }
}
