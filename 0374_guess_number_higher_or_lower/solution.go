// LeetCode 0374 - Guess Number Higher or Lower
// https://leetcode.com/problems/guess-number-higher-or-lower/

func guess(num int) int {
	_ = num
	return 0
}

func guessNumber(n int) int {
	left := 1
	right := n

	for left <= right {
		mid := left + (right-left)/2
		result := guess(mid)
		if result == 0 {
			return mid
		}
		if result < 0 {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return left
}
