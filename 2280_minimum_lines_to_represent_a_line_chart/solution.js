// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

var minimumLines = function(stockPrices) {
    if (stockPrices.length <= 1) return 0;
    stockPrices.sort((a, b) => a[0] - b[0]);
    let ans = 1;
    for (let i = 2; i < stockPrices.length; i++) {
        const x0 = stockPrices[i - 2][0], y0 = stockPrices[i - 2][1];
        const x1 = stockPrices[i - 1][0], y1 = stockPrices[i - 1][1];
        const x2 = stockPrices[i][0], y2 = stockPrices[i][1];
        if ((y1 - y0) * (x2 - x1) !== (y2 - y1) * (x1 - x0)) ans++;
    }
    return ans;
};
