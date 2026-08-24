// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

class Solution {
    private var mp: MutableMap<String, String>? = null

    fun applySubstitutions(replacements: MutableList<MutableList<String>>, text: String): String {
        mp = HashMap()
        for (r in replacements) { mp[r[0]] = r[1] }
        return resolve(text)
    }

    private fun resolve(s: String): String {
        var out = StringBuilder()
        var i = 0
        while (i < s.length) {
            if (s[i] == '%') {
                var j = i + 1
                while (j < s.length && s[j] != '%') j++
                var key = s.substring(i + 1, j)
                out.append(resolve(mp[key]))
                i = j + 1
            } else {
                out.append(s[i])
                i = i + 1
            }
            
        }
        return out.toString()
    }
}
