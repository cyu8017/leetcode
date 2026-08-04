// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

func maximizeSweetness(sweetness []int, k int) int {
	total := 0
	for _, v := range sweetness {
		total += v
	}
	lo, hi := 1, total/(k+1)
	for lo <= hi {
		mid := (lo + hi) / 2
		pieces, current := 0, 0
		for _, value := range sweetness {
			current += value
			if current >= mid {
				pieces++
				current = 0
			}
		}
		if pieces >= k+1 {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return hi
}
