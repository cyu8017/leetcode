// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

func maximumBooks(books []int) int64 {
	n := len(books)
	dp := make([]int64, n)
	stack := []int{}
	var ans int64
	sum := func(l, r, h int) int64 {
		// take from shelf l..r ending with height h at r, decreasing by 1 leftward
		width := r - l + 1
		if h >= width {
			return int64(width) * int64(2*h-width+1) / 2
		}
		return int64(h) * int64(h+1) / 2
	}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && books[stack[len(stack)-1]] >= books[i]-(i-stack[len(stack)-1]) {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			dp[i] = sum(0, i, books[i])
		} else {
			j := stack[len(stack)-1]
			dp[i] = dp[j] + sum(j+1, i, books[i])
		}
		if dp[i] > ans {
			ans = dp[i]
		}
		stack = append(stack, i)
	}
	return ans
}
