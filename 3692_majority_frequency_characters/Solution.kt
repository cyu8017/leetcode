// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

class Solution {
    fun majorityFrequencyGroup(s: String): String {
        val cnt = IntArray(26)
        for (c in s) cnt[c - 'a']++
        val f = HashMap<Int, StringBuilder>()
        for (i in 0 until 26) {
            if (cnt[i] > 0) {
                f.getOrPut(cnt[i]) { StringBuilder() }.append(('a'.code + i).toChar())
            }
        }
        var mx = 0
        var mv = 0
        var ans = ""
        for ((v, sb) in f) {
            val cs = sb.toString()
            if (cs.length > mx || (cs.length == mx && v > mv)) {
                mx = cs.length
                mv = v
                ans = cs
            }
        }
        return ans
    }
}
