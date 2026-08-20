// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

import "sort"

func minimumLines(stockPrices [][]int) int {
	if len(stockPrices) <= 1 {
		return 0
	}
	sort.Slice(stockPrices, func(i, j int) bool { return stockPrices[i][0] < stockPrices[j][0] })
	ans := 1
	for i := 2; i < len(stockPrices); i++ {
		x0, y0 := stockPrices[i-2][0], stockPrices[i-2][1]
		x1, y1 := stockPrices[i-1][0], stockPrices[i-1][1]
		x2, y2 := stockPrices[i][0], stockPrices[i][1]
		// (y1-y0)/(x1-x0) != (y2-y1)/(x2-x1)
		if int64(y1-y0)*int64(x2-x1) != int64(y2-y1)*int64(x1-x0) {
			ans++
		}
	}
	return ans
}
