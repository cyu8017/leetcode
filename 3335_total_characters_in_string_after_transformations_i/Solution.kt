// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution {
    fun lengthAfterTransformations(s: String, t: Int): Int {
        val mod = 1_000_000_007
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a'] = cnt[c - 'a'] + 1 }
        for (step in 0 until t) {
            var ncnt = IntArray(26)
            for (i in 0 until 25) { ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod }
            ncnt[0] = (ncnt[0] + cnt[25]) % mod
            ncnt[1] = (ncnt[1] + cnt[25]) % mod
            cnt = ncnt
        }
        var ans = 0
        for (v in cnt) { ans = (ans + v) % mod }
        return ans
    }
}
