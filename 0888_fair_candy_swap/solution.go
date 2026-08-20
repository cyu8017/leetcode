// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

func fairCandySwap(aliceSizes []int, bobSizes []int) []int {
	sumA, sumB := 0, 0
	for _, a := range aliceSizes {
		sumA += a
	}
	bob := map[int]bool{}
	for _, b := range bobSizes {
		sumB += b
		bob[b] = true
	}
	diff := (sumA - sumB) / 2
	for _, a := range aliceSizes {
		if bob[a-diff] {
			return []int{a, a - diff}
		}
	}
	return nil
}
