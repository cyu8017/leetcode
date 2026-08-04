// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution {
    fun hasAllCodes(s: String, k: Int): Boolean {
        if (s.length < k) return false
        val set = HashSet<String>()
        for (i in 0..s.length - k) {
            set.add(s.substring(i, i + k))
        }
        return set.size == (1 shl k)
    }
}
