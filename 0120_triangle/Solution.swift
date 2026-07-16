class Solution {
    func minimumTotal(_ triangle: [[Int]]) -> Int {
        var dp = triangle[triangle.count - 1]
        for rowIndex in stride(from: triangle.count - 2, through: 0, by: -1) {
            for index in triangle[rowIndex].indices {
                dp[index] = triangle[rowIndex][index] + min(dp[index], dp[index + 1])
            }
        }
        return dp[0]
    }
}