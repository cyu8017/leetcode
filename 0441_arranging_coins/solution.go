// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

func arrangeCoins(n int) int {
	low, high := 0, n
	for low <= high {
		mid := low + (high-low)/2
		if mid*(mid+1)/2 <= n {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return high
}
