// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution {
    fun isPossibleToRearrange(s: String, t: String, k: Int): Boolean {
        var n = s.length
        var sz = n / k
        var cnt = HashMap<Int, Int>()
        var i = 0
        while (i < n) {
            var a = s.substring(i, sz), b = t.substring(i, sz)
            if (!cnt.containsKey(a)) cnt[a] = 0
            cnt[a] = cnt[a] + 1
            if (!cnt.containsKey(b)) cnt[b] = 0
            cnt[b] = cnt[b] - 1
            i += sz
        }
        for (v in cnt.values) if (v != 0) return false
        return true
    }
}
