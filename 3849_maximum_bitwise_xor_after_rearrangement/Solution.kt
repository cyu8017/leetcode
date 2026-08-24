// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution {
    fun maximumXor(s: String, t: String): String {
        var cnt = IntArray(2)
        for (c in t.toCharArray()) { cnt[c - '0']++ }
        var ans = CharArray(s.length)
        for (i in 0 until s.length) {
            var x = s[i] - '0'
            if (cnt[x ^ 1] > 0) {
                cnt[x ^ 1]--
                ans[i] = '1'
            } else {
                cnt[x]--
                ans[i] = '0'
            }
        }
        return String(ans)
    }
}
