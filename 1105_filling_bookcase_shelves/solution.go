// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

func minHeightShelves(books [][]int, shelfWidth int) int {
	n := len(books)
	dp := make([]int, n+1)
	const inf = int(^uint(0) >> 1)
	for i := 1; i <= n; i++ {
		width, height := 0, 0
		dp[i] = inf
		for j := i; j >= 1; j-- {
			w, h := books[j-1][0], books[j-1][1]
			width += w
			if width > shelfWidth {
				break
			}
			if h > height {
				height = h
			}
			if dp[j-1]+height < dp[i] {
				dp[i] = dp[j-1] + height
			}
		}
	}
	return dp[n]
}
