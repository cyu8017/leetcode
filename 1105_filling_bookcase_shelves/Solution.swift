// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

class Solution {
    func minHeightShelves(_ books: [[Int]], _ shelfWidth: Int) -> Int {
        let n = books.count
        var dp = [Int](repeating: 0, count: n + 1)
        for i in 1...n {
            var width = 0, height = 0
            dp[i] = Int.max
            for j in stride(from: i, through: 1, by: -1) {
                let w = books[j - 1][0], h = books[j - 1][1]
                width += w
                if width > shelfWidth { break }
                height = max(height, h)
                dp[i] = min(dp[i], dp[j - 1] + height)
            }
        }
        return dp[n]
    }
}
