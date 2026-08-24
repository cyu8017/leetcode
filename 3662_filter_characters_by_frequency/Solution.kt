// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

class Solution {
    fun filterCharacters(s: String, k: Int): String {
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        var ans = StringBuilder()
        for (char c : s.toCharArray())
            if (cnt[c - 'a'] < k) ans.append(c)
        return ans.toString()
    }
}
