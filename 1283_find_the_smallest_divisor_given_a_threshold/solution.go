// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

func smallestDivisor(nums []int, threshold int) int {
	lo, hi := 1, nums[0]
	for _, x := range nums {
		if x > hi {
			hi = x
		}
	}
	for lo < hi {
		mid := (lo + hi) / 2
		sum := 0
		for _, x := range nums {
			sum += (x + mid - 1) / mid
		}
		if sum <= threshold {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
