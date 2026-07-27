// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution {
    fun minDeletions(s: String): Int {
        val freq = IntArray(26)
        for (c in s) freq[c - 'a']++
        val used = HashSet<Int>()
        var ans = 0
        for (f in freq) {
            var x = f
            while (x > 0 && x in used) {
                x--
                ans++
            }
            if (x > 0) used.add(x)
        }
        return ans
    }
}
