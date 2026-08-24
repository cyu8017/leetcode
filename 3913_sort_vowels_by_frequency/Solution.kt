// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

class Solution {
    fun sortVowels(s: String): String {
        val st = HashSet<Char>()
        for (c in charArrayOf('a', 'e', 'i', 'o', 'u')) st.add(c)
        val vowels = ArrayList<Char>()
        val cnt = HashMap<Char, Int>()
        for (c in s.toCharArray()) {
            if (!st.contains(c)) continue
            if (!cnt.containsKey(c)) {
                vowels.add(c)
                cnt[c] = 0
            }
            cnt[c] = cnt[c]!! + 1
        }
        vowels.sortWith(compareByDescending { cnt[it]!! })
        val ans = s.toCharArray()
        var i = 0
        for (k in s.indices) {
            if (!st.contains(s[k])) continue
            val ch = vowels[i]
            ans[k] = ch
            cnt[ch] = cnt[ch]!! - 1
            if (cnt[ch] == 0) i++
        }
        return String(ans)
    }
}
