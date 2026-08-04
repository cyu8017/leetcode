// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

func minSwaps(data []int) int {
	ones := 0
	for _, x := range data {
		ones += x
	}
	if ones <= 1 {
		return 0
	}
	cur := 0
	for i := 0; i < ones; i++ {
		cur += data[i]
	}
	best := cur
	for i := ones; i < len(data); i++ {
		cur += data[i] - data[i-ones]
		if cur > best {
			best = cur
		}
	}
	return ones - best
}
