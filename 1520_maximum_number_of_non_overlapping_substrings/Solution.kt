// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

class Solution {
    fun maxNumOfSubstrings(s: String): List<String> {
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }
        for (i in s.indices) {
            val index = s[i] - 'a'
            if (first[index] == -1) first[index] = i
            last[index] = i
        }
        val intervals = mutableListOf<IntArray>()
        for (i in s.indices) {
            val ch = s[i] - 'a'
            if (first[ch] != i) continue
            var end = last[ch]
            var j = i
            var valid = true
            while (j <= end) {
                val cj = s[j] - 'a'
                if (first[cj] < i) {
                    valid = false
                    break
                }
                end = maxOf(end, last[cj])
                j++
            }
            if (valid) intervals.add(intArrayOf(end, i))
        }
        intervals.sortBy { it[0] }
        val answer = mutableListOf<String>()
        var previousEnd = -1
        for (interval in intervals) {
            val end = interval[0]
            val start = interval[1]
            if (start > previousEnd) {
                answer.add(s.substring(start, end + 1))
                previousEnd = end
            }
        }
        answer.sortBy { it.length }
        return answer
    }
}
