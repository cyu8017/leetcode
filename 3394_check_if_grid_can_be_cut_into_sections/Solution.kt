// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

class Solution {
    private fun checkCut(rects: Array<IntArray>, axis: Int): Boolean {
        val arr = Array(rects.size) { IntArray(2) }
        for (i in rects.indices) {
            if (axis == 0) {
                arr[i][0] = rects[i][0]
                arr[i][1] = rects[i][2]
            } else {
                arr[i][0] = rects[i][1]
                arr[i][1] = rects[i][3]
            }
        }
        arr.sortWith { x, y ->
            if (x[0] == y[0]) x[1].compareTo(y[1]) else x[0].compareTo(y[0])
        }
        var cuts = 0
        var end = arr[0][1]
        for (i in 1 until arr.size) {
            if (arr[i][0] >= end) {
                cuts++
                end = arr[i][1]
                if (cuts >= 2) return true
            } else if (arr[i][1] > end) {
                end = arr[i][1]
            }
        }
        return false
    }

    fun checkValidCuts(n: Int, rectangles: Array<IntArray>): Boolean =
        checkCut(rectangles, 0) || checkCut(rectangles, 1)
}
