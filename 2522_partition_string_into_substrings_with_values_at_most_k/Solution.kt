// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution {
    fun minimumPartition(s: String, k: Int): Int {
        var ans = 1
        var cur = 0
        for (ch in s.toCharArray()) {
            var d = ch - '0'
            if (d > k) return -1
            var nxt = cur * 10 + d
            if (nxt > k) {
                ans = ans + 1
                cur = d
            } else {
                cur = nxt
            }
        }
        return ans
    }
}
