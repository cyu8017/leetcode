// LeetCode 2287 - Rearrange Characters to Make Target String
// https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution {

    fun rearrangeCharacters(s: String, target: String): Int {

            var sc = IntArray(26), tc = IntArray(26)
            for (c in s.toCharArray()) sc[c - 'a']++
            for (c in target.toCharArray()) tc[c - 'a']++
            var ans = Int.MAX_VALUE
            for (i in 0 until 26) {
                if (tc[i] == 0) continue
                ans = minOf(ans, sc[i] / tc[i])
            }
            return ans

    }

}
