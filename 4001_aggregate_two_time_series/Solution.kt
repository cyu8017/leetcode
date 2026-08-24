// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

class Solution {
    fun aggregateTimeSeries(series1: Array<IntArray>, series2: Array<IntArray>): Array<IntArray> {
        var m = series1.size
        var n = series2.size
        var i = 0
        var j = 0
        var ans = ArrayList<IntArray>()
        while (i < m && j < n) {
            var t1 = series1[i][0]
            var v1 = series1[i][1]
            var t2 = series2[j][0]
            var v2 = series2[j][1]
            if (t1 == t2) {
                ans.add(intArrayOf( t1, v1 + v2 ))
                i++
                j++
            } else if (t1 < t2) {
                ans.add(intArrayOf( t1, v1 + v2 ))
                i++
            } else {
                ans.add(intArrayOf( t2, v1 + v2 ))
                j++
            }
        }
        while (i < m) {
            ans.add(intArrayOf( series1[i][0], series1[i][1] ))
            i++
        }
        while (j < n) {
            ans.add(intArrayOf( series2[j][0], series2[j][1] ))
            j++
        }
        return ans.toArray(IntArray(ans.size)[])
    }
}
