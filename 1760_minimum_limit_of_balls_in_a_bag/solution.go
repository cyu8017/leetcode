// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

func minimumSize(nums []int, maxOperations int) int {
	lo, hi := 1, 0
	for _, x := range nums {
		if x > hi {
			hi = x
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		ops := 0
		for _, x := range nums {
			ops += (x - 1) / mid
		}
		if ops <= maxOperations {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
