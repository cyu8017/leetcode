// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution {
    func minimumLines(_ stockPrices: [[Int]]) -> Int {
        if stockPrices.count <= 1 { return 0 }
        let p = stockPrices.sorted { $0[0] < $1[0] }
        var ans = 1
        if p.count >= 3 {
            for i in 2..<p.count {
                let x0 = p[i - 2][0], y0 = p[i - 2][1]
                let x1 = p[i - 1][0], y1 = p[i - 1][1]
                let x2 = p[i][0], y2 = p[i][1]
                if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0) { ans += 1 }
            }
        }
        return ans
    }
}
