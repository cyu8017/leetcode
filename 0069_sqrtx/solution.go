// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

func mySqrt(x int) int {
	if x < 2 {
		return x
	}

	left := 2
	right := x / 2

	for left <= right {
		mid := left + (right-left)/2
		square := mid * mid
		if square == x {
			return mid
		}
		if square < x {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return right
}
