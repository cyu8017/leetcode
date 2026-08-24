// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution {

    fun minimumLines(stockPrices: Array<IntArray>): Int {

            if (stockPrices.size <= 1) return 0
            stockPrices.sortWith {  a, b  ->  Integer.compare(a[0], b[0] })
            var ans = 1
            for (i in 2 until stockPrices.size) {
                var x0 = stockPrices[i - 2][0]; var y0 = stockPrices[i - 2][1]
                var x1 = stockPrices[i - 1][0]; var y1 = stockPrices[i - 1][1]
                var x2 = stockPrices[i][0]; var y2 = stockPrices[i][1]
                if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) ans++
            }
            return ans

    }

}
