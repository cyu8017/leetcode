// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

class Solution {
    fun partitionLabels(s: String): MutableList<Int> {
        var last = IntArray(26)
        for (i in 0 until s.length) { last[s[i] - 'a'] = i }
        var start = 0
        var end = 0
        var answer = ArrayList<Int>()
        for (i in 0 until s.length) {
            end = maxOf(end, last[s[i] - 'a'])
            if (i == end) {
                answer.add(end - start + 1)
                start = i + 1
            }
        }
        return answer
    }
}
