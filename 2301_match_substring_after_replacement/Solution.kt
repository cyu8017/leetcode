// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

class Solution {

    fun matchReplacement(s: String, sub: String, mappings: Array<CharArray>): Boolean {

            var allow = HashSet<Int>()
            for (m in mappings) allow.add((m[0] << 8) | m[1])
            var n = s.length; var mlen = sub.length
            run {
    var i = 0
    while (i + mlen <= n) {

                var ok = true
                for (j in 0 until mlen) {
                    var a = s[i + j]; var b = sub[j]
                    if (a == b || allow.contains((b << 8) | a)) continue
                    ok = false
                    break
                }
                if (ok) return true

    i++
    }
    }
            return false

    }

}
