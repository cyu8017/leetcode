// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

func maxLength(ribbons []int, k int) int {
	can := func(length int) bool {
		total := 0
		for _, ribbon := range ribbons {
			total += ribbon / length
		}
		return total >= k
	}

	hi := ribbons[0]
	for _, ribbon := range ribbons[1:] {
		if ribbon > hi {
			hi = ribbon
		}
	}

	lo := 1
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if can(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	if can(lo) {
		return lo
	}
	return 0
}
