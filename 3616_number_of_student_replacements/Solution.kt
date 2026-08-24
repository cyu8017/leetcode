// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

class Solution {
    fun totalReplacements(ranks: IntArray): Int {
        var ans = 0
        var cur = ranks[0]
        for (x in ranks) {
            if (x < cur) {
                cur = x
                ans++
            }
        }
        return ans
    }
}
