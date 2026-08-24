// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

class Solution {
    fun calculateScore(s: String): Long {
        val stacks = Array(26) { ArrayList<Int>() }
        var ans = 0L
        for (i in 0 until s.length) {
            val ci = s[i] - 'a'
            val mir = 25 - ci
            if (stacks[mir].isNotEmpty()) {
                val j = stacks[mir].removeAt(stacks[mir].size - 1)
                ans += (i - j).toLong()
            } else {
                stacks[ci].add(i)
            }
        }
        return ans
    }
}
