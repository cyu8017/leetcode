// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

class Solution {
    fun minAbsDiff(grid: Array<IntArray>, k: Int): Array<IntArray> {
        var m = grid.size
        var n = grid[0].size
        var ans = arrayOfNulls<IntArray>(m - k + 1)
        for (i in 0..m - k) { ans[i] = IntArray(n - k + 1) }
        for (i in 0..m - k) {
            for (j in 0..n - k) {
                var nums = ArrayList<Int>()
                var x: Int = i
while (x < i + k) {

                    for (y in j until j + k) { nums.add(grid[x][y]) }
                nums.sort(null)
                var d = Int.MAX_VALUE
                for (t in 1 until nums.size) {
                    if (nums[t] != nums[t - 1]) d = minOf(d, kotlin.math.abs(nums[t] - nums[t - 1]))
                }
                if (d != Int.MAX_VALUE) ans[i][j] = d
            }
        }
        return ans
    }
}
x = x + 1
}
