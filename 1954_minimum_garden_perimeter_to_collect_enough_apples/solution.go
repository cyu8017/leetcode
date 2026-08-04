// LeetCode 1954 - Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

func minimumPerimeter(neededApples int64) int64 {
	lo, hi := int64(1), int64(100000)
	for lo < hi {
		mid := (lo + hi) / 2
		apples := 2 * mid * (mid + 1) * (2*mid + 1)
		if apples >= neededApples {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return 8 * lo
}
