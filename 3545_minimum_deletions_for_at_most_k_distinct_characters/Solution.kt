// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

class Solution {
    fun minDeletion(s: String, k: Int): Int {
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        cnt.sort()
        var ans = 0
        run {
            var i = 0
            while (i + k < 26) {
                ans += cnt[i]
                i = i + 1
            }
        }
        return ans
    }
}
