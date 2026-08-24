// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

class Solution {
    fun buddyStrings(s: String, goal: String): Boolean {
        if (s.length != goal.length) return false
        if ((s == goal)) {
            var set = HashSet<Char>()
            for (ch in s.toCharArray()) { if (!set.add(ch)) return true }
            return false
        }
        var diffs = ArrayList<IntArray>()
        for (i in 0 until s.length) {
            if (s[i] != goal[i]) {
                diffs.add(intArrayOf(s[i], goal[i]))
            }
        }
        return diffs.size == 2
            && diffs.get(0)[0] == diffs.get(1)[1]
            && diffs[0][1] == diffs[1][0]
    }
}
