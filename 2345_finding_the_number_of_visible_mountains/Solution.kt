// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

class Solution {
    fun visibleMountains(peaks: Array<IntArray>): Int {
        val arr = peaks.map { intArrayOf(it[0] - it[1], it[0] + it[1]) }.toMutableList()
        arr.sortWith(compareBy({ it[0] }, { -it[1] }))
        var ans = 0
        var maxR = Int.MIN_VALUE
        var i = 0
        while (i < arr.size) {
            var j = i
            while (j < arr.size && arr[j][0] == arr[i][0] && arr[j][1] == arr[i][1]) j++
            if (arr[i][1] > maxR) {
                if (j - i == 1) ans++
                maxR = arr[i][1]
            }
            i = j
        }
        return ans
    }
}
