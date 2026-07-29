// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

class Solution {
    fun largestValsFromLabels(values: IntArray, labels: IntArray, numWanted: Int, useLimit: Int): Int {
        val n = values.size
        val idx = Array(n) { it }
        idx.sortByDescending { values[it] }
        val used = mutableMapOf<Int, Int>()
        var ans = 0
        var taken = 0
        for (i in idx) {
            if (taken == numWanted) break
            val label = labels[i]
            val count = used.getOrDefault(label, 0)
            if (count < useLimit) {
                used[label] = count + 1
                ans += values[i]
                taken++
            }
        }
        return ans
    }
}
