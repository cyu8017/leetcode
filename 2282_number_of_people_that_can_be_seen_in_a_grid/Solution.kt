// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

class Solution {

    fun seePeople(heights: Array<IntArray>): Array<IntArray> {

            var m = heights.size; var n = heights[0].size
            var ans = arrayOfNulls<IntArray>(m)
            for (i in 0 until m) { ans[i] = IntArray(n) }
            for (i in 0 until m) {
                var stack = ArrayList<Int>()
                for (j in n - 1 downTo 0) {
                    var cnt = 0
                    while (stack.size > 0 && heights[i][stack[stack.size - 1]] < heights[i][j]) { stack.removeAt(stack.size - 1); cnt++; }
                    if (stack.size > 0) cnt++
                    ans[i][j] += cnt
                    while (stack.size > 0 && heights[i][stack[stack.size - 1]] == heights[i][j]) stack.removeAt(stack.size - 1)
                    stack.add(j)
                }
            }
            for (j in 0 until n) {
                var stack = ArrayList<Int>()
                for (i in m - 1 downTo 0) {
                    var cnt = 0
                    while (stack.size > 0 && heights[stack[stack.size - 1]][j] < heights[i][j]) { stack.removeAt(stack.size - 1); cnt++; }
                    if (stack.size > 0) cnt++
                    ans[i][j] += cnt
                    while (stack.size > 0 && heights[stack[stack.size - 1]][j] == heights[i][j]) stack.removeAt(stack.size - 1)
                    stack.add(i)
                }
            }
            return ans

    }

}
