// LeetCode 2158 - Amount of New Area Painted Each Day
// https://leetcode.com/problems/amount-of-new-area-painted-each-day/

class Solution {
    fun amountPainted(paint: Array<IntArray>): IntArray {
        var ans: IntArray = IntArray(paint.size), line = IntArray(50001)
        for (i in 0 until paint.size) {
            var start: Int = paint[i][0], end = paint[i][1], j = start
            while (j < end) {
                if (line[j] == 0) {
                    ans[i]++
                    line[j] = end
                    j++
                } else {
                    var next: Int = line[j]
                    line[j] = maxOf(end, next)
                    j = next
                }
            }
        }
        return ans
    }
}
