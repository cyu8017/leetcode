// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/


class Solution {
    fun checkInclusion(s1: String, s2: String): Boolean {
        val n1 = s1.length
        val n2 = s2.length
        if (n1 > n2) return false
        val need = IntArray(26)
        val window = IntArray(26)
        for (i in 0 until n1) {
            need[s1[i] - 'a']++
            window[s2[i] - 'a']++
        }
        var matches = 0
        for (i in 0 until 26) if (need[i] == window[i]) matches++
        if (matches == 26) return true
        for (right in n1 until n2) {
            val add = s2[right] - 'a'
            val remove = s2[right - n1] - 'a'
            if (window[add] == need[add]) matches--
            window[add]++
            if (window[add] == need[add]) matches++
            if (window[remove] == need[remove]) matches--
            window[remove]--
            if (window[remove] == need[remove]) matches++
            if (matches == 26) return true
        }
        return false
    }
}
