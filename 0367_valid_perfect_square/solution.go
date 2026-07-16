// LeetCode 0367 - Valid Perfect Square
// https://leetcode.com/problems/valid-perfect-square/

func isPerfectSquare(num int) bool {
	left := 1
	right := num

	for left <= right {
		mid := left + (right-left)/2
		square := mid * mid
		if square == num {
			return true
		}
		if square < num {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false
}
